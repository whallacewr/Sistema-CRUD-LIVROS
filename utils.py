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

def validar_texto(valor):
    return bool(valor.strip()) 

def validar_isbn(isbn):
    isbn = isbn.strip()

    return isbn.isdigit() and len(isbn) == 13

def validar_preco(valor):
    try:
     preco = float(valor)

     if preco > 0:
        return True
     else:
        return False
    
    except ValueError:
     return False
         