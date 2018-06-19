# -*- coding: utf-8 -*-

from server import main_loop as server_side
from client import main_loop as client_side
from errors import NumberRequiredException, InvalidCodeException


def show_menu():
    try:
        str = input('Address: ')
        idx = str.index(':')
        return ((str[0:idx]), int(str[idx+1:]))
    except:
        pass


def switch(value: int):
    if value == 1:
        server_side()

    elif value == 2:
        client_side()

    else:
        # TODO: 01
        InvalidCodeException()

if __name__ == '__main__':
    try:
        server_side()

        ip, port = show_menu()
        client_side(ip, port)
    except:
        pass


'''

Não vai mais existir Client e nem Server pelo menos para o usuário final, vai ser transparente como se fosse 
ambos em um produto. A classe Client e Server deverão ser chamados respectivamente quando o opt for escolhido,
iniciando a conexão e enviando as mensagens.

Toda vez que o produto for aberto, ele iniciará um Server para ficar ouvindo a determinada porta.
Se por ventura o usuário final do produto escolher enviar mensagens para algum destino especifico, então a classe
Client deverá ser instanciada para que criar um socket com o Server de destino. 

'''