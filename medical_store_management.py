import mysql.connector as sqltor
mydb=sqltor.connect(host="localhost",user="root",passwd="1234",database="medical")
if mydb.is_connected():
    print("***********MYSQL IS CONNECTED SUCCEFULLY************")
else:
    print("mysql is not connected successfully")
mycon=mydb.cursor()


def menu():
    print("***********WELCOME TO STORE MANAGEMENT SYSTEM*********")
    print("******************************************************")
    print("********************MEDICAL STORE***********************")
    print()
    print("********************************************************")
    print("1.ABOUT THE PROJECT")
    print("2.DISPLAY LIST OF ALL THE STOCK AVAILABLE IN THE STORE")
    print("3.ADD THE PURCHASED ITEM IN STOCK TABLE")
    print("4.UPDATE THE PRICE OF MEDICINES")
    print("5.DELETE THE MEDICINE DETAILS")
    print("6.ACCEPT CUSTOMER ORDER AND SHOW BILL")
    print("7.SHOW DETAILS OF ALL SALES DONE FROM TABLE BILL")
    print("8.ENTER ALL CUSTOMER ORDER AND MAINTAIN RECORD")
    print("9.ENTER NEW STAFF DETAILS IN STAFF TABLE")
    print("10.SHOW RECORDS OF STAFF TABLE")
    print("11.DELETE STAFF DETAILS FROM STAFF TABLE")
    print("12.UPDATE STAFF TABLE")
    print("13 WANT TO EXIT FROM PROGRAM")
    print("*******************************************************")
def about():
    print("WELCOME TO STORE MANAGEMENT SYSTEM,It has 13 choices and 3 tables named as stock,bill and staff")
def showlist():
    print("display the list of MEDICINE available ")
    print()
    mycon=mydb.cursor()
    mysq=mycon.execute("select * from stock")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
def addstock():
    print("medicines already in stock")
    print()
    mysq=mycon.execute("select * from stock")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
    L=[]
    mcode=input("Enter medicine code:")
    L.append(mcode)
    mname=input("enter name of the medicine")
    L.append(mname)
    dateofexp=input("enter date of expiry of medicine")
    L.append(dateofexp)
    quan=int(input("enter quantity of medicine:"))
    L.append(quan)
    price=int(input("enter the price of medicine:"))
    L.append(price)
    stock=(L)
    sql="insert into stock(mcode,mname,dateofexp,quan,price)values(%s,%s,%s,%s,%s)"
    mysq=mycon.execute(sql,stock)
    mydb.commit()
    print("RECORD OF MEDICINE INSERTED SUCCESSFULLY")
    mysq=mycon.execute("select * from stock")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)



def updatestock():
    print("change the price of medicines")
    print("old prices")
    mysq=mycon.execute("select * from stock")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
    updateprice=int(input("enter the number to set the price of medicine:"))
    updatecode=int(input("enter the mcode of medicine whose price you want to increase:"))
    mysq=mycon.execute("update stock set price={}".format(updateprice)," where mcode={}".format(updatecode))
    mydb.commit()
    print("PRICE INCREASED")
    mysq=mycon.execute("select * from stock")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)


def deletestock():
    print("BEFORE ANY CHANGES IN TABLE STOCK")
    mysq=mycon.execute("select * from stock")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
    deletecode=int(input("enter the mcode whose record you want to delete:"))
    mysq="delete from stock where mcode={}".format(deletecode)
    mycon.execute(mysq,deletecode)
    mydb.commit()
    print("RECORD DELETED")
    mysq=mycon.execute("select * from stock")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)


def custorder():
    print("Medicine codes ,Name and Price of each medicine is shown below:")
    print()
    mysq=mycon.execute("select * from stock")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
    print()
    print()
    print()
    print()
    print()
    x=int(input("ENTER MEDICINE CODE YOU WANT TO PURCHASE:"))
    n=int(input("ENTER THE QUANTITY OF MEDICINE:"))
    if (x==101):
          print()
          print("YOU HAVE BOUGHT DOLO TABLET")
          print()
          print("YOU HAVE TO PAY RS 150 FOR EACH STRIP")
          s=n*150
          print("YOU HAVE TO PAY RS ",s,"FOR",n,"STRIPS")
    elif(x==102):
        print()
        print("YOU HAVE BOUGHT CIPLOX")
        print()
        print("YOU HAVE TO PAY RS 120 FOR EACH STRIP")
        s=n*120
        print("YOU HAVE TO PAY RS",s,"FOR",n,"STRIPS")
    elif(x==103):
        print()
        print("YOU HAVE BOUGHT A SANITIZER")
        print()
        print("YOU HAVE TO PAY RS 220 FOR SANITIZER OF 500ML BOTTLE")
        print()
        s=n*220
        print("YOU HAVE TO PAY RS",s,"for",n,"BOTTLE OF SANITIZERS")
    elif(x==104):
        print()
        print("YOU HAVE BOUGHT LIFEBOY SOAP")
        print()
        print("YOU HAVE TO PAY RS 60 PER PIECE OF SOAP")
        s=n*60
        print("YOU HAVE TO PAY RS",s,"FOR",n,"PIECES OF SOAP")
    elif(x==105):
        print()
        print("YOU HAVE BOUGHT A SURGICAL MASK")
        print()
        print("YOU HAVE TO PAY RS 20 PER MASK")
        s=n*20
        print("YOU HAVE TO PAY RS",s,"FOR",n,"PIECES OF SURGICAL MASK")
    elif(x==106):
        print()
        print("YOU HAVE BOUGHT A DETTOL BOTTLE OF 200ML")
        print("YOU HAVE TO PAY RS 90 FOR DETTOL")
        s=n*90
        print("YOU HAVE TO PAY RS",s,"FOR",n,"BOTTLES OF DETTOL")
    elif(x==107):
        print()
        print("YOU HAVE TO BOUGHT VICS OF 50MG")
        print("YOU HAVE TO PAY RS 50 FOR 50 MG OF VICS")
        s=n*50
        print("YOU HAVE TO PAY RS",s,"for",n,"PIECES OF VICS")
    else:
        print("PLEASE ENTER CORRECT MEDICINE CODE")


