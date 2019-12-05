from flask import Flask, request
from flask_cors import  CORS
from crawler import boleto

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/gerar-guia', methods=['POST'])
def gerar_pdf():
    nome = request.form['nome']
    num_doc = request.form['num_doc']
    insc_estadual = request.form['insc_estadual']
    cep = request.form['cep']
    endereco = request.form['endereco']
    bairro = request.form['bairro']
    cidade = request.form['cidade']
    uf = request.form['uf']
    cod_receita = request.form['cod_receita']
    obs = request.form['obs']
    data_vencimento = request.form['data_vencimento']
    num_nota = request.form['num_nota']
    valor = request.form['valor']
    return boleto(nome, num_doc, insc_estadual, cep, endereco, bairro, cidade, uf, cod_receita, obs, data_vencimento, num_nota, valor)

if __name__ == '__main__':
    app.run()