
new_v = 3
new_nome = ''
nome = new_nome


def opcoes():
    global new_v, new_nome
    while True:
        print('[1] Mudar nome\n'
              '[2] Alterar vidas\n'
              '[3] Voltar\n')
        resp = int(input('Escola a opção: '))
        while resp not in [1, 2, 3]:
            resp = int(input('Escolha uma opção valida: '))
        if resp == 1:
            new_nome = str(input('Digite o seu novo nome: '))
        elif resp == 2:
            new_v = int(input('Quantas vidas voce deseja ter agora? '))
        elif resp == 3:
            break

def jogo():
    from random import choice
    vidas = new_v
    while vidas > 0:
        print(f'Voce tem {vidas} vidas')
        print('[1] Pedra\n'
              '[2] Papel\n'
              '[3] Tesoura\n'
              '[999] Sair')
        jogador = int(input('Escolha sua opção: '))

        escolhas = [1, 2, 3, 999]

        while jogador not in escolhas:
            print('Opção errada, tente escolher uma dessas opções: ')
            jogador = int(input('Sua escolha: '))

        pc = choice(escolhas)

        # Caso de empate
        if jogador == pc:
            if jogador == 1:
                print('Ambus escolheram pedra')
            elif jogador == 2:
                print('Ambus escolheram papel')
            else:
                print('Ambus escolheram tesoura')
                print('Empate!')
                status = 'empate'

        # Caso o jogador perca ua vida
        elif jogador == 1 and pc == 2 or jogador == 2 and pc == 3 or jogador == 3 and pc == 1:
            vidas -= 1
            if jogador == 1:
                print('O jogador escolheu pedra')
            elif jogador == 2:
                print('O jogador escolheu papel')
            elif jogador == 3:
                print('O jogador escolheu tesoura')
            if pc == 1:
                print('O pc escolheu pedra')
            elif pc == 2:
                print('O pc escolheu papel')
            else:
                print('O pc escolheu tesoura')
            print('Voce perdeu uma vida!')

        # Caso o jogador ganhe
        elif jogador == 1 and pc == 3 or jogador == 2 and pc == 1 or jogador == 3 and pc == 2:
            if jogador == 1:
                print('O jogador escolheu pedra')
            elif jogador == 2:
                print('O jogador escolheu papel')
            elif jogador == 3:
                print('O jogador escolheu tesoura')
            if pc == 1:
                print('O pc escolheu pedra')
            elif pc == 2:
                print('O pc escolheu papel')
            else:
                print('O pc escolheu tesoura')
            print('Voce ganhou!')

        elif jogador == 999:
            break
    print('Cabou o jogo suas vidas acabaram')


def menu():
    global nome
    print('BEM VINDO AO JOGO PEDRA PAPEL TESOURA!!!')
    nome = new_nome
    nome = str(input('Digite o seu nome jogador: '))
    while True:
        print('[1] Jogar\n'
              '[2] Como Jogar\n'
              '[3] Opções\n'
              '[4] Creditos\n'
              '[5] Sair')
        opc = int(input(f'{nome} escolha a opção: '))
        while opc not in [1, 2, 3, 4, 5]:
            opc = int(input(f'{nome} escolha uma opção valida: '))
        if opc == 1:
            jogo()
        elif opc == 2:
            print('Regras')
        elif opc == 3:
            opcoes()
        elif opc == 4:
            print('Creditos')
        elif opc == 5:
            break
    print('Adeus ate a proxima')


menu()
