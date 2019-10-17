from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

if __name__=='__main__':
    app.run(debug=True)