from tkinter import *
from tkinter import messagebox
#main login form 
top=Tk()
top.geometry("600x600+400+100")
t1=Entry(top,width=17)
t1.place(x=400,y=150)
t2=Entry(top,width=17)
t2.place(x=400,y=300)
t1.focus()



def Cancel():
    top.destroy()
# signup page creation
def signup():
    win=Tk()
    win.geometry("600x600+400+100")
    f1=Label(win,text="Registration Form",font=("Arial Bold",14))
    f1.pack()
    l1=Label(win,text="Name",font=("Arial Bold",10))
    l1.place(x=30,y=70)
    l1=Label(win,text="Email Id",font=("Arial Bold",10))
    l1.place(x=30,y=140)
    l1=Label(win,text="Address",font=("Arial Bold",10))
    l1.place(x=30,y=210)
    l1=Label(win,text="Phone No.",font=("Arial Bold",10))
    l1.place(x=30,y=280)
    l1=Label(win,text="User Id",font=("Arial Bold",10))
    l1.place(x=30,y=350)
    l1=Label(win,text="Password",font=("Arial Bold",10))
    l1.place(x=30,y=420)
    g1=Entry(win,width=17)
    g1.place(x=440,y=70)
    g2=Entry(win,width=17)
    g2.place(x=440,y=140)
    g4=Entry(win,width=17)
    g4.place(x=440,y=210)
    g5=Entry(win,width=17)
    g5.place(x=440,y=280)
    g6=Entry(win,width=17)
    g6.place(x=440,y=350)
    g7=Entry(win,width=17)
    g7.place(x=440,y=420)
    g1.focus()
#save the details in database 
    def save():
                import cx_Oracle
                con = cx_Oracle.connect('system/abc123@localhost')
                cursor = con.cursor()
                data = [(g1.get(),g2.get(),g4.get(),g5.get(),g6.get(),g7.get())]
                cursor.executemany('insert into user_c values(:1,:2,:3,:4,:5,:6)', data)
                con.commit()
                print('Record inserted successfully')

    def back():
         win.destroy()
    b7=Button(win,text ="Cancel",command=back)
    b7.place(x=400,y=540)
    b6=Button(win,text ="Register",command=save)
    b6.place(x=100,y=540)

# LOgin Page Creation
def Login():

    import cx_Oracle
    con = cx_Oracle.connect('system/abc123@localhost')
    cursor = con.cursor()
    uid= t1.get()
    pwd=t2.get()
    cursor.execute("SELECT password FROM user_c WHERE username = :id", {'id': uid})
    r=cursor.fetchall()
    pas=r[0][0]
    if pwd==pas:
        messagebox.showinfo("conf","ok")

        
               
        root=Tk()
        root.geometry("600x600+400+100")
        f1=Label(root,text="ABC BANK",font=("Arial Bold",14))
        f1.place(x=270,y=10)
# Account Open for the Account Holder
        def open():
            open = Tk()
            open.geometry("600x600+400+100")
            f1=Label(open,text="Account Open",font=("Arial Bold",14))
            f1.place(x=250,y=10)
            l1=Label(open,text="Account Number",font=("Arial Bold",10))
            l1.place(x=30,y=70)
            l1=Label(open,text="Account Name",font=("Arial Bold",10))
            l1.place(x=30,y=140)

            l1=Label(open,text="DOB",font=("Arial Bold",10))
            l1.place(x=30,y=210)
            l1=Label(open,text="Address",font=("Arial Bold",10))
            l1.place(x=30,y=280)
            l1=Label(open,text="Phone No.",font=("Arial Bold",10))
            l1.place(x=30,y=350)
            l1=Label(open,text="Email",font=("Arial Bold",10))
            l1.place(x=30,y=420)
            l1=Label(open,text="Deposit amt",font=("Arial Bold",10))
            l1.place(x=30,y=490)
            O1=Entry(open,width=17)
            O1.place(x=440,y=70)
            O2=Entry(open,width=17)
            O2.place(x=440,y=140)
            O4=Entry(open,width=17)
            O4.place(x=440,y=210)
            O5=Entry(open,width=17)
            O5.place(x=440,y=280)
            O6=Entry(open,width=17)
            O6.place(x=440,y=350)
            O7=Entry(open,width=17)
            O7.place(x=440,y=420)
            O8=Entry(open,width=17)
            O8.place(x=440,y=490)
            O1.focus()
   

            def back():
                open.destroy()
            def save():
                import cx_Oracle
                con = cx_Oracle.connect('system/abc123@localhost')
                cursor = con.cursor()
                data = [(O1.get(),O2.get(),O4.get(),O5.get(),O6.get(),O7.get(),O8.get())]
                cursor.executemany('insert into abcbank values(:1,:2,:3,:4,:5,:6,:7)', data)
                con.commit()
                print('Record inserted successfully')



            b2=Button(open,text ="BACK",command=back)
            b2.place(x=390,y=550)
            b1=Button(open,text ="A/C Open",command=save)

            b1.place(x=170,y=550)



        


        b6=Button(root,text ="A/C open",width=20,command =open)
        b6.place(x=250,y=50)
