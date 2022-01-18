def super_digito(numero, fator):
    novo_numero = int(str(numero)*fator)
    lista = [int(num) for num in str(novo_numero)]

    if len(lista) == 1:
        return lista
    else:
        return super_digito(sum(lista), 1)


super_digito(123, 3)
