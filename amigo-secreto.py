nb = input('Digite a quantidade de participantes: ')
while nb.isnumeric == False or int(nb) < 1:
    nb = input('Digite a quantidade de participantes: ')
lista = {}
i = 0
print('Digite seu nome e 3 opcoes de presentes:')
while i < int(nb):
    usuario = input(f'{i + 1}:').lower()
    opcoes = usuario.split(' ')
    if len(opcoes) == 4:
        lista[opcoes[0]] = opcoes[1:]
        i += 1

while True:
    alternativa = input('Digite o nome e o presente do seu amigo secreto:\n').lower().split(' ')
    while len(alternativa) != 2:
        alternativa = input('Numero invalido de presentes.\nDigite o nome e o presente do seu amigo secreto:\n').lower().split(' ')
    nome = alternativa[0]
    presente = alternativa[1]

    acertou = False
    
    if nome in lista:
        for opcao in lista[nome]:
            if opcao == presente:
                acertou = True
        if acertou == True:
            print('Uhul! Seu amigo secreto vai adorar o/')
            break
        else:
            print('Tente Novamente!')