import socket


program = '''
import os
print(os.environ)
'''

s = socket.create_connection(('127.0.0.1', 1024))
s.sendall(program.encode('utf-8'))
s.close()
