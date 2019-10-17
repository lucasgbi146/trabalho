from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cadastro.html')
def index():
    return render_template('/paginas/cadastro.html')

@app.route('/login.html')
def index():
    return render_template('/paginas/cadastro.html')

if __name__=='__main__':
    app.run(debug=True)