import socket
cs=socket.socket()
cs.connect(('localhost',9600))
cs.send(bytes('cloning', 'utf-8'))
print(cs.recv(1024).decode())