import socket
import threading as td
import sys
import struct
import time

server_ip = 'localhost'
ADMIN_PORT = 9999
BUFFSIZE = 10100

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
            break
        print("data from server",data)
        
    # user exit
    client.close()
    sys.exit()

def admin_connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        client.connect((server_ip,ADMIN_PORT))
    except:
        print('ERROR! can not connect to server.')
        sys.exit()
    # runthread
    task = td.Thread(target=server_handler,args=(client,))
    task.start()

    # input from user.
    while True:
        msg = input('Admin Message: ')
        if msg == '':
            msg = " "
        client.send(msg.encode('utf-8'))
        time.sleep(0.25)
        if msg == 'q':
            break
    client.close()
    sys.exit()
#############################################################
############# รัน admin_connect_to_server ที่นี่ #################
#############################################################
if __name__ == '__main__':
    admin_connect_to_server()
