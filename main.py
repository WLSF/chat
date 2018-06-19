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

if __name__ == '__main__':
    try:
        server_side()

        ip, port = show_menu()
        client_side(ip, port)
    except:
        pass