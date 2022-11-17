#Nicolas Lamback de Paulo
cont = 0
par = 0
maior = 0


def preenche_matriz(linha, coluna):
    lista = list()
    for i in range(linha + 1):
        lista.append([0] * coluna)
    return lista


linha = int(input('Digite o número de linhas:'))
coluna = int(input('Digite o número de colunas: '))
matriz = preenche_matriz(linha, coluna)


for li in range(linha):
    for co in range(coluna):
        cont += 1
        num = int(input(f'Digite o {cont}º numero de {linha * coluna}: '))
        matriz[li][co] = num
        if cont == 1:
            maior = num
        elif num > maior:
            maior = num
        if num % 2 == 0:
            par += 1


for i in range(linha):
    print(matriz[i])
print(f'O maior é {maior} e o nº de pares é {par}.')
