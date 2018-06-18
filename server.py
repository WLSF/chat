from models import Server


def main_loop():
    server = Server()
    try:

        server.listen()
        print('server started and listening')

        # Not working, check this out
        def create_thread(server):
            try:
                while True:
                    print('Thread started, waiting for messages')
                    clientsocket, address = server.accept()
                    msg = clientsocket.recv(1024).decode()
                    print('Client sent: ', msg)
            except:
                print('\nCTRL+C')

        from threading import Thread
        server_thread = Thread(target=create_thread, args=(server, ))
        server_thread.start()
        print('Out thread')

    except:
        server.close_socket()

'''
clientsocket, address = server.accept()
msg = clientsocket.recv(1024).decode()
print('Client sent:', msg)
msg = input('Say something: ')
clientsocket.send('Server response: {}\n'.format(msg).encode())
'''