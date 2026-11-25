def validar_inteiro(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def validar_decimal(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
 