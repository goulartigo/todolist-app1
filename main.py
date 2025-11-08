#importação de bibliotecas
from flask import Flask 
from tarefa import buscar_tarefas

#cria o objeto do flask
app = Flask(__name__)

#criando nossa primeira rota /api
@app.route('/api')
def index():
    return 'Api rodando'

#criando a rota que retorna as tarefas
@app.route ('/api/tarefas')   
def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas

#identifica que é o arquivo principal
#e liga o servidor executando o Flask 🤣
if __name__ == "__main__":
    app.run(debug=True)


    