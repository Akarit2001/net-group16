import  time
import socket
import threading as td
# my_ip = '192.168.88.1'
# my_ip = '192.168.88.130'
my_ip = 'localhost'
PORT = 5050
BUFFSIZE = 4096
clientlist = [] # เก็บผู้ใช้ที่ connect เข้ามา
print(type(clientlist))
def client_handler(client,addr):
    while True:
        try:
            data = client.recv(BUFFSIZE).decode('utf-8')
        except:
            clientlist.remove(client)
            break
        #exit funtion
        if(not data) or (data.decode('utf-8') == 'q'):
            clientlist.remove(client)
            print('OUT : ',client)
            break
        masage = str(addr) + ' >>> ' + data
        prit('Masage from User : ',masage)

        sendmassageall()

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
    
def sendmassageall():
    msg = "สวัสดีจาก Admin".encode('utf-8')
    for i in clientlist:
        i.sendall(msg)