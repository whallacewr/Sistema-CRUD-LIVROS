import json

def carregar_livros():
    try:
     with open("dados/acervo.json", "r", encoding="utf-8")as arquivo:
      livros = json.load(arquivo)

     return livros


    except FileNotFoundError:
     print("Arquivo não encontrado. Iniciando acervo vazio.")
    return []