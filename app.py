from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html_code = '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Abrir Câmera</title>
    </head>
    <body>
        <button onclick="openCamera()">Abrir Câmera</button>

        <script>
            function openCamera() {
                const cameraUrl = 'intent://#Intent;action=android.media.action.IMAGE_CAPTURE;end';
                window.location.href = cameraUrl;
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)
