import requests

def buscar_dados():
    request = requests.get("https://api.randomuser.me/?results=10")
    return(request.content)

if __name__ == '__main__':
    buscar_dados()