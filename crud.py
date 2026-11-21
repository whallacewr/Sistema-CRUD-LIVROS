from dados import livros

def cadastrar_livro():

  try:
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    preco = float(input("Digite o preço do livro: "))
    quantidade = int(input("Digite a quantidade de livros: "))

  except ValueError:
    print("Digite os valores numéricos corretos!")

  else:
    if titulo == "" or autor == "" or preco < 0  or quantidade < 0:
        print("Os campos título/autor não podem estar vazios e os " \
        "campos preço/quantidade não podem ser menores que 0.")

    else:
        novo_livro = { 
        "codigo": len(livros) + 1,
        "titulo": titulo,
        "autor": autor,
        "preco": preco,
        "quantidade": quantidade
        }

        livros.append(novo_livro)
