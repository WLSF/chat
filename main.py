# -*- coding: utf-8 -*-

from server import main_loop as server_side
from client import main_loop as client_side
from errors import NumberRequiredException, InvalidCodeException


def show_menu():
    try:
        return ((input('1. IP:\n ')), int(input('2. PORT:\n ')))
    except ValueError:
        # TODO: 00
        NumberRequiredException()


def switch(value: int):
    if value == 1:
        server_side()

    elif value == 2:
        client_side()

    else:
        # TODO: 01
        InvalidCodeException()

if __name__ == '__main__':
    ip, port = show_menu()
    server_side(ip, port)

    ip, port = show_menu()
    client_side(ip, port)

'''

Não vai mais existir Client e nem Server pelo menos para o usuário final, vai ser transparente como se fosse 
ambos em um produto. A classe Client e Server deverão ser chamados respectivamente quando o opt for escolhido,
iniciando a conexão e enviando as mensagens.

Toda vez que o produto for aberto, ele iniciará um Server para ficar ouvindo a determinada porta.
Se por ventura o usuário final do produto escolher enviar mensagens para algum destino especifico, então a classe
Client deverá ser instanciada para que criar um socket com o Server de destino. 

'''