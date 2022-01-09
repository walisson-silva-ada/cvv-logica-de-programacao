notas = {'W':1,'H': 1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T': 1/32, 'X':1/64}
composicao = input("Digite a composição, separando os compassos por /").upper()
lista = composicao.split("/")

incorretos = []
corretos = []

for compasso in lista:
    somatorio = []
    for nota in compasso:
        somatorio.append(notas[nota])
    if sum(somatorio) == 1 and compasso.isalpha():
        corretos.append(compasso)
    if sum(somatorio) != 1 and compasso.isalpha():
        incorretos.append(compasso)


print(f"Quantidade de corretos: {len(corretos)}")
if len(incorretos) != 0:
    print(f"Incorretos: {incorretos}")