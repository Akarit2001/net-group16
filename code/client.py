import socket
import threading as td
import sys
# from pysql import mysqls as ms

server_ip = 'localhost'
port = 5050
BUFFSIZE = 4096



def server_handler(client):
    while True:
        try:
            data = client.recv(BUFFSIZE)
        except:
            print('ERROR')
            break
        #exit funtion
        if(not data) or (data.decode('utf-8') == 'q'):
            print('OUT : ',client)
            break

        print('Masage from User : ',data.decode('utf-8'))
    # user exit
    client.close()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    client.connect((server_ip,port))
except:
    print('ERROR!')
    sys.exit()

task = td.Thread(target=server_handler,args=(client,))
task.start()
while True:
    msg = input('Message: ')
    client.sendall(msg.encode('utf-8'))
    if msg == 'q' or msg == '':
        break
cilent.close()