def billrecords():
    print("contact number of customer ,medicine purchased,quantity and its price")
    print()
    mysq=mycon.execute("select * from bill")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)


def recordorder():
    print("list and prices of medicines")
    print()
    mysq=mycon.execute("select * from stock")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
    print()
    print("INSERT INTO BILL RECORDS NEW SALE")
    mydb.cursor()
    L=[]
    mobile=int(input("enter the customer mobile number"))
    L.append(mobile)
    mcode=int(input("enter the item code that customer has purchased"))
    L.append(mcode)
    mname=input("enter name of the item customer has purchased")
    L.append(mname)
    quan=int(input("enter the quantity of the item customer has purchased"))
    L.append(quan)
    price=int(input("enter the price of the item customer has purchased"))
    L.append(price)
    sql="insert into bill(mobile,mcode,mname,quan,price)values(%s,%s,%s,%s,%s)"
    billrec=L
    mysq=mycon.execute(sql,billrec)
    mydb.commit()
    print("RECORD INSERTED SUCCESSFULLY")
    mysq=mycon.execute("select * from bill")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)


def insertstaff():
    print("OLD STAFF DETAILS")
    mysq=mycon.execute("select * from staff")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
    print()
    print()
    print("ENTER NEW STAFF INFORMATION:-")
    print()
    L=[]
    sid=int(input("enter the staff id:"))
    L.append(sid)
    name=input("enter the name of the staff:")
    L.append(name)
    age=int(input("enter the age of the staff:"))
    L.append(age)
    profile=input("enter work profile of staff:")
    L.append(profile)
    mobile=int(input("enter the mobile number of staff:"))
    L.append(mobile)
    staff=L
    sq=("insert into staff(sid,name,age,profile,mobile)values(%s,%s,%s,%s,%s)")
    mysq=mycon.execute(sq,staff)
    print(" RECORD SUCCESSFULLY REGISTERED")
    mysq=mycon.execute("select * from staff")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
    
def showstaff():
    print("ALL RECORD OF STAFF DETAILS")
    print()
    mysq=mycon.execute("select * from staff")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
    print()

def deletestaff():
    mysq=mycon.execute("select * from staff")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
    print("RECORD OF STAFF TABLE")
    deletesid=int(input("enter the id of staff whose record you want to delete:"))
    mysq=("delete from staff where sid={}".format(deletesid))
    mycon.execute(mysq)
    mydb.commit()
    print("RECORD DELETED")
    mysq=mycon.execute("select * from staff")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)


def updatestaff():
    mysq=mycon.execute("select * from staff")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)
    updatemobileno=int(input("enter the 7 digit mobile no to update:"))
    updatename=input("enter the name whose mobile no you have to update:")
    mysq=mycon.execute("update staff set mobile={}".format(updatemobileno)," where name={}".format(updatename))
    mydb.commit()
    print("RECORD UPDATED")
    print()
    mysq=mycon.execute("select * from staff")
    mysq=mycon.fetchall()
    for i in mysq:
        print(i)

    

c="yes"
while(c=="yes"):
    menu()
    opt=int(input("ENTER YOUR CHOICE :"))
    if opt==1:
        about()
    elif opt==2:
        showlist()
    elif opt==3:
        addstock()
    elif opt==4:
        updatestock()
    elif opt==5:
        deletestock()
    elif opt==6:
        custorder()
    elif opt==7:
        billrecords()
    elif opt==8:
        recordorder()
    elif opt==9:
        insertstaff()
    elif opt==10:
        showstaff()
    elif opt==11:
        deletestaff()
    elif opt==12:
        updatestaff()
    elif opt==13:
        print("EXITING FROM PROGRAM")
        break
    else:
        print("WRONG ENTER PLEASE ENTER THE CORRECT CHOICE:")
    c=input("do you want to continue(yes/no):")
