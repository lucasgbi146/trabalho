from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=80)])
    idade = StringField('Idade', validators=[DataRequired(), Length(max=20)])
    estado = StringField('Estado', validators=[DataRequired(), Length(max=20)])
    telefone = StringField('Telefone', validators=[DataRequired(), Length(min=11, max=11)])
    cidade = StringField('Cidade', validators=[DataRequired(), Length(max=25)])
    rg = StringField('RG', validators=[DataRequired(), Length(max=15)])
    cep = StringField('CEP', validators=[DataRequired(), Length(min=8, max=8)])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11, max=11)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    senha = StringField('Senha', validators=[DataRequired(), Length(max=20)])
    sobre_voce = StringField('Sobre você', validators=[DataRequired(), Length(min=20, max=400)])
    botao = SubmitField('Cadastar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=35)])
    senha = StringField('Senha', validators=[DataRequired(), Length(max=20)])
    botao = SubmitField('Cadastar')