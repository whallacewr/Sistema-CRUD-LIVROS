def validar_inteiro(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
