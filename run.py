from flask import Flask
app = Flask(__name__)

@app.route('/<numero>', methods=['GET', 'POST'])
def ola(numero):
    return 'Óla mundo! {}'.format(numero)


if __name__=='__main__':
    app.run(debug=True)


tarefas = [
    {'id': 0,
    'responsavel': 'Camila',
    'tarefa': 'Lavar Louça',
    'status': 'Incompleto'},
    {'id': 1,
    'responsavel': 'Karine',
    'tarefa': 'Pagar o Cartão',
    'status': 'Incompleto'},
    {'id': 2,
    'responsavel': 'Barbara',
    'tarefa': 'Pagar o Cartão',
    'status': 'Incompleto'},
    {'id': 3,
    'responsavel': 'Camila',
    'tarefa': 'Fazer comida',
    'status': 'Completo'}
]