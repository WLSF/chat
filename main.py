from server import main_loop as server_side
from client import main_loop as client_side

if __name__ == '__main__':
    option = int(input('1. Chat client\n2. Server client\nR: '))
    if option == 1:
        client_side()
    else:
        server_side()
