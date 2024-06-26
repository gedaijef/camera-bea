from flask import Flask, render_template, render_template_string, request, jsonify
from flask_cors import CORS
import pandas as pd
from db_config import get_db_connection

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/salvar", methods=["POST"])
def salvar():
    data = request.json
    nr_inscricao = data["nr_inscricao"]
    data_presenca = data["data_presenca"]
    hora = data["hora"]

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        ## verificar se o aluno já marcou presença nessa data
        cur.execute("SELECT * FROM presenca WHERE nr_inscricao = %s AND data_presenca = %s", (nr_inscricao, data_presenca))
        rows = cur.fetchall()
        if len(rows) > 0:
            return jsonify({"status": "erro", "error": "Aluno ja marcou presença nessa data"}), 409
        
        cur.execute("INSERT INTO presenca (nr_inscricao, data_presenca, hora) VALUES (%s, %s, %s)", (nr_inscricao, data_presenca, hora))
        
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "ok"})
    except Exception as e:
        print("Erro: " + str(e))
        return jsonify({"status": "erro", "error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True, port=5500)