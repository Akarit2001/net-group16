import socket
import threading as td
from pysql import mysqls as ms
# server_ip = '193.168.88.129'
# server_ip = '192.168.88.130'
# server_ip = '10.224.109.10'
ms.test()
pp = ms.Person('AAA',50)
pp.myfunc()
server_ip = 'localhost'
port = 5050

while True:
    data = input('Sen Message : ')
    # server = socket.socket()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.connect((server_ip, port))
    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print('Data from Server: ',data_server)
    server.close()
