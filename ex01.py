#Nicolas Lamback de Paulo
def preenche_lista(tamanho):
    lista = list()
    for i in range(tamanho):
        lista.append(0)
    return lista


tamanho = int(input('Digite o número de elementos da lista: '))
lista = preenche_lista(tamanho)
for i in range(len(lista)):
    num = int(input(f'Digite o {i + 1}º número da lista: '))
    lista[i] = num

print('A lista.', lista)
print('A lista ordenada.', sorted(lista))
print('A soma dos valores.', sum(lista))
print('O maior número da lista.', max(lista))
