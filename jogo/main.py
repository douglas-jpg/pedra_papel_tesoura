from time import sleep
from random import randint

import emo  # Modulo criado para facilitar os emojis.


def jogo():
    """
    Função para jogar pedra papel tesoura
    E apos terminar adiciona o nome e a
    Pontuação em um arquivo txt.
    """
    vidas = 3
    pontos = 0
    nome = str(input('Digite o seu nome jogador: '))

    sleep(0.75)
    # Inicio do jogo até as vidas acabarem.
    while vidas > 0:
        print(f'\n {nome} voce tem {vidas} vidas')
        emo.vida(vidas)
        print(f'[1] Pedra{emo.pedra()}\n'
              f'[2] Papel{emo.papel()}\n'
              f'[3] Tesoura{emo.tesoura()}\n'
              f'[999] Sair{emo.sair()}')
        jogador = int(input('Escolha sua opção: '))
        sleep(0.5)
        # Tratamento de erro para caso o usuario digite errado.
        while jogador not in [1, 2, 3, 999]:
            print('Opção errada, tente escolher uma dessas opções: ')
            jogador = int(input('Sua escolha: '))
        pc = randint(1, 3)  # Escolha do computador.
        # Caso houver empate entre o computador e o jogador.
        if jogador == pc:
            if jogador == 1:
                sleep(0.5)
                print('Ambus escolheram pedra')
                sleep(0.5)
                print(emo.empate_pedra())
            elif jogador == 2:
                sleep(0.5)
                print('Ambus escolheram papel')
                sleep(0.5)
                print(emo.empate_papel())
            else:
                sleep(0.5)
                print('Ambus escolheram tesoura')
                sleep(0.5)
                print(emo.empate_tesoura())
            print('Empate!')
            sleep(0.5)
        # Caso o computador ganhe uma rodada.
        elif (jogador == 1 and pc == 2 or
              jogador == 2 and pc == 3 or
              jogador == 3 and pc == 1):
            sleep(1)
            vidas -= 1  # O jogador perde uma vida.
            if jogador == 1:
                print('O jogador escolheu pedra')
                print(f'{emo.pedra()}', end='')
                print(' x ', end='')
            elif jogador == 2:
                print('O jogador escolheu papel')
                print(f'{emo.papel()}', end='')
                print(' x ', end='')
            elif jogador == 3:
                print('O jogador escolheu tesoura')
                print(f'{emo.tesoura()}', end='')
                print(' x ', end='')
            if pc == 1:
                print(emo.pedra())
                print('O pc escolheu pedra')
            elif pc == 2:
                print(emo.papel())
                print('O pc escolheu papel')
            else:
                print(emo.tesoura())
                print('O pc escolheu tesoura')
            print('Voce perdeu uma vida!')
        # Caso o jogador ganhe uma rodada.
        elif (jogador == 1 and pc == 3 or
              jogador == 2 and pc == 1 or
              jogador == 3 and pc == 2):
            sleep(0.5)
            pontos += 1  # É adicionado 1 ponto para o jogador.
            if jogador == 1:
                print('O jogador escolheu pedra')
                print(f'{emo.pedra()}', end='')
                print(' x ', end='')
            elif jogador == 2:
                print('O jogador escolheu papel')
                print(f'{emo.papel()}', end='')
                print(' x ', end='')
            elif jogador == 3:
                print('O jogador escolheu tesoura')
                print(f'{emo.tesoura()}', end='')
                print(' x ', end='')
            if pc == 1:
                print(emo.pedra())
                print('O pc escolheu pedra')
            elif pc == 2:
                print(emo.papel())
                print('O pc escolheu papel')
            else:
                print(emo.tesoura())
                print('O pc escolheu tesoura')
            print('Voce ganhou!')
        # Caso o jogador queira abadonar a partida.
        elif jogador == 999:
            break
    print('QUE PENA TODAS AS SUAS VIDAS ACAVARAM!!!')
    # Nome e pontos do jogador são adicionados no arquivo de pontuações.
    tabela = open('docs/pontuacao.txt', 'a', encoding='utf-8')
    tabela.write(f"{nome:<10} {pontos:>10}\n")


def main():
    """
    Função principal com o menu com várias funções.
    """
    print(f'{"-"*50}')  # letreiro inicial.
    print(f'BEM VINDO AO JOGO PEDRA{emo.pedra()}'
          f' PAPEL{emo.papel()} TESOURA{emo.tesoura()}!!!')
    print(f'{"-" * 50}')
    while True:
        print('[1] Jogar\n'
              '[2] Como Jogar\n'
              '[3] Pontuação\n'
              '[4] Creditos\n'
              '[5] Sair')
        opc = int(input(f'Escolha a opção: '))
        #  Tratamento de erro caso o usuario digite errado.
        while opc not in [1, 2, 3, 4, 5]:
            opc = int(input(f'Escolha uma opção valida: '))
        # Tela de carregamento simples.
        print('Carregando', end='')
        for i in range(3):
            sleep(0.33)
            print('.', end='')
        print('\n')
        # Inicia o jogo.
        if opc == 1:
            jogo()
        # Abri o arquivo e imprime as regras do jogo.
        elif opc == 2:
            regras = open('docs/regras.txt', 'r', encoding='utf-8')
            print(regras.read())
            regras.close()
        # Abre e imprime o arquivo da pontuação.
        elif opc == 3:
            pontuacao = open('docs/pontuacao.txt', 'r', encoding='utf-8')
            print(pontuacao.read())
            pontuacao.close()
        # Abre e imprime o arquivo do criador com minhas redes sociais.
        elif opc == 4:
            credito = open('docs/creditos.txt', 'r', encoding='utf-8')
            print(credito.read())
            credito.close()
        # Fecha o programa.
        elif opc == 5:
            break
    print(f'Que pena que voce ja vai'
          f',bem ate mais!!')


main()
