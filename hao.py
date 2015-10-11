import socket
from queue import Queue
import threading


instructions = Queue()
debug = False


def get_socket(seed):
    "Get socket to listen at"
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    while True:
        try:
            sock.bind(('0.0.0.0', seed))
        except:
            seed += 1
        else:
            break
    sock.listen(1)  # to the first that connects
    com, addr = sock.accept()
    sock.close()
    com.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    return com, addr


def listen(seed=1024):
    global instructions, debug
    try:
        while True:
            com, addr = get_socket(seed)
            try:
                data = com.recv(2 ** 10)  # BUFFER of 1024
                inst = data.decode()
            except Exception as e:
                if debug:
                    raise e
            else:
                instructions.put(inst)
    except Exception as e:
        if debug:
            raise e


def execute():
    global instructions, debug
    try:
        while True:
            try:
                code = instructions.get()
                exec(code)
            except Exception as e:
                if debug:
                    raise e
    except Exception as e:
        if debug:
            raise e


if __name__ == '__main__':
    li = threading.Thread(target=listen)
    li.start()
    execute()