#Account Information for Account Holder
        def inform():
            inform=Tk()
            inform.geometry("600x600+400+100")
            f1=Label(inform,text="Account Open",font=("Arial Bold",14))
            f1.place(x=250,y=10)
            l1=Label(inform,text="Account Number",font=("Arial Bold",10))
            l1.place(x=30,y=70)
            l1=Label(inform,text="Account Name",font=("Arial Bold",10))
            l1.place(x=30,y=140)

            l1=Label(inform,text="DOB",font=("Arial Bold",10))
            l1.place(x=30,y=210)
            l1=Label(inform,text="Address",font=("Arial Bold",10))
            l1.place(x=30,y=280)
            l1=Label(inform,text="Phone No.",font=("Arial Bold",10))
            l1.place(x=30,y=350)
            l1=Label(inform,text="Email",font=("Arial Bold",10))
            l1.place(x=30,y=420)
            l1=Label(inform,text="Balance",font=("Arial Bold",10))
            l1.place(x=30,y=490)
            q1=Entry(inform,width=17)
            q1.place(x=440,y=70)
            q2=Entry(inform,width=17)
            q2.place(x=440,y=140)
            q4=Entry(inform,width=17)
            q4.place(x=440,y=210)
            q5=Entry(inform,width=17)
            q5.place(x=440,y=280)
            q6=Entry(inform,width=17)
            q6.place(x=440,y=350)
            q7=Entry(inform,width=17)
            q7.place(x=440,y=420)
            q8=Entry(inform,width=17)
            q8.place(x=440,y=490)
            q1.focus()
            def find():
                    
                    import cx_Oracle
                    con = cx_Oracle.connect('system/abc123@localhost')

                    def clear():
                         q1.delete(0,20)
                         q2.delete(0,20)
                         q4.delete(0,20)
                         q5.delete(0,20)
                         q6.delete(0,20)
                         q7.delete(0,20)
                         q8.delete(0,20)

                         q1.focus()


                    try:
                        cur= con.cursor()
                        n=q1.get()
                        clear()
                        cur.execute("select * from abcbank where acnumber=" + n)
                        r=cur.fetchall()
                        q1.insert(0,r[0][0])
                        q2.insert(0,r[0][1])
                        q4.insert(0,r[0][2])  
                        q5.insert(0,r[0][3])
                        q6.insert(0,r[0][4])
                        q7.insert(0,r[0][5])
                        q8.insert(0,r[0][6])

                    except Exception as err:
                       messagebox.showinfo("Error","Number Not Found ")
            b6=Button(inform,text ="find",width=20,command=find)
            b6.place(x=170,y=550)
            def back():
                 inform.destroy()
       

            b6=Button(inform,text ="Back",width=20,command=back)
            b6.place(x=390,y=550)
        b6=Button(root,text ="A/C inform",width=20,command=inform)
        b6.place(x=250,y=150)
