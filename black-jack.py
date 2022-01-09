from random import randint

def criar_baralho():
    faces = {
        'A': 1,
        '2': 2,
        '3': 3, 
        '4': 4, 
        '5': 5, 
        '6': 6, 
        '7': 7, 
        '8': 8, 
        '9': 9, 
        '10': 10, 
        'J': 10, 
        'Q': 10, 
        'K': 10}
    naipes = {'O', 'P', 'C', 'E'}
    baralho = []
    carta = {}
    for face, valor in faces.items():
        for naipe in naipes:
            carta['face'] = face
            carta['naipe'] = naipe
            carta['valor'] = valor
            baralho.append(carta)
            carta = {}
    return baralho

def criar_mao_jogador(nomes_jogadores):
    jogadores = {}
    jogador = {}
    for nome in nomes_jogadores:
        jogador['ativo'] = True
        jogador['pontos'] = 0
        jogadores[nome] = jogador
        jogador = {}
    return jogadores

def sorteio(baralho:dict):
    tamanho = len(baralho)
    id_sorteado = randint(0, tamanho - 1)
    valor = baralho[id_sorteado]['valor']
    carta = f'{baralho[id_sorteado]["face"]} de valor {baralho[id_sorteado]["valor"]}'
    baralho.pop(id_sorteado)
    return valor, carta

def jogada(baralho:dict, jogadores:dict):
    for nome, jogador in jogadores.items():
        if jogador['ativo'] == True:
            joga = input(f'{nome}, quer comprar uma carta? (S/N)').strip().upper()
            while joga != 'S' and joga != 'N':
                joga = input('Opcao invalida! Quer comprar uma carta? (S/N)').strip().upper()
            if joga == 'N':
                jogador['ativo'] = False
                continue
            else:
                # print(f'{nome} tinha {jogador["pontos"]} pontos')
                pontos, carta = sorteio(baralho)
                jogador['pontos'] += pontos
                print(f'{nome} tirou uma carta {carta}')
                # print(f'{nome} agora tem {jogador["pontos"]} pontos')
                if jogador['pontos'] > 21:
                    jogador['ativo'] = False

def verifica(jogadores:dict):
    maior = 0
    vencedores = []
    for nome, jogador in jogadores.items():
        if jogador['pontos'] <= 21 and jogador['pontos'] > maior:
            maior = jogador['pontos']
            vencedores = []
            vencedores.append(nome)
        elif jogador['pontos'] <= 21 and jogador['pontos'] == maior:
            vencedores.append(nome)
    return vencedores, maior

def is_final(jogadores:dict):
    final = False
    finalizados = 0
    for nome, jogador in jogadores.items():
        if jogador['ativo'] == False:
            finalizados += 1
    if finalizados == len(jogadores):
        final = True
    return final

def black_jack():
    # Perguntar numero de jogadores e criar uma lista com o nome de cada um
    num_jogadores = input('Digite o numero de jogadores: ')
    while num_jogadores.isnumeric() == False or int(num_jogadores) <= 0:
        num_jogadores = input('Numero invalido.\nDigite o numero de jogadores: ')
    num_jogadores = int(num_jogadores)
    nomes_jogadores = []
    for i in range(num_jogadores):
        nomes_jogadores.append(input(f'Digite o numero do jogador {i + 1}: '))
        
    # Cria baralho
    baralho = criar_baralho()
    jogadores = criar_mao_jogador(nomes_jogadores)
    while True:
        jogada(baralho, jogadores)
        if is_final(jogadores) == True:
            vencedores, maior = verifica(jogadores)
            if maior == 0:
                print('Nao houve vencedores')
            elif maior > 0 and len(vencedores) == 1:
                print(f'Ganhou:\n{vencedores[0]}\nCom: {maior} pontos')
            else:
                print('Ganhou:')
                for nome in vencedores:
                    print(nome)
                print(f'Com: {maior} pontos')
            break

black_jack()