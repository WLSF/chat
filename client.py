from models import Client

def main_loop(ip, port):
    try:
        print('Write your first message: ')
        while 1:
            client = Client(ip, port)
            client.connect()
            msg = input()
            client.send_message(msg)
    except:
        pass