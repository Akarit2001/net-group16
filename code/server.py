import  time
import socket
import threading as td

broadcast_ip = '127.255.255.255' # ใช้สำหรับติดต่อไปยังผู้ใช้ทุกคนใน localhost
ADMIN_PORT = 9999

my_ip = 'localhost'
PORT = 5050
BUFFSIZE = 4096




clientlist = [] # เก็บผู้ใช้ที่ connect เข้ามา

print(type(clientlist))
def sendmassageall():
    clientlist[0].send("Halo from admin".encode('utf-8'))

    
def client_handler(client,addr):
    while True:
        try:
            data = client.recv(BUFFSIZE).decode('utf-8')
        except:
            clientlist.remove(client)
            break
        #exit funtion
        if(not data) or (data == 'q'):
            clientlist.remove(client)
            print('OUT : ',client)
            break
        masage = str(addr) + ' >>> ' + data
        print('Masage from User : ',masage)
        if data == 'admin':
            client.send("hello admin".encode('utf-8'))

    # user exit
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((my_ip, PORT))
server.listen(5)

while True:
    print('Waiting for client...')
    client, addr = server.accept()
    clientlist.append(client)
    print('All CLIENTS : ',clientlist)

    task = td.Thread(target=client_handler,args=(client,addr))
    task.start()
    
