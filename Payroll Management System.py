import mysql.connector
from tabulate import tabulate
import datetime
db=input("Enter the name of the database: ")
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Chimutindsri7#')
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE "+db)
print("Database created successfully")
mycursor=mydb.cursor()
mycursor.execute("Use "+db)
tablename=input("Enter the name of the table: ")
query="create table if not exists "+tablename+" (empno int primary key, name varchar(15) not null, job varchar(15), basicsalary int, da float, hra float, grosssalary float, tax float, netsalary float)"
print("Table created successfully")
mycursor.execute(query)

while True:
    print("\n\n\n")
    print("Main Menu")
    print("\n")
    print("1.Adding Employee Records")
    print("2.For displaying record of all employees")
    print("3.For displaying record of a particular employee")
    print("4.For deleting records of all employees")
    print("5.For deleting a record of particular employee")
    print("6.For modification in a record")
    print("7.For displaying payroll")
    print("8.For displaying salary slip of all the emplyees")
    print("9.For displaying salary slip of the particular employee")
    print("10.Exit")
    print("\n")
    print("Enter Choice: ")
    choice=int(input())

    if choice==1:
        try:
            print("Enter Employee Information")
            mempno=int(input("Enter employee no: "))
            mname=input("Enter employee name: ")
            mjob=input("Enter employee job: ")
            mbasic=float(input("Enter basic salary: "))
            if mjob.upper()=="OFFICER":
                mda=mbasic*0.5
                mhra=mbasic*0.35
                mtax=mbasic*0.2
            elif mjob.upper()=="MANAGER":
                mda=mbasic*0.45
                mhra=mbasic*0.30
                mtax=mbasic*0.15
            else:
                mda=mbasic*0.40
                mhra=mbasic*0.25
                mtax=mbasic*0.1
            mgross=mbasic+mda+mhra
            mnet=mgross-mtax
            rec =(mempno,mname,mjob,mbasic,mda,mhra,mgross,mtax,mnet)
            query="insert into "+tablename+" values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(query,rec) 
            mydb.commit()
            print("Record added")
        except:
            print("Something went wrong")

    elif choice==2:
        try:
            query="select * from "+tablename
            mycursor.execute(query)
            print(tabulate(mycursor, headers=['Empno','Name','Job','Basic salary','Da','Hra','Grosssalary','Tax','Netsalary'], tablefmt='fancy_gris'))
        except:
            print("Something went wrong")

    elif choice==3:
        try:
            en=input('Enter employee no of the record to be displayed:')
            query="select * from "+tablename+" where empno="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("Record of employee no:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==-1:
                print("Nothing to display")
        except:
           print("Something went wrong")

    elif choice==4:
        try:
            ch=input("Do you want to delete all the records y/n: ")
            if ch.upper()=="Y":
                mycursor.execute("delete from "+tablename)
                mydb.commit()
                print("All the records are deleted")
        except:
            print("Something went wrong")

    elif choice==5:
        try:
            en=input("Enter employee no of the record to be deleted: ")
            query="delete from "+tablename+" where empno="+en
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print("Deletion done")
            else:
                print("Employee no ",en," not found")
        except:
            print("Something went wrong")
            
    elif choice==6:
        try:
            en=input("Enter employee no of the record to be modified: ")
            query="select * from "+tablename+" where empno="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print("empno "+en+" does not exist")
            else:
                mname=myrecord[1]
                mjob=myrecord[2]
                mbasic=myrecord[3]
                print("Empno :",myrecord[0])
                print("Name :",myrecord[1])
                print("Job :",myrecord[2])
                print("Basic :",myrecord[3])
                print("Da :",myrecord[4])
                print("Hra :",myrecord[5])
                print("Gross :",myrecord[6])
                print("Tax :",myrecord[7])
                print("Net :",myrecord[8])
                print("Type value to modify or enter for no change")
                x=input("Enter name: ")
                if len(x)>0:
                 mname=x
                x=input("Enter job: ")
                if len(x)>0:
                 mjob=x
                x=input("Enter basic salary: ")
                if len(x)>0:
                 mbasic=float(x)
                query="update "+tablename+" set name="+"'"+mname+"'"+','+'job='+"'"+mjob+"'"+','+'basicsalary='+str(mbasic)+' where empno='+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("Record modified: ")
        except:
            print("Something went wrong")

    elif choice==7:
        try:
            query='select * from '+tablename
            mycursor.execute(query)
            myrecords=mycursor.fetchall()
            print('Employee Payroll'.center(90))
            now=datetime.datetime.now()
            print("Current date and time: ",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print()
            print(95*'-')
            print('%-5s %-15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s'\
                  %('Empno','Name','Job','Basic','Da','Hra','Gross','Tax','Net'))
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
        except:
            print("Something went wrong")

    elif choice==8:
        try:
            query='select * from '+tablename
            mycursor.execute(query)
            now = datetime.datetime.now()
            print("Salary Slip")
            print("Current date and time:",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            myrecords=mycursor.fetchall()
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
        except:
                print('Something went wrong')

    elif choice==10:
        break

    else:
        print("Wrong choice")
        



            
