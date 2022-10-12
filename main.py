from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    server_message = ''
    client_message = ''
    if request.method == 'POST':
        client_message = request.form.get('message')

    if client_message == 'hi':
        server_message = 'Hello'
    elif client_message != '':
        server_message = 'How are you?'

    return render_template(
        'index.html',
        message=server_message,
    )


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
