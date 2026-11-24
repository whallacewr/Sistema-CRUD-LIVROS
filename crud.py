from dados import livros

def cadastrar_livro():
    #Função para realizar o cadastro do livro.

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

def listar_livros():
    #Função para mostrar os livros cadastrados no acervo.

    if not livros:
        print("O acervo está vazio.")

    else:
        print("Livros cadastrados.")

        for livro in livros:
            print("Código:", livro["codigo"])
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Preço:", livro["preco"])
            print("Quantidade:", livro["quantidade"])
        
            print()
