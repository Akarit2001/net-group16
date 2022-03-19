# import pymysql
import mysql.connector
import random
import datetime


# เตือนการใช้ object เดียวในการ aad ค่าในตารางจะทำให้ id มันซ้ำกัน แต่จะใช้ในการ genbill ได้
class MySql:
    def __init__(self):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="foodservice"
        )
        self.uid = str({0: 11}).format(
            random.randint(1, 9999999999)).replace(" ", "0")
        self.fid = str({0: 6}).format(
            random.randint(1, 999999)).replace(" ", "0")
        self.bid = str({0: 6}).format(
            random.randint(1, 999999)).replace(" ", "0")
    # for client and admin
    def createUser(self, username, password, address):
        mycursor = self.__mydb.cursor()
        uid = self.uid
        my_str = "INSERT INTO User VALUES('"+self.uid + \
            "','"+username+"','"+password+"','"+address+"');"
        # chek user
        b = bool(self.getUser(username=username))
        if(not b):
            mycursor.execute(my_str)
            self.__mydb.commit()
            print("UserID: {} name: {} created.".format(self.uid, username))
        elif(b):
            print("User name: {} has been used.".format(username))

    # for admin only
    def showAllUser(self):
        mycursor = self.__mydb.cursor()
        my_str = """select * from user;"""
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("UID: {} UName: {} Password: {} Address: {}".format(
                x[0], x[1], x[2], x[3]))

    def showUser(self, UIDs="", username=""):
        mycursor = self.__mydb.cursor()
        my_str = ""
        uid = "select * from user where uid = '{}';".format(UIDs)
        name = "select * from user where UName = '{}';".format(username)
        seall = "select * from user where uid = '{}' and UName = '{}';".format(
            UIDs, username)
        if UIDs == "":
            my_str = name
        elif username == "":
            my_str = uid
        else:
            my_str = seall
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        if(not myresult):
            print("NO data found.")
        for x in myresult:
            print("UID: {} UName: {} Password: {} Address: {}".format(
                x[0], x[1], x[2], x[3]))

    def getUser(self, UIDs="", username=""):
        mycursor = self.__mydb.cursor()
        my_str = ""
        uid = "select * from user where uid = '{}';".format(UIDs)
        name = "select * from user where UName = '{}';".format(username)
        seall = "select * from user where uid = '{}' and UName = '{}';".format(
            UIDs, username)
        if UIDs == "":
            my_str = name
        elif username == "":
            my_str = uid
        else:
            my_str = seall
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        return myresult #returntype ->> list<tuple>

    def dropUser(self, UIDs, username):
        mycursor = self.__mydb.cursor()
        my_str = "DELETE FROM user WHERE uid = '{}' and UName = '{}'".format(
            UIDs, username)
        mycursor.execute(my_str)
        print('User: {} droped.'.format(username))
        self.__mydb.commit()


    # Food
    def addFoods(self,name,price):
        mycursor = self.__mydb.cursor()
        fid = self.fid
        my_str = "INSERT INTO food VALUES('{}','{}',{});".format(fid,name,price)
        # chek user
        b = bool(self.getFoods(fname=name))
        if(not b):
            # print(my_str)
            mycursor.execute(my_str)
            self.__mydb.commit()
            print("ID: {} Food: {} Price: {} was added.".format(fid, name,price))
        elif(b):
            print("There is a food with this name '{}'".format(name))

    def deleteFoods(self,fid, fname):
        mycursor = self.__mydb.cursor()
        my_str = "DELETE FROM food WHERE fid = '{}' and fname = '{}'".format(
            fid, fname)
        mycursor.execute(my_str)
        print('Food: {} droped.'.format(fname))
        self.__mydb.commit()
    def showAllFood(self):
        mycursor = self.__mydb.cursor()
        my_str = """select * from food;"""
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        for x in myresult:
            # print('tets')
            print("FID: {} Food name: {} price: {}".format(
                x[0], x[1], x[2]))

    def getFoods(self, fname):
        mycursor = self.__mydb.cursor()
        my_str = "select * from food where fname = '{}';".format(fname)
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        return myresult #returntype ->> list<tuple>

    # pirvate function
    def genBill(self,fid,uid,total):
        mycursor = self.__mydb.cursor()
        bid = self.bid
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        my_str = "INSERT INTO Bill VALUES('{}','{}','{}',{},'{}');".format(bid,uid,fid,total,date)
        mycursor.execute(my_str)
        self.__mydb.commit()
    def oder(self,fid,uid,total):
        for i in a:
          print()
        print()

# if __name__ == '__main__':
#     MySql().createUser('user1', 'user1', 'kku')
# if __name__ == '__main__':
#     print('============end============')
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="foodservice"
#     )
#     # str = """ DROP TABLE User  ;"""
#     str = """  CREATE TABLE User(
#     UID CHAR(11),
#     UName VARCHAR(40),
#     password VARCHAR(20),
#     UAddress VARCHAR(80),
#     CONSTRAINT User_PK PRIMARY KEY (UID)
#   );
#   """
#     mycursor = mydb.cursor()
#     mycursor.execute(str)
