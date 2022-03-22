import  time
from time import sleep
import socket
import threading as td
import sys

ADMIN_PORT = 9999
broadcast = '<broadcast>' # ใช้สำหรับติดต่อไปยังผู้ใช้ทุกคนใน server
my_ip = 'localhost'
PORT = 5050
PORT2 = 5000
BUFFSIZE = 10100

clientlist = [] # เก็บผู้ใช้ที่ connect เข้ามา

print(type(clientlist))

def sende_to_all():
    msg = 'Hello from addmin'.encode("utf-8")
    dest = (broadcast,PORT2)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    for i in range(5):
        s.sendto(msg, dest)
    print('='*15+' Sending '+'='*15)

def client_handler(client,addr):# รองรับผู้ใช้หลายคน
    while True:
        try:
            data = client.recv(BUFFSIZE).decode('utf-8')
        except:
            clientlist.remove(client)
            break
        #exit funtion
        if(not data) or (data == 'q'):
            clientlist.remove(client)
            print('USER OUT : ',addr)
            break
        masage = str(addr) + ' >>> ' + data
        print('Masage from User : ',masage)
        client.send(("we recive "+data).encode('utf-8'))
        client.send(("we recive2 "+data).encode('utf-8'))
        ############################################################################
        ###         ส่งข้อความหาผู้ใช้หลายครั้งได้โดยไม่ต้องรอผู้ใช้ตอบกลับ                  ###
        # for i in range(5):
        #     print(i)
        #     client.send("Masage from server: testing{}".format(i).encode('utf-8'))
        ############################################################################

    # user exit
    client.close()
    sys.exit()

def client_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((my_ip, PORT))
    server.listen(5)

    while True:
        print('Waiting for client... PORT for Client: ',PORT)
        client, addr = server.accept()
        clientlist.append(client)
        print('connet form: ',addr)
        ##########################
        # เรียกใช้ฟังชั่น login ตรงนี้  #
        ##########################
        task = td.Thread(target=client_handler,args=(client,addr))
        task.start()
 
def addmin_server():
    server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server2.bind((my_ip, ADMIN_PORT))
    server2.listen(1)

    print('Waiting for Addmin... PORT for Admin: ',ADMIN_PORT)
    admin, addr = server2.accept()
      ##########################
     # เรียกใช้ฟังชั่น login ตรงนี้  #
    ##########################
    print('Addmin is connect form: ',addr)
    while True:

       ####################################
        # เมื่อมีผู้ใช้เชื่อมต่อเข้ามาครบ 3 เครื่องและ Admin connect เข้ามาจะส่ง message ไปยังทุกเครื่อง ทดสอบให้ดูเฉยๆ
        n = 0
        # สร้างเงื่อนไขในการ run function sende_to_all
        for i in clientlist:
            n = n+1
            if n==3:
                sende_to_all()
                # task1 = td.Thread(target=sende_to_all)
                # task1.start()
        ######################################
        try:
            data = admin.recv(BUFFSIZE).decode('utf-8')
        except:
            break
        #exit funtion
        if(not data) or (data == 'q'):
            print('USER OUT : ',addr)
            break
        masage =  'Admin >>> ' + data
        print('Masage from User : ',masage)
        admin.send(("we recive "+data).encode('utf-8'))
        admin.send(("we recive2 "+data).encode('utf-8'))
    admin.close()
    sys.exit()
    #############
############# รัน server รัน Code ที่นี่ ##################
if __name__ == '__main__':
    task1 = td.Thread(target=client_server)
    task1.start()
    time.sleep(0.25) # รอให้เซิร์ฟเวอร์แรกรันเสร็จก่อน
    task2 = td.Thread(target=addmin_server)
    task2.start()