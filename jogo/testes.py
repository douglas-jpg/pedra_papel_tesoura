import random

# Função que recebe a jogada do jogador
def jogada_jogador():
    jogada = input("Escolha a sua jogada (pedra, papel ou tesoura): ")
    while jogada not in ['pedra', 'papel', 'tesoura']:
        jogada = input("Jogada inválida. Escolha novamente (pedra, papel ou tesoura): ")
    if jogada == 'pedra':
        return 0
    elif jogada == 'papel':
        return 1
    elif jogada == 'tesoura':
        return 2

# Função que realiza a jogada do computador
def jogada_computador():
    return random.randint(0, 2)

# Função que verifica o resultado da partida
def verificar_resultado(jogada_jogador, jogada_computador):
    if jogada_jogador == jogada_computador:
        return 0
    elif jogada_jogador == 0 and jogada_computador == 2:
        return 1
    elif jogada_jogador == 1 and jogada_computador == 0:
        return 1
    elif jogada_jogador == 2 and jogada_computador == 1:
        return 1
    else:
        return 2

# Função principal do jogo
def jogar():
    print("Bem-vindo ao jogo de Pedra-Papel-Tesoura!")
    vidas = 3
    while vidas > 0:
        print(f"Você tem {vidas} vidas.")
        jogada_j = jogada_jogador()
        jogada_c = jogada_computador()
        resultado = verificar_resultado(jogada_j, jogada_c)
        if resultado == 0:
            print("Empate!")
        elif resultado == 1:
            print("Você venceu!")
        else:
            print("Você perdeu!")
            vidas -= 1
        if vidas == 0:
            print("Fim de jogo. Você perdeu todas as vidas.")
            break
        jogar_novamente = input("Deseja jogar novamente? (sim ou nao) ")
        if jogar_novamente.lower() != 'sim':
            break

# Execução do jogo
jogar()
