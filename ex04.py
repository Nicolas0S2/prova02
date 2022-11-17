#Nicolas Lamback de Paulo
linha = 5
coluna = 5


def preenche_matriz(linha, coluna):
    lista = list()
    for i in range(linha + 1):
        lista.append([0] * coluna)
    return lista


matriz = preenche_matriz(linha, coluna)


for li in range(linha):
    for co in range(coluna):
        if li == co:
            matriz[li][co] = 1

for i in range(linha):
    print(matriz[i])