#Deposit Money For Account Holder
        def update():
            edit=Tk()
            edit.geometry("600x600+400+100")
            f1=Label(edit,text="Deposit Page",font=("Arial Bold",19))
            f1.place(x=250,y=10)

            f1=Label(edit,text="Account Number",font=("Arial Bold",14))
            f1.place(x=30,y=90)
            f8=Entry(edit,width=17)
            f8.place(x=250,y=95)
            f8.focus()
            
            f1=Label(edit,text="Account Holder Name",font=("Arial Bold",10))
            f1.place(x=30,y=160)
            l1=Label(edit,text="Account Holder DOB",font=("Arial Bold",10))
            l1.place(x=30,y=230)
            l1=Label(edit,text="Balance",font=("Arial Bold",10))
            l1.place(x=30,y=300)




            p1=Entry(edit,width=17)
            p1.place(x=440,y=160)
            p2=Entry(edit,width=17)
            p2.place(x=440,y=230)
            p4=Entry(edit,width=17)
            p4.place(x=440,y=300)
            p1.focus()

            

            

            def fonti():
                      import cx_Oracle
                      con = cx_Oracle.connect('system/abc123@localhost')


                      def clear():
                         p1.delete(0,20)
                         p2.delete(0,20)
                         p4.delete(0,20)
                         p1.focus()

                      try:
                        cursor= con.cursor()
                        p=f8.get()
                        
                        cursor.execute("select * from abcbank where acnumber=" + p)
                        mr=cursor.fetchall()
                        p1.insert(0,mr[0][1])
                        p2.insert(0,mr[0][2])
                        p4.insert(0,mr[0][6])  
                      except Exception as err:
                          print(err)
                
            
            
            b6=Button(edit,text ="Submit",width=20,command=fonti)

            b6.place(x=420,y=90)
            l1=Label(edit,text="Enter Amount For Deposit",font=("Arial Bold",10))
            l1.place(x=30,y=380)
            p3=Entry(edit,width=17)
            p3.place(x=250,y=380)


            l1=Label(edit,text="Balance Ater Deposition",font=("Arial Bold",10))
            l1.place(x=30,y=500)

            y3=Entry(edit,width=17)
            y3.place(x=440,y=500)
            def add():
                   a=p3.get()
                   b=p4.get()
                   c=float(a)+float(b)
                   y3.insert(0,c)
            b6=Button(edit,text ="Deposit",width=20,command=add)

            b6.place(x=420,y=370)
            def apple():
                      import cx_Oracle
                      con = cx_Oracle.connect('system/abc123@localhost')

                      cur = con.cursor()
                      sql = "UPDATE abcbank SET depo = :new WHERE acnumber = :new1"
                      cur.execute(sql, {'new': y3.get(), 'new1': f8.get()})
                      con.commit()

    

                      print(cur.rowcount, "record(s) affected")
                      messagebox.showinfo("Title","Updated")
                      cur.close()
            b6=Button(edit,text ="OK",width=20,command=apple)

            b6.place(x=420,y=550)

        b6=Button(root,text ="Deposit",width=20,command=update)
        b6.place(x=250,y=250)
#Withdrawl Amount For Account Holder
        def withdraw():
            adit=Tk()
            adit.geometry("600x600+400+100")
            f1=Label(adit,text="withdrawl Page",font=("Arial Bold",19))
            f1.place(x=250,y=10)

            f1=Label(adit,text="Account Number",font=("Arial Bold",14))
            f1.place(x=30,y=90)
            f8=Entry(adit,width=17)
            f8.place(x=250,y=95)
            f8.focus()
            
            f1=Label(adit,text="Account Holder Name",font=("Arial Bold",10))
            f1.place(x=30,y=160)
            l1=Label(adit,text="Account Holder DOB",font=("Arial Bold",10))
            l1.place(x=30,y=230)
            l1=Label(adit,text="Balance",font=("Arial Bold",10))
            l1.place(x=30,y=300)




            p1=Entry(adit,width=17)
            p1.place(x=440,y=160)
            p2=Entry(adit,width=17)
            p2.place(x=440,y=230)
            p4=Entry(adit,width=17)
            p4.place(x=440,y=300)

            

            

            def fonti():
                      import cx_Oracle
                      con = cx_Oracle.connect('system/abc123@localhost')


                      def clear():
                         p1.delete(0,20)
                         p2.delete(0,20)
                         p4.delete(0,20)
                         p1.focus()

                      try:
                        cursor= con.cursor()
                        p=f8.get()
                        
                        cursor.execute("select * from abcbank where acnumber=" + p)
                        mr=cursor.fetchall()
                        p1.insert(0,mr[0][1])
                        p2.insert(0,mr[0][2])
                        p4.insert(0,mr[0][6])  
                      except Exception as err:
                          print(err)
                
            
            
            b6=Button(adit,text ="Submit",width=20,command=fonti)

            b6.place(x=420,y=90)
            l1=Label(adit,text="Enter Amount For withdrawl",font=("Arial Bold",10))
            l1.place(x=30,y=380)
            p3=Entry(adit,width=17)
            p3.place(x=250,y=380)


            l1=Label(adit,text="Balance Ater withdraw",font=("Arial Bold",10))
            l1.place(x=30,y=500)

            y3=Entry(adit,width=17)
            y3.place(x=440,y=500)
            def sub():
                   a=p3.get()
                   b=p4.get()
                   c=abs(float(a)-float(b))
                   y3.insert(0,c)
            b6=Button(adit,text ="withdraw",width=20,command=sub)

            b6.place(x=420,y=370)
            def apple():
                      import cx_Oracle
                      con = cx_Oracle.connect('system/abc123@localhost')

                      cur = con.cursor()
                      sql = "UPDATE abcbank SET depo = :new WHERE acnumber = :new1"
                      cur.execute(sql, {'new': y3.get(), 'new1': f8.get()})
                      con.commit()

                      print(cur.rowcount, "record(s) affected")
                      messagebox.showinfo("Title","Updated")
                      cur.close()
            b6=Button(adit,text ="OK",width=20,command=apple)

            b6.place(x=420,y=550)

        b6=Button(root,text ="Withdrawl",width=20,command=withdraw)
        b6.place(x=250,y=350)
