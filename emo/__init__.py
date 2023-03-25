import emoji


def pedra():
    """
    Cria o emoji de pedra
    :return: emoji de pedra U+1FAA8
    """
    return emoji.emojize(':rock:')


def tesoura():
    """
    Cria o emoji de tesoura
    :return: emoji de tesoura U+FE0F
    """
    return emoji.emojize(':scissors:')


def papel():
    """
    Cria o emoji de papel
    :return: emojis de papel U+1F4DC
    """
    return emoji.emojize(':scroll:')


def vida(n=3):
    """
    Cria a quantidade de vidas para o jogo
    inicialmente 3 vidas
    :param n: quantidade de corações
    :return: emoji de coração U+FE0F
    """
    for c in range(n):
        print(emoji.emojize(':red_heart:'), end='')
    return ''
