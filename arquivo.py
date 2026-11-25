import json

def carregar_livros():
    try:
     with open("dados/acervo.json", "r", encoding="utf-8")as arquivo:
      livros = json.load(arquivo)

     return livros


    except FileNotFoundError:
     print("Arquivo não encontrado. Iniciando acervo vazio.")
    return []


def salvar_livros(livros):
 with open("dados/acervo.json", "w", encoding="utf-8") as arquivo:
   json.dump(livros, arquivo, ensure_ascii=False, indent=4)
  