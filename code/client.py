import socket
import threading as td
import sys
import struct
import time
# from pysql import mysqls as ms

multicast_Address = '224.1.1.1' # ใช้สำหรับติดต่อไปยังผู้ใช้ทุกคนใน localhost

server_ip = 'localhost'
port = 5050
port2 = 5000
BUFFSIZE = 4096

def listenmsg():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(('',port2))
    mreq = struct.pack("4sl",socket.inet_aton(multicast_Address),socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    while  True:
        print('\nyou got message: ',sock.recv(BUFFSIZE).decode('utf8'))

def server_handler(client):
    while True:
        try:
            data = client.recv(BUFFSIZE).decode('utf8')
        except:
            print('ERROR! connect failed.')
            break
        #exit funtion
        if(not data) or (data == 'q'):
            print("----------- exit -----------")
            # print('OUT : ',client)
            break
        print("data from server",data)
        # print(data.decode('utf-8'))
    # user exit
    client.close()
    sys.exit()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    client.connect((server_ip,port))
except:
    print('ERROR! can not connect to server.')
    sys.exit()

# runthread
task = td.Thread(target=server_handler,args=(client,))
task.start()

# รอข้อรับความแบบกระจายทุกคนที่เชื่อมต่อจะได้รับเมื่อเชื่อมต่ออยู่
task2 = td.Thread(target=listenmsg)
task2.start()
# input from user.
while True:
    msg = input('Message: ')
    if msg == '':
        msg = " "
    client.send(msg.encode('utf-8'))
    time.sleep(0.5)
    
    if msg == 'q':
        break
client.close()
sys.exit()