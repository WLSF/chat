from models import Client

def main_loop(ip, port):
    while 1:
        client = Client(ip, port)
        client.connect()
        msg = input('<You> ')
        client.send_message(msg)