#Account Close for Account Holder

        def close():
            close=Tk()
            close.geometry("600x600+400+100")
            f1=Label(close,text="Account close",font=("Arial Bold",14))
            f1.place(x=250,y=10)
            l1=Label(close,text="Account Number",font=("Arial Bold",10))
            l1.place(x=30,y=70)
            l1=Label(close,text="Account Name",font=("Arial Bold",10))
            l1.place(x=30,y=140)

            l1=Label(close,text="DOB",font=("Arial Bold",10))
            l1.place(x=30,y=210)
            l1=Label(close,text="Address",font=("Arial Bold",10))
            l1.place(x=30,y=280)
            l1=Label(close,text="Phone No.",font=("Arial Bold",10))
            l1.place(x=30,y=350)
            l1=Label(close,text="Email",font=("Arial Bold",10))
            l1.place(x=30,y=420)
            l1=Label(close,text="Balance",font=("Arial Bold",10))
            l1.place(x=30,y=490)
            q1=Entry(close,width=17)
            q1.place(x=440,y=70)
            q2=Entry(close,width=17)
            q2.place(x=440,y=140)
            q4=Entry(close,width=17)
            q4.place(x=440,y=210)
            q5=Entry(close,width=17)
            q5.place(x=440,y=280)
            q6=Entry(close,width=17)
            q6.place(x=440,y=350)
            q7=Entry(close,width=17)
            q7.place(x=440,y=420)
            q8=Entry(close,width=17)
            q8.place(x=440,y=490)
            q1.focus()
            def find():
                      import cx_Oracle
                      con = cx_Oracle.connect('system/abc123@localhost')
                      def clear():
                         q1.delete(0,20)
                         q2.delete(0,20)
                         q4.delete(0,20)
                         q5.delete(0,20)
                         q6.delete(0,20)
                         q7.delete(0,20)
                         q8.delete(0,20)

                         q1.focus()


                      try:
                        cur= con.cursor()
                        n=q1.get()
                        clear()
                        cur.execute("select * from abcbank where acnumber=" + n)
                        r=cur.fetchall()
                        q1.insert(0,r[0][0])
                        q2.insert(0,r[0][1])
                        q4.insert(0,r[0][2])  
                        q5.insert(0,r[0][3])
                        q6.insert(0,r[0][4])
                        q7.insert(0,r[0][5])
                        q8.insert(0,r[0][6])

                      except Exception as err:
                       messagebox.showinfo("Error","Number Not Found ")
            b6=Button(close,text ="find",width=20,command=find)
            b6.place(x=150,y=550)
            def delete():
                      import cx_Oracle
                      con = cx_Oracle.connect('system/abc123@localhost')

                      cur = con.cursor()
                      cur.execute("delete from abcbank where acnumber=" + q1.get() )
                      con.commit()
                      messagebox.showinfo("Title","Deleted")
                      cur.close()
        
            b6=Button(close,text ="Close",width=20,command=delete)
            b6.place(x=300,y=550)

        b6=Button(root,text ="A/C close",width=20,command=close)
        b6.place(x=250,y=450)
        def bye():
           root.destroy()
        b6=Button(root,text ="Exit",width=20,command=bye)
        b6.place(x=250,y=550)
    else :
            messagebox.showerror("Error","Invalid")
 
         


        

 
         


top.title("Logic Form")
l1=Label(top,text="Login Form",font=("Arial Bold",20))
l1.pack()
l1=Label(top,text="Enter User Id",font=("Arial Bold",13))
l1.place(x=30,y=150)
l1=Label(top,text="Enter Password",font=("Arial Bold",13))
l1.place(x=30,y=300)
b1=Button(top,text ="Sign In",command=Login)
b1.place(x=50,y=450)
b1=Button(top,text ="Cancel",command=Cancel)
b1.place(x=270,y=450)
b1=Button(top,text ="Sign Up",command=signup)
b1.place(x=490,y=450)

top.mainloop() 
 
        
