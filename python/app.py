from array import array
import json, requests
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def buscar_dados():
    response = requests.get("https://api.randomuser.me/?results=10")
    dados = json.loads(response.content);
    dados_tratados = tratar_dados(dados["results"]);
    return json.dumps(dados_tratados)

def tratar_dados(objeto):
    new_dado = [];
    for i in range(10):
        del objeto[i]["cell"];
        del objeto[i]["email"];
        del objeto[i]["phone"];
        del objeto[i]["nat"];
        del objeto[i]["registered"];
        del objeto[i]["login"]
        del objeto[i]["id"]
        del objeto[i]["gender"]
        
    return objeto

if __name__ == "__main__":
    app.run(port=3000)