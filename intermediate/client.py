import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.137.1',55555))

message = s.recv(1024)
s.close()
print(message.decode())