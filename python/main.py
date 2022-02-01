import requests, json

def buscar_dados():
    response = requests.get("https://api.randomuser.me/?results=10")
    dados = json.loads(response.content);
    dados_tratados = tratar_dados(dados["results"]);
    # print(dados["results"][0]["dob"]) 
    print(dados_tratados);

def tratar_dados(objeto):
    new_dado = [];
    for i in range(10):
        # print(objeto[i]) 
        del objeto[i]["dob"]
        # new_dado["age"] = objeto[i]["dob"]["age"]
        # new_dado["first_name"] = objeto[i]["name"]["first"]
        # new_dado["last_name"] = objeto[i]["name"]["last"]
        # new_dado["picture"] = objeto[i]["picutres"]
        
        return objeto
if __name__ == '__main__':
    buscar_dados()