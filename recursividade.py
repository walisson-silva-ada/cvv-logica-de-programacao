lista_n = [3,10,1,4,2,5,3]

def maior (lista):
    if len(lista) == 1:
        return lista[0]
    else:
        m = lista[0]
        return maior(lista[1:]) if maior(lista[1:])>m else m
maior(lista_n)