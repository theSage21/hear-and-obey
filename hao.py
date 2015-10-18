import socket


debug = False  # Keep false when deploying
seed_port = 5995


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


def listen(seed=seed_port):
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
                execute(inst)
            finally:
                com.close()
    except Exception as e:
        if debug:
            raise e


def execute(code):
    global debug
    try:
        exec(code)
    except Exception as e:
        if debug:
            raise e


if __name__ == '__main__':
    listen()
