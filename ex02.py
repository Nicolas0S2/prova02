#Nicolas Lamback de Paulo
from random import  randint
qual_jogador = 'Jogador 1'
impar_par = 0
jogador1 = list()
jogador2 = list()
dado = list(range(1, 7))


while True:
    opcao = int(input(f'''
{qual_jogador}
[ 1 ] - Jogar
[ 2 ] - Sair
Digite a sua opção: '''))
    if opcao != 1:
        if impar_par % 2 != 0:
            jogador2.append(dado[randint(0, 5)])
            print(f'Último número do jogador 2: {jogador2[-1]}')
        break
    else:
        if impar_par % 2 == 0:
            jogador1.append(dado[randint(0, 5)])
            print(f'Número do jogador 1: {jogador1[-1]}')
            impar_par += 1
            qual_jogador = 'Jogador 2'
        else:
            jogador2.append(dado[randint(0, 5)])
            print(f'Número do jogador 2: {jogador2[-1]}')
            impar_par += 1
            qual_jogador = 'Jogador 1'


print('\nResultados: ')
print(f'Jogadas do jogador 1: {jogador1}')
print(f'Jogadas do jogador 2: {jogador2}')
print(f'Soma dos valores do jogador 1: {sum(jogador1)}')
print(f'Soma dos valores do jogador 2: {sum(jogador2)}')
if sum(jogador1) > sum(jogador2):
    print('O jogador 1 é o vencedor')
else:
    print('O jogador 2 é o vencedor')
print('Obrigada por Jogar!')