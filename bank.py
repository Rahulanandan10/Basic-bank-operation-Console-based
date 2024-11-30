import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rahul@2004",
    database="bank")
mycursor=mydb.cursor()
ch=1
while(ch<5):
    print("1.To add account\n2.To Deposit amount\n3.To Withdraw amount\n4.To display details\n5.To exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        l=[]
        name=input("Enter name:")
        l.append(name)
        accno=int(input("Enter account number:"))
        l.append(accno)
        bal=0
        l.append(bal)
        qry="insert into account(name,accno,balance) values(%s,%s,%s)"
        mycursor.execute(qry,l)
        mydb.commit()
    elif ch==2:
        l=[]
        m=[]
        n=[]
        ac=int(input("Enter account number:"))
        amt=int(input("Enter amount to deposit:"))
        que="select balance from account where accno=%s"
        m.append(ac)
        mycursor.execute(que,m)
        r=mycursor.fetchone()
        n=list(r)
        t=n[0]
        bal=t+amt
        l.append(bal)
        l.append(ac)
        sql="update account set balance=%s where accno=%s"
        mycursor.execute(sql,l)
        print("Amount deposited")
        mydb.commit()
    elif ch==3:
        l=[]
        m=[]
        n=[]
        ac=int(input("Enter account number:"))
        amt=int(input("Enter amount to Withdraw:"))
        que="select balance from account where accno=%s"
        m.append(ac)
        mycursor.execute(que,m)
        r=mycursor.fetchone()
        if (r==None):
            print("Account not found")
        else:
            n=list(r)
            t=n[0]
            if (t<amt):
                print("Insufficient amount")
            else:
                bal=t-amt
                l.append(bal)
                l.append(ac)
                sql="update account set balance=%s where accno=%s"
                mycursor.execute(sql,l)
                print("Amount withdrawn")
                mydb.commit()
        
    elif ch==4:
        l=[]
        m=[]
        print("1.Search with accno\n2.Search with name")
        ch=int(input("Enter choice:"))
        if ch==1:
            ac=int(input("Enter account number:"))
            qr="Select accno from account"
            mycursor.execute(qr)
            l=mycursor.fetchall()
            m.append(ac)
            qry="select * from account where accno=%s"
            mycursor.execute(qry,m)
            r=mycursor.fetchall()
            if r==[]:
                print("Account not found")
            else:
                print("Account details")
                print(r)
        if ch==2:
            na=input("Enter name:")
            qr="Select name from account"
            mycursor.execute(qr)
            l=mycursor.fetchall()
            m.append(na)
            qry="select * from account where name=%s"
            mycursor.execute(qry,m)
            r=mycursor.fetchall()
            if r==[]:
                print("Account not found")
            else:
                print("Account details")
                print(r)
            
            
                
            
                
        
