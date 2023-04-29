import emoji
from time import sleep


def pedra():
    """
    Cria o emoji de pedra
    """
    return emoji.emojize(':rock:')


def tesoura():
    """
    Cria o emoji de tesoura
    """
    return emoji.emojize(':scissors:')


def papel():
    """
    Cria o emoji de papel
    """
    return emoji.emojize(':scroll:')


def vida(n=3):
    """
    Cria a quantidade de vidas para o jogo inicialmente 3 vidas.
    :param n: Quantidade de corações
    :return: emoji de coração U+FE0F
    """
    print(n*f"{emoji.emojize(':red_heart:')}")
    return ''


def sair():
    """
    Cria o emoji de xis vermelho
    """
    return emoji.emojize(':cross_mark:')


def empate_pedra():
    print(pedra(), end='')
    sleep(1)
    print(' x ', end='')
    sleep(1)
    print(pedra())
    return ''


def empate_papel():
    print(papel(), end='')
    sleep(1)
    print(' x ', end='')
    sleep(1)
    print(papel())
    return ''

def empate_tesoura():
    print(tesoura(), end='')
    sleep(1)
    print(' x ', end='')
    sleep(1)
    print(tesoura())
    return ''

