from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    return {'id': id, 'nome': 'Camila Costa', 'profissao': 'Quimica'}



#app.route('/soma/<int:valor1>/<int:valor2>/')
#def soma(valor1, valor2):
#    soma = valor1 + valor2
#    return {'soma': soma}

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return {'soma': total}


if __name__=='__main__':
    app.run(debug=True)