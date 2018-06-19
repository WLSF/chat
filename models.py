import socket, select, string, sys


class Client:
    _socket = []
    _host = "0.0.0.0"
    _port = 8000

    def __init__(self, ip, port):
        if not ip and not port:
            pass

        self._host = ip
        self._port = port

    def connect(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(2)

        try:
            self._socket.connect((self._host, self._port))
        except:
            print('Unable to connect')
            exit()

    def send_message(self, message):
        self._socket.send(message.encode())


class Server:
    _server_socket = []
    _host = "0.0.0.0"
    _port = 8000

    def __init__(self, ip, port):
        if not ip and not port:
            pass

        self._host = ip
        self._port = port

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