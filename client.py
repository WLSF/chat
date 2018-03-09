import socket, select, string, sys


def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()

def main_loop():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect(('0.0.0.0', 8000))
    except:
        print('Unable to connect')
        sys.exit()

    print('Connected to remote host. Start sending messages')
    prompt()

    while 1:
        socket_list = [sys.stdin, s]

        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print('\nDisconnected from chat server')
                    sys.exit()
                else:
                    sys.stdout.write(data.decode())
                    prompt()

            else:
                msg = sys.stdin.readline()
                s.send(msg.encode())
                prompt()