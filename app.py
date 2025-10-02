from flask import Flask, render_template  # Adicione render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
       return render_template('index.html')
       
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']  # Removida a vírgula desnecessária
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return 'Login com sucesso'  # Redireciona para home em sucesso
        else:
            error = 'Credenciais inválidas. Tente novamente.'
    return render_template('login.html', error=error)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
