import socket


serversocket = []
host = "0.0.0.0"
port = 8000

def main_loop():
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((host, port))
        serversocket.listen(5)
        print('server started and listening')
        while 1:
            clientsocket, address = serversocket.accept()
            msg = clientsocket.recv(1024).decode()
            print('Client sent:', msg)
            msg = input('Say something: ')
            clientsocket.send('Server response: {}\n'.format(msg).encode())
    except:
        serversocket.close()