import  time
from time import sleep
import socket
import threading as td

multicast_Address = '224.1.1.1' # ใช้สำหรับติดต่อไปยังผู้ใช้ทุกคนใน server
# ADMIN_PORT = 9999

my_ip = 'localhost'
PORT = 5050
BUFFSIZE = 4096




clientlist = [] # เก็บผู้ใช้ที่ connect เข้ามา


print(type(clientlist))

def sende_to_all():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 5)
    my_str = "\nthere have 3 clients connected to this server".encode('utf-8')
    sock.sendto(my_str, (multicast_Address,5000))
    print('xxxxxxxxxxxxx sending. xxxxxxxxxxxxx')
    
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
        ############################################################################
        ###         ส่งข้อความหาผู้ใช้หลายครั้งได้โดยไม่ต้องรอผู้ใช้ตอบกลับ                  ###
        for i in range(5):
            print(i)
            client.send("Masage from server: testing{}".format(i).encode('utf-8'))
        ############################################################################

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
    ####################################
    # เมื่อมีผู้ใช้เชื่อมต่อเข้ามาครบ 3 เครื่องจะส่ง message ไปยังทุกเครื่อง
    n = 0
    # สร้างเงื่อนไขในการ run thread
    for i in clientlist:
        n = n+1
        if n==3:
            task1 = td.Thread(target=sende_to_all)
            task1.start()
        # print()
    ######################################
