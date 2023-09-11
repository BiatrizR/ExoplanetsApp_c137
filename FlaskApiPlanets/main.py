from flask import Flask, jsonify, request
#importar as bibliotecas request e jsonify para enviar os dados para o navegador
from dt import data
#importando o arquivo data de data.py

#configurando a API:
app = Flask(__name__)

#rota para apresentar todos os planetas
@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200
# a instrução return significa que queremos enviar os dados no navegador para exibi-los
# 200 indica execução bem sucedida

# !parte II 
# retornar apenas um planeta por vez
@app.route("/planet")
def planet():
    #A função requests.args é usada para obter o nome da URL
    name = request.args.get("name")
    
    #e a função next() cria um iterador e encontra no dicionário um elemento da lista planet_data que satisfaça a condição.
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()

# * como buscar o nome dos planetas
 # http://127.0.0.1:5000/planet?name=Canopus

 # ! 3.C137= RODAR NO PROJETO
 # * 4. INSTALAR NGROK E RODAR NA MESMA PORTA DE SERVIDOR QUE O PROJETO PYTHON. EX.: NGROK HTTP 5000