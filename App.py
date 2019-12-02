from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from formulario import CadastroForm, LoginForm

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///informacoes.db'
app.config['SECRET_KEY'] = 'dfsshfehryuakbfpefeg875368jgkdfoadydgkfbdfnlshobcl'

class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=False, nullable=False)
    idade = db.Column(db.Integer, unique=False, nullable=False)
    estado = db.Column(db.String(20), unique=False, nullable=False)
    telefone = db.Column(db.Integer, unique=True, nullable=False)
    cidade = db.Column(db.String(25), unique=False, nullable=False)
    rg = db.Column(db.Integer, unique=True, nullable=False)
    cep = db.Column(db.Integer, unique=False, nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    senha = db.Column(db.String(20), unique=False, nullable=False)
    sobre_voce = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Cadastro %r>' % self.cadastro


@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():

    form = CadastroForm()
    if form.validate_on_submit():
        Cadastro = Cadastro()
        cadastro.cadastro = form.cadastro.data
        db.session.add(cadastro)
        db.session.commit()
        
    print(form.nome.data)
    return render_template('paginas/cadastro.html', form=form)

@app.route('/login')
def login():

    form = LoginForm()

    return render_template('/paginas/cadastro.html')

if __name__=='__main__':
    app.run(debug=True)