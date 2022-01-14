import requests
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

# def users():
#     return {"users": [{"name": "Bruno Palhano", "location": "rua Pedro Juscelino de Aquino", "picture": "https://randomuser.me/api/portraits/men/1.jpg"},
#         {"name": "Vitor", "location": "Moovery Jp", "picture": "https://randomuser.me/api/portraits/men/2.jpg"}, 
#         {"name": "Vinicius", "location": "Moovery Jp", "picture": "https://randomuser.me/api/portraits/men/3.jpg"}, 
#         {"name": "Thales", "location": "Moovery Jp", "picture": "https://randomuser.me/api/portraits/men/4.jpg"}, 
#         {"name": "João", "location": "Moovery Jp", "picture": "https://randomuser.me/api/portraits/men/5.jpg"}, 
#         {"name": "Yonara", "location": "Moovery Jp", "picture": "https://randomuser.me/api/portraits/women/2.jpg"}, 
#         {"name": "Larissa", "location": "Moovery Jp", "picture": "https://randomuser.me/api/portraits/women/3.jpg"}, 
#         {"name": "Elder", "location": "Moovery Jp", "picture": "https://randomuser.me/api/portraits/men/6.jpg"}, 
#         {"name": "Marye", "location": "Moovery Jp", "picture": "https://randomuser.me/api/portraits/women/4.jpg"}, 
#         {"name": "Ray", "location": "Moovery Jp", "picture": "https://randomuser.me/api/portraits/men/7.jpg"}, 
#         {"name": "Felipe", "location": "Moovery Jp", "picture": "https://randomuser.me/api/portraits/men/8.jpg"}
#         ]}

@app.route("/")
def buscar_dados():
    request = requests.get("https://api.randomuser.me/?results=10")
    dados = request.json()
    return dados

if __name__ == "__main__":
    app.run(port=3002)