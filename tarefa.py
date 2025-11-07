#importa a conexao criada
from conexao import get_conexao

#importa a bibilioteca do psycog2
from psycopg2.extras import RealDictCursor

#importa o jsonfy do flask para
#retornar os dados no formato json 
from flask import jsonify

def buscar_tarefas():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, nome, descricao FROM tarefas;"
    )
    #Busca todos registros na tabela
    tarefas = cursor.fetchall()

    #Fecha as conexoes 
    cursor.close()
    conn.close()

    return jsonify(tarefas)
   