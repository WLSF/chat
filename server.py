from models import Server


def main_loop(ip = '0.0.0.0', port = 8000):
    server = Server(ip, port)
    try:

        server.listen()
        print('server started and listening')

        def create_thread(server):
            try:
                while True:
                    clientsocket, address = server.accept()
                    msg = clientsocket.recv(1024).decode()
                    print('<{}>: {}'.format(ip, msg))
            except:
                print('\nCTRL+C')

        from threading import Thread
        server_thread = Thread(target=create_thread, args=(server, ))
        server_thread.start()

    except:
        server.close_socket()