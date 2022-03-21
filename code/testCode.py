from pysql import mysqls as ms
import datetime
#####################################################################################################
## การจะใช้คำสั่งใน mysqls ได้ต้องสร้าง database ให้เหมือนในโปรเจคนี้ก่อน ตั้งชื่อ database ว่า foodservice และมี   ##
## table เหมือนใน file net-group16\code\pysql\create_table_and_table_struct\createTable.py         ##
####################################################################################################
# ms.MySql().createUser(username='user234',password='user23', address='KKU')
# print('--------------------------------------')
# ms.MySql().showAllUser()
# print('--------------------------------------')
# ms.MySql().showUser(UIDs="00000000000",username='admin')
# print('--------------------------------------')
# # ms.MySql().dropUser(UIDs='08281117706', username='user2')
# print('--------------------------------------')
ms.MySql().showAllUser()

# ss = ms.MySql().getUser(username='user23s')
# # print(ss,type(ss), not ss)
# for s in ss:
#     print(s,type(s))
sql = ms.MySql()
# print('--------------------------------------------------')
# ms.MySql().addFoods("somtum", 50)
# ms.MySql().addFoods("pingkai", 60)
# ms.MySql().addFoods("kao", 20)
# ms.MySql().addFoods("ping moo", 90)
print('--------------------------------------------------')
sql.showAllFood()
print(type(sql.getFoods('somtum')[0]))
# ms.MySql().deleteFoods('057901', 'kao')

date = datetime.datetime.now()
print(date.strftime("%Y-%m-%d"))

# user1 = ms.MySql()
# for i in range(3):
#     fids = str(input())
#     totals = int(input())
#     user1.genBill(fids, '07055401949', totals)

ms.MySql().getbillUserDetail(userId="07055401949")
print("-------------------------------------------")
ms.MySql().showAllBill()
