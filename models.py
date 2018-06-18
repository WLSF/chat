import socket, select, string, sys


class Client:
    _socket = []
    def connect(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(2)

        try:
            self._socket.connect(('0.0.0.0', 8000))
        except:
            print('Unable to connect')
            exit()


class Server:
    _server_socket = []
    _host = "0.0.0.0"
    _port = 8000

    def listen(self):
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind((self._host, self._port))
        self._server_socket.listen(5)

    def get_socket(self):
        return self._server_socket

    def close_socket(self):
        self._server_socket.close()

    def accept(self):
        return self._server_socket.accept()