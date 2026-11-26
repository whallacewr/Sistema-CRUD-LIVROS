from dados import livros

def cadastrar_livro():
  """Função para realizar o cadastro do livro."""

  try:
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    preco = float(input("Digite o preço do livro: "))
    quantidade = int(input("Digite a quantidade de livros: "))

  except ValueError:
    print("Digite os valores numéricos corretos.")

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
    """Função para mostrar os livros cadastrados no acervo."""

    if not livros:
        print("O acervo está vazio.")

    else:
        print("LISTA DE LIVROS CADASTRADOS NO ACERVO: \n")

        for livro in livros:
            print("Código:", livro["codigo"])
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Preço:", livro["preco"])
            print("Quantidade:", livro["quantidade"])
        
            print()

def buscar_livro():
  """Função para buscar livros no acervo."""

  codigo_livro = int(input("Digite o código do livro: "))

  encontrado = False

  for livro in livros:
     if codigo_livro == livro["codigo"]:
        encontrado = True

        print("O livro foi encontrado no acervo.")

        print("Código:", livro["codigo"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Preço:", livro["preco"])
        print("Quantidade:", livro["quantidade"])

  if not encontrado:
    print("O livro não foi encontrado no acervo.")

def editar_livro():
    """Função para editar os dados de um livro."""

    codigo_livro = int(input("Digite o código do livro: "))
    
    encontrado = False
    
    for livro in livros:
         if codigo_livro == livro["codigo"]:
            encontrado = True

            print("O livro foi encontrado no acervo, agora digite os novos dados: ")

            try:
                    novo_titulo = input("Digite o título do novo livro: ")
                    novo_autor = input("Digite o nome do autor do novo livro: ")
                    nova_quantidade = int(input("Digite a quantidade do novo livro: "))
                    novo_preco = float(input("Digite o preço do novo livro: "))

                    if novo_titulo.strip() == "" or novo_autor.strip() == "" or novo_preco < 0  or nova_quantidade < 0:

                        print("Os campos título/autor não podem estar vazios e os " \
                                                "campos preço/quantidade não podem ser menores que 0.")

                    else:
                          livro["titulo"] = novo_titulo
                          livro["autor"] = novo_autor
                          livro["quantidade"] = nova_quantidade
                          livro["preco"] = novo_preco

                          print("Parabéns! A atualização foi concluída. ")
                        

            except ValueError:
               print("Digite os valores numéricos corretos.")
         
    if not encontrado:
      print("O livro não foi encontrado no acervo.")

def excluir_livro():
    """Função para excluir um livro do acervo."""

    codigo_do_livro = int(input("Digite o código do livro: "))

    encontrado = False

    for livro in livros:
     if codigo_do_livro == livro["codigo"]:
        encontrado = True

        livros.remove(livro)
        print("Ótimo. A exclusão foi feita com sucesso.")
        break

    if not encontrado:
      print("O livro não foi encontrado no acervo.")



