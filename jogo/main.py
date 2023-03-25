from random import randint
from time import sleep

import emo


# escolha do jogador
def escolha_jogador():
    jogador = int(input(f'[1]{emo.pedra()}\n'
                        f'[2]{emo.papel()}\n'
                        f'[3]{emo.tesoura()}\n'
                        'Escolha uma opção: '))
    if jogador == 1:
        return 1
    elif jogador == 2:
        return 2
    elif jogador == 3:
        return 3
# concertar essa parte
    while jogador not in [1, 2, 3]:
        print('Escolha invalida tente novamente: ')
        jogador = int(input(f'[1]{emo.pedra()}\n'
                            f'[2]{emo.papel()}\n'
                            f'[3]{emo.tesoura()}\n'
                            'Escolha uma opção: '))



def escolha_pc():
    return randint(1, 3)


def resultado(jg1, jg2):
    if jg1 == jg2:
        return 0
    elif jg1 == 1 and jg2 == 2:
        return -1
    elif jg1 == 2 and jg2 == 3:
        return -1
    elif jg1 == 3 and jg2 == 1:
        return -1
    elif jg1 == 1 and jg2 == 3:
        return 1
    elif jg1 == 2 and jg2 == 1:
        return 1
    elif jg1 == 3 and jg2 == 2:
        return 1


def jogo():
    print('interface')
    vidas = 3
    while vidas > 0:
        jogador = escolha_jogador()
        maquina = escolha_pc()
        resposta = resultado(jogador, maquina)
        if resposta == 0:
            print('Empate')
        elif resposta == -1:
            print('voce perdeu uma chance')
            vidas -= 1
            print(emo.vida(vidas))
        elif resposta == 1:
            print('Voce ganhou')
        if vidas == 0:
            print('suas vidas acabaram')
            break


jogo()
