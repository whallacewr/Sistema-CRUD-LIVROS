from arquivo import carregar_livros, salvar_livros
from utils import validar_isbn

livros = carregar_livros()


def cadastrar_livro():
    """Função para realizar o cadastro do livro."""

    try:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        genero = input("Digite o gênero do livro: ")
        estado = input("Digite o estado de conservação do livro: ")
        preco = float(input("Digite o preço do livro: "))
        quantidade = int(input("Digite a quantidade de livros: "))

    except ValueError:
        print("Digite os valores numéricos corretos.")

    else:
        if not validar_isbn(isbn):
            print("O ISBN está inválido. Por favor digite exatamente 13 números.")

        elif not titulo.strip() or not autor.strip() or preco <= 0 or quantidade < 0:
            print(
                "Os campos título/autor não podem estar vazios, o campo "
                "preço deve ser maior que 0 e a quantidade não pode ser menor que 0."
            )

        else:
            for livro in livros:
                if livro["isbn"] == isbn:
                    print(
                        "Esse ISBN já está cadastrado no acervo, por favor digite outro ISBN. "
                    )
                    return

            maior_codigo = 0

            for livro in livros:
                if livro["codigo"] > maior_codigo:
                    maior_codigo = livro["codigo"]

            novo_livro = {
                "codigo": maior_codigo + 1,
                "titulo": titulo,
                "autor": autor,
                "isbn": isbn,
                "genero": genero,
                "estado": estado,
                "preco": preco,
                "quantidade": quantidade,
            }

            livros.append(novo_livro)
            salvar_livros(livros)

            print("Parabéns. O livro foi cadastrado com sucesso.")


def listar_livros():
    """Função para mostrar os livros cadastrados no acervo."""

    if not livros:
        print("O acervo está vazio.")

    else:
        print("LISTA DE LIVROS CADASTRADOS NO ACERVO: \n")

        print(
            f"{'CÓDIGO':<8} | {'TÍTULO':<25} | {'AUTOR':<25} | "
            f"{'GÊNERO':<12} | {'PREÇO':<10} | {'QUANTIDADE':<8}"
        )
        print("-" * 110)

        for livro in livros:
            titulo = livro["titulo"]

            if len(titulo) > 25:
                titulo = titulo[:22] + "..."

            preco_duas_casas = f"R$ {livro['preco']:.2f}"
            # Variável para o preço ajustado para duas casas decimais.

            print(
                f"{livro['codigo']:<8} | {titulo:<25} | {livro['autor']:<25} | "
                f"{livro['genero']:<12} | {preco_duas_casas:<10} | {livro['quantidade']:<8}"
            )


def buscar_livro():
    """Função para buscar livros no acervo."""

    print("1 - Buscar por código")
    print("2 - Buscar por título")

    opcao = input("Escolha uma opção entre 1 e 2: ")

    if opcao == "1":
        print("Você escolheu buscar por código.")

        try:
            codigo_livro = int(input("Digite o código do livro: "))

        except ValueError:
            print("Digite os valores numéricos corretos.")
            return

        encontrado = False

        for livro in livros:
            if codigo_livro == livro["codigo"]:
                encontrado = True

                print("O livro foi encontrado no acervo.")

                print("Código:", livro["codigo"])
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("ISBN:", livro["isbn"])
                print("Gênero:", livro["genero"])
                print("Estado de conservação:", livro["estado"])
                print("Preço:", livro["preco"])
                print("Quantidade:", livro["quantidade"])

        if not encontrado:
            print("O livro não foi encontrado no acervo.")

    elif opcao == "2":
        print("Você escolheu buscar por título.")

        buscar_titulo = input("Digite o título do livro: ").lower()

        encontrado = False

        for livro in livros:
            titulo_do_livro = livro["titulo"].lower().strip()

            if buscar_titulo in titulo_do_livro:
                encontrado = True
                print("Livro encontrado.")
                print("Código:", livro["codigo"])
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("ISBN:", livro["isbn"])
                print("Gênero:", livro["genero"])
                print("Estado de conservação:", livro["estado"])
                print("Preço:", livro["preco"])
                print("Quantidade:", livro["quantidade"])

        if not encontrado:
            print("O livro não foi encontrado no acervo.")

    else:
        print("Você escolheu uma opção inválida. Digite 1 ou 2.")


def editar_livro():
    """Função para editar os dados de um livro."""

    try:
        codigo_livro = int(input("Digite o código do livro: "))

    except ValueError:
        print("Código inválido. Só números são aceitos.")
        return

    encontrado = False

    for livro in livros:
        if codigo_livro == livro["codigo"]:
            encontrado = True

            print("Livro encontrado.")
            print("Código:", livro["codigo"])
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("ISBN:", livro["isbn"])
            print("Gênero:", livro["genero"])
            print("Estado de conservação:", livro["estado"])
            print("Preço:", livro["preco"])
            print("Quantidade:", livro["quantidade"])

            print("O livro foi encontrado no acervo, agora digite os novos dados: ")

            try:
                novo_titulo = (
                    input("Digite o título do novo livro: ") or livro["titulo"]
                )
                novo_autor = (
                    input("Digite o nome do autor do novo livro: ") or livro["autor"]
                )
                novo_isbn = input("Digite o novo ISBN do livro: ") or livro["isbn"]
                novo_genero = (
                    input("Digite o gênero do novo livro: ") or livro["genero"]
                )
                novo_estado = (
                    input("Digite o estado de conservação do novo livro: ")
                    or livro["estado"]
                )
                novo_preco = float(
                    input("Digite o preço do novo livro: ") or livro["preco"]
                )
                nova_quantidade = int(
                    input("Digite a quantidade do novo livro: ") or livro["quantidade"]
                )
                # Caso o usuário aperte 'enter', o valor será mantido.

                if novo_genero not in (
                    "Romance",
                    "Ficção",
                    "Cordel",
                    "Poesia",
                    "Didático",
                    "Infantil",
                    "Biografia",
                    "Outros",
                ):

                    print("O gênero é inválido.")
                    return

                if novo_estado not in ("Ótimo", "Bom", "Regular"):
                    print("O estado de conservação é inválido.")
                    return

                if not validar_isbn(novo_isbn):
                    print(
                        "O ISBN está inválido. Por favor digite exatamente 13 números."
                    )
                    return

                for outro_livro in livros:
                    if (
                        outro_livro["isbn"] == novo_isbn
                        and outro_livro["codigo"] != codigo_livro
                    ):
                        print(
                            "Esse ISBN já pertence a outro livro. Por favor digite outro."
                        )
                        return

                if (
                    novo_titulo.strip() == ""
                    or novo_autor.strip() == ""
                    or novo_preco <= 0
                    or nova_quantidade < 0
                ):

                    print(
                        "Os campos título/autor não podem estar vazios, o campo "
                        "preço tem que ser maior que 0 e a quantidade não pode ser menos que 0."
                    )

                else:
                    livro["titulo"] = novo_titulo
                    livro["autor"] = novo_autor
                    livro["isbn"] = novo_isbn
                    livro["genero"] = novo_genero
                    livro["estado"] = novo_estado
                    livro["preco"] = novo_preco
                    livro["quantidade"] = nova_quantidade

                    salvar_livros(livros)

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
            salvar_livros(livros)

            print("Ótimo. A exclusão foi feita com sucesso.")
            break

    if not encontrado:
        print("O livro não foi encontrado no acervo.")
