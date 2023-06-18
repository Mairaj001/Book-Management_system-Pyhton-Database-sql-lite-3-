from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import numpy as np
import entryclear
from tkinter import ttk
import random
import string
import datetime




root=Tk()



root.title("Login page")
root.configure(bg="#fff")
root.geometry("1100x500+300+200")
root.resizable(False,False)

connection=sqlite3.connect("library_sys2.db")
cursor=connection.cursor()

#cursor.execute("""CREATE TABLE user_details (
    
 #       first_name text,
  #      Last_name text,
   #     username text,
    #   password text) """)


# function for checking removing the text of the fields name  
# creating database here
 
################################################sign_up start########################################################
def new_login():
    
    def entry_of_data():
        connection=sqlite3.connect("library_sys2.db")
        cursor=connection.cursor()
        
        cursor.execute("INSERT INTO user_details VALUES (:f_name,:L_name,:user_name,:password)",
                       {
                         'f_name':khoo.get(),
                         'L_name':last_name.get(),
                         'user_name':username.get(),
                         'password':pasword.get()
                       })
      
    
        connection.commit()
        connection.close()
        
    
    
    def see_pass(event):
        pasword.config(show="")
        confrim_pass.config(show="")
        
    def hide_pass(event):
        pasword.config(show="*")
        confrim_pass.config(show="*")
        
    
    def check_pass_both_true():
        check_first_pass=pasword.get()
        check_second_pass=confrim_pass.get()
        usernum=username.get()
        
        if check_first_pass!=check_second_pass:
            messagebox.showerror("Invalid password error","Please enter the same password")
            
        elif check_first_pass==check_second_pass:
            entry_of_data()
            messagebox.showinfo("Sussesfull","Your account is created")
            screen.after(500,screen.destroy)
        elif check_first_pass==''or check_second_pass=='' or usernum=='':
            messagebox.showerror("Invalid Entry", "please enter the all fields")
        
    def clear_fname(event):
        khoo.delete(0,END)
     
    
    def clear_Lname(event):
        last_name.delete(0,END)
    
    def clear_username(event):
        username.delete(0,END)
    
    def clear_paswrdd(event):
        pasword.delete(0,END)
        pasword.config(show="*")
    
    def clear_passcnfrm(event):
        confrim_pass.delete(0,END)
        confrim_pass.config(show="*")
        
    
    
    screen=Toplevel(root)
    screen.title("Sign up")
    #screen.geometry("1100x500+300+200")
    screen.config(bg="white")
    screen.resizable(False,False)
    
    
    
    image=ImageTk.PhotoImage(file="Assets/bg2.jpg")
    
    Label(screen,image=image,bg="white").grid(row=0,column=0)
    #creating signup frame text in it
    

    heading=Label(screen, text="Sign up", fg="#C71585", bg="white", font=("Microsoft Yahei UI light",28,'bold'))
    heading.place(x=700,y=110)
    
    khoo=Entry(screen,fg="black",border=0,highlightcolor="red",highlightbackground="blue",highlightthickness=0,width=10,font=("Microsoft Yahei UI light",11,'bold'))
    khoo.place(x=640,y=230)
    khoo.insert(0,"First name")
    
    
    Frame(screen,width=100,height=2,bg="#FF1493").place(x=640,y=260)
    khoo.bind("<Button-1>",clear_fname)
    
    last_name=Entry(screen,fg="black",border=0,width=11,font=("Microsoft Yahei UI light",11,'bold'))
    last_name.place(x=820,y=230)
    last_name.insert(0,"Last name")
    
    
    Frame(screen,width=100,height=2,bg="#FF1493").place(x=820,y=260)
    last_name.bind("<Button-1>",clear_Lname)
    
    username=Entry(screen,fg="black",border=0,width=24,font=("Microsoft Yahei UI light",11,'bold'))
    username.place(x=640,y=300)
    username.insert(0,"Username")
    
    
    Frame(screen,width=280,height=2,bg="#FF1493").place(x=640,y=328)
    username.bind("<Button-1>",clear_username)
    
    pasword=Entry(screen,fg="black",border=0,width=20,font=("Microsoft Yahei UI light",11,'bold'))
    pasword.place(x=640,y=365)
    pasword.insert(0,"Password")
    
    Frame(screen,width=280,height=2,bg="#FF1493").place(x=640,y=392)
    pasword.bind("<Button-1>",clear_paswrdd)
    
    

    
    
    confrim_pass=Entry(screen,fg="black",border=0,width=25, font=("Microsoft Yahei UI light",11,'bold'))
    confrim_pass.place(x=640,y=430)
    confrim_pass.insert(0,"Retype password")
    
    
    Frame(screen,width=280,height=2,bg="#FF1493").place(x=640,y=460)
    confrim_pass.bind("<Button-1>",clear_passcnfrm)
    
    show_pass=Button(screen, text="See passwords", bg="white", fg="#FF1493", font=("Microsoft Yahei UI light",9,'bold'), width=11, cursor="hand2", border=0)
    show_pass.place(x=815,y=465)
    show_pass.bind("<ButtonRelease-1>",hide_pass)
    show_pass.bind("<ButtonPress-1>",see_pass)
    
    register=Button(screen, text="Register", width=24, pady=4, bg="#FF1493",fg="White",font=("Microsoft Yahei UI light",9,'bold'),command=check_pass_both_true)
    register.place(x=655,y=515)
    
    
    
    
    #FF7F50
    
    screen.mainloop()
    
##########################################SIGN UP END############################################################### 

#########################################FORGOT START##############################################################

def forgot_ui():
    
    #######eye jpg will be added in the password section 
    
    def update_password():
        get_user=u_name.get()
        get_user_pass=pass1.get()
        
        connection=sqlite3.connect("library_sys2.db")
        cursor=connection.cursor()
        cursor.execute("SELECT * , oid FROM user_details")
        records=cursor.fetchall()
        status=False
        for i in records:
            print(i)
            if get_user==i[2]:
                status=True
                userid=i[4]
        
        if status==True:
            cursor.execute("""UPDATE user_details SET 
                           password = :pass
                           
                           WHERE oid = :oid""",
                           {
                               'pass':pass1.get(),
                               'oid':userid
                           })
                           
            messagebox.showinfo("Message","Password updated sussesfully")
        
        elif status==False:
            messagebox.showerror("Invalid","Invalid username or account is not created")
        
        connection.commit()
        connection.close()
        
    
    def clear_uname(event):
        var=u_name.get()
        
        if var=="Enter Username":
            u_name.delete(0,END)
        else:
            return
        
    def clear_pass(event):
        var2=pass1.get()
        
        if var2=="New Password":
            pass1.delete(0,END)
            pass1.config(show="*")
        
    
    
    forgot_screen=Toplevel(root)
    forgot_screen.geometry("1100x500+300+200")
    forgot_screen.title("FORGOT SCREEN")
    forgot_screen.resizable(False,False)
    forgot_screen.configure(bg="White")
    
    imgf=ImageTk.PhotoImage(file="Assets/forgot.jpg")
    Label(forgot_screen,image=imgf,bg="white").place(x=-50,y=30)
    
    heading=Label(forgot_screen,text="Enter your information",fg="#088F8F", bg="white", font=("Microsoft Yahei UI light",20,'bold'))
    heading.place(x=670,y=50)
    
    
    u_name=Entry(forgot_screen,fg="black",border=0,width=25,insertborderwidth=10,font=("Microsoft Yahei UI light",11,'bold'))
    u_name.place(x=700,y=150)
    u_name.insert(0,"Enter Username")
    u_name.bind("<Button-1>",clear_uname)
    
    Frame(forgot_screen,width=280,height=2,bg="#088F8F").place(x=700,y=180)
    
    
    
    pass1=Entry(forgot_screen,fg="black",border=0,width=25,insertborderwidth=10,font=("Microsoft Yahei UI light",11,'bold'))
    pass1.place(x=700,y=230)
    pass1.insert(0,"New Password")
    pass1.bind("<Button-1>",clear_pass)
    Frame(forgot_screen,width=280,height=2,bg="#088F8F").place(x=700,y=260)
    
    update_button=Button(forgot_screen,text="Update", bg="#088F8F", fg="white", font=("Microsoft Yahei UI light",9,'bold'), width=20, cursor="hand2", border=0,command=update_password)
    update_button.place(x=730,y=300)
    
    forgot_screen.mainloop()
    


###################################################FORGOT END ########################################################################################################################################

######################################   STORE  - GUI - START  ################################################################################

#######################################################################################################################################################################################################
    
#starting of main work from here library system


#################################################    ADMIN   ~~~~~~~~~~~~~~~~~~~~~~~~~~###########################################################################################################


    
    
def administration_portal():
    
   
    
    def back_menu_button():
        
        signin_screen()
        return
    
    def admin_portal_orignal():
        
        def back_from_admin():
           admin_screen2.destroy()
           back_menu_button()
        
        def Stock_page():
            
            title_frame=Frame(main_frame,bg='Blue',width=1037,height=100)
            disp_title_img=Label(title_frame,text="Stock",bg="blue",fg='red',font=('bold',40))
            disp_title_img.place(x=450,y=15)
            title_frame.pack()
            
            def show_books():
                b_name=book_name.get()
                athr=Authr_name.get()
                dbs_acces=False
                dbs_acces2=False
                if (b_name=="" and athr=="") or (b_name=="Bookname" and athr=="Author_name"):
                    messagebox.showerror("Error","Please fill the all fields")
                elif (b_name!="" and athr!="") or (b_name!="Bookname" and athr!="Author_name"):
                    dbs_acces=True
                    
                if dbs_acces==True:
                    connection=sqlite3.connect("library_sys2.db")
                    cursor=connection.cursor()
                    cursor.execute("Select author_id from author_details where name=?",(athr,))
                    athr_id=cursor.fetchone()
                    print(athr_id)
                    
                    if athr_id==None:
                        messagebox.showinfo("INFO",f"Author {athr} is not available in the database")
                    else:
                        dbs_acces2=True
                    cursor.execute("Select ISBN from Books_details where book_name=?",(b_name,))
                    b_isbn=cursor.fetchone()
                   
                    print(b_isbn)
                    if b_isbn==None:
                        messagebox.showinfo("INFO",f"Book [{b_name}]  not available")
                        dbs_acces2=False
                    
                if dbs_acces2==True:
                    colum_name=("Book_name","ISBN","Authr_name","Publisher_name","Genre","Quantity","Price")
                    
                    for i,col in enumerate(colum_name):
                      label = Label(frame, text=col, font=("Arial", 8, "bold"))
                      label.grid(row=0, column=i+5, padx=2, pady=5)
                    cursor.execute("Select b.book_name,b.ISBN,a.name,p.publisher_name,b.genre,b.quantity,b.price from Books_details b, author_details a, publisher_details p where a.author_id=b.author_id and b.publisher_id=p.publisher_id and  b.book_name=? and a.name=?",(b_name,athr))
                    data=cursor.fetchall()
                    print(data)
                    if data==[]:
                        messagebox.showinfo("INFO",f"BOOK[{b_name} having authr {athr} is not available]")
                    for row, record in enumerate(data):
                     for col, value in enumerate(record):
                      label = Label(frame, text=value,font=(6))
                      label.grid(row=row+1, column=col+5, padx=18, pady=7)
                    
                connection.commit()
                connection.close()
                return
            
            
            def on_canvas_configure(event):
                 canvas.configure(scrollregion=canvas.bbox("all"))

            canva_frame=Frame(main_frame,width=1020,height=280)
            canva_frame.pack()
                
            x_scrollbar = Scrollbar(canva_frame, orient=HORIZONTAL)
            x_scrollbar.pack(side=BOTTOM, fill=X)

                
            y_scrollbar = Scrollbar(canva_frame)
            y_scrollbar.pack(side=RIGHT, fill=Y)


            canvas = Canvas(canva_frame, xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set,width=1020,height=350)
            canvas.pack(side=LEFT, fill=BOTH, expand=True)


            x_scrollbar.config(command=canvas.xview)
            y_scrollbar.config(command=canvas.yview)


            canvas.bind("<Configure>", on_canvas_configure)


            frame = Frame(canvas,width=1020,height=350)
            canvas.create_window((0, 0), window=frame, anchor="nw")
            
            book_name=Entry(main_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
            book_name.place(x=200,y=500)
            book_name.insert(0,"Bookname")
            book_name.bind("<Button-1>", lambda event:entryclear.clear_ISBN(book_name))
            Frame(main_frame,width=221,height=2,bg="red").place(x=200,y=500)
            Frame(main_frame,width=221,height=2,bg="red").place(x=200,y=527)
            
            
            Authr_name=Entry(main_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
            Authr_name.place(x=600,y=500)
            Authr_name.insert(0,"Author_name")
            Authr_name.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Authr_name))
            Frame(main_frame,width=221,height=2,bg="red").place(x=600,y=500)
            Frame(main_frame,width=221,height=2,bg="red").place(x=600,y=527)
            
            
            entr_btn=Button(main_frame,width=30,text="Enter",fg="white",bg="blue",command=show_books)
            entr_btn.place(x=395,y=600)
            
            Frame(main_frame,width=1035,height=5,highlightcolor='Black',bg='Black').place(x=0,y=100)
            
            
        def add_book_page():
            
            
            def add_book_database():
                
                database_bool=FALSE
                book_availability=False
                authors_availble=False
                pub_available=False
                Isbn_no=isbn_no.get()
                authr_id=Auth_id.get()
                publisher=Pub_id.get()
                authr_name=Auth_name.get()
                publisher_name=Pub_name.get()
                bookname=Title_name.get()
                Quant=Quantity.get()
                price=Price.get()
                Genre=genre.get()
                yrs=selected_year.get()
                print(Genre,bookname)
            
                
                
                if Isbn_no==' ISBN No' or  authr_id==' Author Id'or publisher==' Publisher Id' or authr_name==' Author name' or publisher_name==' Publisher name' or bookname==' Book Title/Name' or Genre=='Select Genre' or Quant==' Quantity' or price==' Book Price':
                    messagebox.showwarning("Information Missing","Please fill the all fields")
                    database_bool=FALSE
                elif Isbn_no!=''and authr_id!=' 'and publisher!=' ' and authr_name!=' ' and publisher_name!=' ' and bookname!=' ' and Genre!='Select Genre' and Quant!=' ' and price!=' ':
                    messagebox.showinfo("All Done", "book entered sussesfully")
                    database_bool=TRUE
                else:
                    messagebox.showwarning("Information Missing","Please fill the all fields")
                
                if database_bool:
                    print("access got to the data base")
                    connection=sqlite3.connect("library_sys2.db")
                    cursor=connection.cursor()
                    cursor.execute("Select *from Books_details")
                    book_info=cursor.fetchall()
                    cursor.execute("Select *from author_details")
                    author_info=cursor.fetchall()
                    cursor.execute("select *from publisher_details")
                    pub_info=cursor.fetchall()
                    
                    for books in book_info:
                        print(books[0])
                        if books[0]==Isbn_no:
                             book_availability=TRUE
                             break
                        else:
                             book_availability=False
                    
                    if book_availability==True:
                        messagebox.showerror("Error","Book is already entered")
                    elif book_availability==False:  # for new book 
  
                         for authors in author_info:
                            print(authors)
                            if authors[0]==authr_id:
                                authors_availble=True
                                break
                            else:
                                authors_availble=False
                         for publicators in pub_info:
                            print(publicators)
                            if publicators[0]==publisher:
                                pub_available=True
                                break
                            else:
                                pub_available=False
                                
                         if authors_availble==True and pub_available==True:
                           query="INSERT INTO books_details (ISBN, author_id, publisher_id, genre, quantity, price,book_name,year) VALUES (?, ?, ?, ?, ?, ?,?,?)"
                           values=(Isbn_no,authr_id,publisher,Genre,int(Quant),int(price),bookname,yrs)
                           cursor.execute(query,values)
                           connection.commit()
                         elif authors_availble==False and pub_available==True:
                           query="INSERT INTO books_details (ISBN, author_id, publisher_id, genre, quantity, price,book_name,year) VALUES (?, ?, ?, ?, ?, ?,?,?)"
                           values=(Isbn_no,authr_id,publisher,Genre,int(Quant),int(price),bookname,yrs)
                           cursor.execute(query,values)
                           connection.commit()
                           author_query="Insert into author_details(author_id,name) values(?,?)"
                           author_val=(authr_id,authr_name)
                           cursor.execute(author_query,author_val)
                           connection.commit()
                         elif authors_availble==True and pub_available==False:
                           query="INSERT INTO books_details (ISBN, author_id, publisher_id, genre, quantity, price,book_name,year) VALUES (?, ?, ?, ?, ?, ?,?,?)"
                           values=(Isbn_no,authr_id,publisher,Genre,int(Quant),int(price),bookname,yrs)
                           cursor.execute(query,values)
                           connection.commit()
                           pub_query="Insert into publisher_details(publisher_id,publisher_name) values(?,?)"
                           pub_val=(publisher,publisher_name)                    
                           cursor.execute(pub_query,pub_val)
                           connection.commit()
                         elif authors_availble==False and pub_available==False:
                           query="INSERT INTO books_details (ISBN, author_id, publisher_id, genre, quantity, price,book_name,year) VALUES (?, ?, ?, ?, ?, ?,?,?)"
                           values=(Isbn_no,authr_id,publisher,Genre,int(Quant),int(price),bookname,yrs)
                           cursor.execute(query,values)
                           connection.commit()
                           pub_query="Insert into publisher_details(publisher_id,publisher_name) values(?,?)"
                           pub_val=(publisher,publisher_name)                    
                           cursor.execute(pub_query,pub_val)
                           connection.commit()
                           author_query="Insert into author_details(author_id,name) values(?,?)"
                           author_val=(authr_id,authr_name)
                           cursor.execute(author_query,author_val)
                           connection.commit()
                           
                    
                    
                    
                    connection.commit()
                    connection.close()
                    
                
                
                
                return
            
            title_frame=Frame(main_frame,bg='Blue',width=1037,height=100)
            disp_title_img=Label(title_frame,text="Add books",bg="blue",fg='red',font=('bold',40))
            disp_title_img.place(x=380,y=15)
            title_frame.pack()
            Frame(main_frame,width=1035,height=5,highlightcolor='Black',bg='Black').place(x=0,y=100)
            
            
            #Label(main_frame,text='Enter the details',bg='white',fg='Blue',font=('Microsoft Yahei UI light)',30,)).place(x=200,y=120)
            
            #Frame(main_frame,width=1010,height=10 ,highlightbackground="blue", highlightcolor="blue",bg='white', highlightthickness=2).place(x=2,y=150)
            
            isbn_no=Entry(main_frame,fg="black",border=1,bg="white",width=22,font=("Microsoft Yahei UI light",11,'bold'))
            isbn_no.place(x=20,y=150)
            isbn_no.insert(0,' ISBN No')
            isbn_no.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_no))
            
            isbn_no_frame=Frame(main_frame,width=250,height=2,bg="red")
            isbn_no_frame.place(x=20,y=180)
            
            
            Auth_id=Entry(main_frame,fg="black",border=1,bg="white",width=22,font=("Microsoft Yahei UI light",11,'bold'))
            Auth_id.place(x=400,y=150)
            Auth_id.insert(0,' Author Id')
            Auth_id.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Auth_id))
            
            Auth_id_frame=Frame(main_frame,width=250,height=2,bg="red")
            Auth_id_frame.place(x=400,y=180)
            
            
            Pub_id=Entry(main_frame,fg="black",border=1,bg="white",width=22,font=("Microsoft Yahei UI light",11,'bold'))
            Pub_id.place(x=765,y=150)
            Pub_id.insert(0,' Publisher Id')
            Pub_id.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Pub_id))
            
            Pub_id_frame=Frame(main_frame,width=250,height=2,bg="red")
            Pub_id_frame.place(x=765,y=180)
            
            
            
            Auth_name=Entry(main_frame,fg="black",border=1,bg="white",width=22,font=("Microsoft Yahei UI light",11,'bold'))
            Auth_name.place(x=20,y=300)
            Auth_name.insert(0,' Author name')
            Auth_name.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Auth_name))
            
            Auth_name_frame=Frame(main_frame,width=250,height=2,bg="red")
            Auth_name_frame.place(x=20,y=331)
            
            
            
            Pub_name=Entry(main_frame,fg="black",border=1,bg="white",width=22,font=("Microsoft Yahei UI light",11,'bold'))
            Pub_name.place(x=400,y=300)
            Pub_name.insert(0,' Publisher name')
            Pub_name.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Pub_name))
            
            Pub_name_frame=Frame(main_frame,width=250,height=2,bg="red")
            Pub_name_frame.place(x=400,y=331)
            
            
            genre=StringVar()
            genre.set("Select Genre")
            genre_dropdown_menu=OptionMenu(main_frame,genre,"Mystery Books","Action Adventure book","Notification books"
                                           "Historical Fiction","Horror Novels","Fantacy Novels","Children Books",
                                           "Graphic Novels",)
            genre_dropdown_menu.config(highlightbackground="red", highlightcolor="red",fg="black",bg="white", borderwidth=2,width=22)
            genre_dropdown_menu.place(x=765,y=295)
            
            
            Title_name=Entry(main_frame,fg="black",border=1,bg="white",width=22,font=("Microsoft Yahei UI light",11,'bold'))
            Title_name.place(x=20,y=450)
            Title_name.insert(0,' Book Title/Name')
            Title_name.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Title_name))
            
            Title_name_frame=Frame(main_frame,width=250,height=2,bg="red")
            Title_name_frame.place(x=20,y=480)
            
            
            
            Quantity=Entry(main_frame,fg="black",border=1,bg="white",width=22,font=("Microsoft Yahei UI light",11,'bold'))
            Quantity.place(x=400,y=450)
            Quantity.insert(0,' Quantity')
            Quantity.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Quantity))
            
            Quantity_frame=Frame(main_frame,width=250,height=2,bg="red")
            Quantity_frame.place(x=400,y=480)
            
            
            year_list = [str(year) for year in range(2000, 2023)]
            selected_year = StringVar()
            selected_year.set(year_list[-1])
            
            year_menu=OptionMenu(main_frame,selected_year,*year_list)
            
            
            year_menu.config(highlightbackground="red", highlightcolor="red",fg="black",bg="white", borderwidth=2,width=22)
            year_menu.place(x=765,y=445)
            
            
            Price=Entry(main_frame,fg="black",border=1,bg="white",width=22,font=("Microsoft Yahei UI light",11,'bold'))
            Price.place(x=20,y=600)
            Price.insert(0,' Book Price')
            Price.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Price))
            
            Price_frame=Frame(main_frame,width=250,height=2,bg="red")
            Price_frame.place(x=20,y=630)
            
            
            
            Entre_button_addBook=Button(main_frame,width=30,text="Enter",border=0,bg="blue",cursor="hand2",fg="white",font=("Microsoft Yahei UI light",10,'bold'),command=add_book_database)
            Entre_button_addBook.place(x=375,y=670)
                      
            
            
            
        def del_book_page():
            
            def delete_book_btn_function():
                delete_book_isbn=Delete_book.get()
                if delete_book_isbn=='Enter the ISBN no ':
                    messagebox.showwarning("Error","Please fill the ISBN Entry")
                elif delete_book_isbn=='':
                    messagebox.showwarning("Error","Isbn entry is empty please fill it")
                
                connection=sqlite3.connect("library_sys2.db")
                cursor=connection.cursor()
                
                cursor.execute("Select ISBN from Books_details")
                record_book_isbn=cursor.fetchall()
                
                
                available=False
                not_available=False
                databse=False
                for i in record_book_isbn:
                    print(i[0])
                    
                    if i[0]==delete_book_isbn:
                        available=True
                        break
                    else:
                        not_available=True
                if available==True:
                    messagebox.showinfo("DONE",f"Book with ISBN {delete_book_isbn} has been deleted.")
                    databse=True
                elif not_available==True:
                    messagebox.showinfo("Availability",f"Book with ISBN {delete_book_isbn} is not avaialbe in the database.")
                    databse=False
                if databse==True:
                 cursor.execute("DELETE FROM Books_details WHERE ISBN=?", (delete_book_isbn,))
                
                    
                connection.commit()
                connection.close()
                
                return 
            
            title_frame=Frame(main_frame,bg='Blue',width=1037,height=100)
            disp_title_img=Label(title_frame,text="Delete Books",bg="blue",fg='red',font=('bold',40))
            disp_title_img.place(x=330,y=15)
            title_frame.pack()
            Frame(main_frame,width=1030,height=5,highlightcolor='Black',bg='Black').place(x=0,y=100)
            
            book_show_frame=Frame(main_frame,width=1035,height=450,highlightbackground='red',highlightthickness=2,bg="white")
            book_show_frame.place(x=0,y=104)
            
            my_canvas=Canvas(book_show_frame,width=1000)
            my_canvas.pack(side=LEFT,fill=BOTH,expand=True)
            
            my_scrool_bar=Scrollbar(book_show_frame,orient=VERTICAL,command=my_canvas.yview)
            my_scrool_bar.pack(side=RIGHT,fill=Y)
            
           # scrool_x=Scrollbar(book_show_frame,orient=HORIZONTAL,command=my_canvas.xview)
            #scrool_x.pack(side=BOTTOM,fill=X)
            

            
            my_canvas.configure(yscrollcommand=my_scrool_bar.set)
            my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all")))
            
            
            second_frame=Frame(my_canvas)
            my_canvas.create_window((0,0),window=second_frame,anchor="nw")
            
            connection=sqlite3.connect("library_sys2.db")
            cursor=connection.cursor()
            cursor.execute("Select *from books_details")
            data=cursor.fetchall()
            
            coloum_name=('ISBN_no','Author_id',"publisher_id",'Genre','Quantity','price','book name','Year')
            
            for i,col in enumerate(coloum_name):
                label = Label(second_frame, text=col, font=("Arial", 8, "bold"))
                label.grid(row=0, column=i, padx=2, pady=5)
            
            for row, record in enumerate(data):
              for col, value in enumerate(record):
                 label = Label(second_frame, text=value,font=(6))
                 label.grid(row=row+1, column=col, padx=18, pady=7)
            
            connection.commit()
            connection.close()
            
            Delete_book=Entry(main_frame,fg="black",border=1,bg="white",width=27,font=("Microsoft Yahei UI light",11,'bold'))
            Delete_book.place(x=380,y=500)
            Delete_book.insert(0,"Enter the ISBN no ")
            Delete_book.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Delete_book))
            Frame(main_frame,width=300,height=2,bg="red").place(x=380,y=528)
            Frame(main_frame,width=300,height=2,bg="red").place(x=380,y=500)
            
            
            delete_book_butn=Button(main_frame,width=20,cursor="hand2",border=0,text="Enter",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=delete_book_btn_function)
            delete_book_butn.place(x=420,y=550)
            
            #for thing in range(100):
             #   Button(second_frame,text=f'haha {text}').grid(row=thing,column=0)
  
        
        def Update_book_page():
            
            def book_btn_page():
                
                
                def refresh_page():
                    for frame in book_btn_sub_frame.winfo_children():
                        frame.destroy()
                
                def selected_fun_btn(selected_val,isbn_entry,selected_entry):
                    
                    print(selected_val,isbn_entry,selected_entry)
                    if isbn_entry=="Enter the ISBN no " or (selected_entry=="ISBN (must be unique)"or selected_entry=="Publisher_id" or selected_entry=="Author Id" or selected_entry=="Select Genre" or selected_entry=="Price" or selected_entry=="Book name" or selected_entry=="Year" ):
                        messagebox.showerror("Error","Please fill the all fields")
                        return
                    elif isbn_entry=="" or selected_entry=="":
                        messagebox.showerror("Error","Please fill the fields cant be empty")
                        return
                    
                    access=False
                    connection=sqlite3.connect("library_sys2.db")
                    cursor=connection.cursor()
                    cursor.execute("Select *from books_details")
                    data=cursor.fetchall()
                   
                    
                    
                    for i in data:
                        if i[0]==isbn_entry:
                            access=True
                            break
                        else:
                            access=False
                    
                    if access==False:
                        messagebox.showerror("Error",f"Book having ISBN=>[{isbn_entry}] is not avaialble in dbms")
                    elif access==True:
                        
                        if selected_val=="Publisher_id":
                            cursor.execute("Select *from publisher_details")
                            r=cursor.fetchall()
                            acs=False
                            for kr in r:
                                print(kr)
                                if kr[0]==selected_entry:
                                    acs=True
                                    break
                                else:
                                    acs=False
                            if acs==False:
                                messagebox.showerror("Error","No publisher is present in the publihser table")
                                 
                                 #name_pub_entry=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                                 #name_pub_entry.place(x=350,y=45)
                                 #name_pub_entry.insert(0,"name of publisher ")
                                 #name_pub_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(name_pub_entry))
                                 #Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=350,y=40)
                                 #Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=50)
                                 #name_entry=name_pub_entry.get()
                                 #pub_query="Insert into publisher_details(publisher_id,publisher_name) values(?,?)"
                                 #pub_val=(selected_entry,name_entry)                    
                                 #cursor.execute(pub_query,pub_val)
                                 #cursor.execute("UPDATE Books_details SET publisher_id = ? WHERE ISBN = ?", (selected_entry, isbn_entry,))    
                            elif acs==True:
                                 cursor.execute("UPDATE Books_details SET publisher_id = ? WHERE ISBN = ?", (selected_entry, isbn_entry,))    
                            
                        elif selected_val=="Auhtor_id":
                            cursor.execute("Select *from author_details")
                            r=cursor.fetchall()
                            acs=False
                            for kr in r:
                                print(kr)
                                if kr[0]==selected_entry:
                                    acs=True
                                    break
                                else:
                                    acs=False
                            if acs==True:
                             cursor.execute("UPDATE Books_details SET author_id = ? WHERE ISBN = ?", (selected_entry, isbn_entry,))
                            else:
                                messagebox.showerror("Error","No author is present in the author table")
                            
                        elif selected_val=="Genre":
                            cursor.execute("UPDATE Books_details SET genre = ? WHERE ISBN = ?", (selected_entry, isbn_entry,))
                        elif selected_val=="Qunatity":
                            print("yahe chale ha")
                            cursor.execute("UPDATE Books_details SET quantity = ? WHERE ISBN = ?", (int(selected_entry), isbn_entry,))
                        elif selected_val=="Price":
                            cursor.execute("UPDATE Books_details SET price = ? WHERE ISBN = ?", (int(selected_entry), isbn_entry,))
                        elif selected_val=="Bookname":
                            cursor.execute("UPDATE Books_details SET book_name = ? WHERE ISBN = ?", (selected_entry, isbn_entry,))
                        elif selected_val=="Year":
                            cursor.execute("UPDATE Books_details SET year = ? WHERE ISBN = ?", (selected_entry, isbn_entry,))
                        
                            
                        
                            
                            
                            
                        
                    
                    connection.commit()
                    connection.close()
                    return
                
                def selected_fun():
                    
                    
                    selected_optn=books_select.get()
                    print(selected_optn)
                    
                    if selected_optn=="Select The options":
                      messagebox.showerror("error","Please select from the drop down menu")
                    elif selected_optn!="Select The options" and selected_optn!="":
                        refresh_page()
                        
                        
                        if selected_optn=="ISBN":

                            
                            isbn_book=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                            isbn_book.place(x=250,y=15)
                            isbn_book.insert(0,"Enter the ISBN no ")
                            isbn_book.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_book))
                            Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=15)
                            Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=40)
                            
                            
                            
                            isbn_book_update=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                            isbn_book_update.place(x=570,y=15)
                            isbn_book_update.insert(0,"ISBN (must be unique)")
                            isbn_book_update.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_book_update))
                            Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=15)
                            Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=40)
                            
                            Button(book_btn_sub_frame,width=17,cursor="hand2",border=0,text="Enter",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:selected_fun_btn(selected_optn,isbn_book.get(),isbn_book_update.get())).place(x=423,y=120)
                            
                        
                            
                            
                            
                        elif selected_optn=="Publisher_id":
                            
                           lbl1= Label(book_btn_sub_frame,text="haha 2")
                           lbl1.pack() 
                           
                           isbn_book=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           isbn_book.place(x=250,y=15)
                           isbn_book.insert(0,"Enter the ISBN no ")
                           isbn_book.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_book))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=40)
                            
                            
                            
                           publisher_id_update=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           publisher_id_update.place(x=570,y=15)
                           publisher_id_update.insert(0,"Publisher_id")
                           publisher_id_update.bind("<Button-1>", lambda event:entryclear.clear_ISBN(publisher_id_update))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=40)
                            
                           Button(book_btn_sub_frame,width=17,cursor="hand2",border=0,text="Enter",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:selected_fun_btn(selected_optn,isbn_book.get(),publisher_id_update.get())).place(x=423,y=120)
                        
                        elif selected_optn=="Auhtor_id":
                            
                       
                           
                           isbn_book=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           isbn_book.place(x=250,y=15)
                           isbn_book.insert(0,"Enter the ISBN no ")
                           isbn_book.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_book))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=40)
                            
                            
                            
                           authr_id_update=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           authr_id_update.place(x=570,y=15)
                           authr_id_update.insert(0,"Author Id")
                           authr_id_update.bind("<Button-1>", lambda event:entryclear.clear_ISBN(authr_id_update))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=40)
                            
                           Button(book_btn_sub_frame,width=17,cursor="hand2",border=0,text="Enter",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:selected_fun_btn(selected_optn,isbn_book.get(),authr_id_update.get())).place(x=423,y=120)
                        
                        elif selected_optn=="Genre":
                            
                            
                           isbn_book=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           isbn_book.place(x=250,y=15)
                           isbn_book.insert(0,"Enter the ISBN no ")
                           isbn_book.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_book))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=40)
                           
                           genre_update=StringVar()
                           genre_update.set("Select Genre")
                           genre_dropdown_menu=OptionMenu(book_btn_sub_frame,genre_update,"Mystery Books","Action Adventure book","Notification books"
                                           "Historical Fiction","Horror Novels","Fantacy Novels","Children Books",
                                           "Graphic Novels",)
                           genre_dropdown_menu.config(highlightbackground="red", highlightcolor="red",fg="black",bg="white", borderwidth=2,width=22,height=-1)
                           genre_dropdown_menu.place(x=570,y=15)
                           
                           Button(book_btn_sub_frame,width=17,cursor="hand2",border=0,text="Enter",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:selected_fun_btn(selected_optn,isbn_book.get(),genre_update.get())).place(x=423,y=120)
                           
                           
                            
                        elif selected_optn=="Qunatity":
                            
                           
                           
                           isbn_book=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           isbn_book.place(x=250,y=15)
                           isbn_book.insert(0,"Enter the ISBN no ")
                           isbn_book.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_book))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=40)
                            
                            
                            
                           Quant_update=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           Quant_update.place(x=570,y=15)
                           Quant_update.insert(0,"Quantity")
                           Quant_update.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Quant_update))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=40)
                            
                           Button(book_btn_sub_frame,width=17,cursor="hand2",border=0,text="Enter",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:selected_fun_btn(selected_optn,isbn_book.get(),Quant_update.get())).place(x=423,y=120)
                        
                            
                        elif selected_optn=="Price":
                            
                           
                           isbn_book=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           isbn_book.place(x=250,y=15)
                           isbn_book.insert(0,"Enter the ISBN no ")
                           isbn_book.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_book))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=40)
                            
                            
                            
                           price_update=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           price_update.place(x=570,y=15)
                           price_update.insert(0,"Price")
                           price_update.bind("<Button-1>", lambda event:entryclear.clear_ISBN(price_update))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=40)
                            
                           Button(book_btn_sub_frame,width=17,cursor="hand2",border=0,text="Enter",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:selected_fun_btn(selected_optn,isbn_book.get(),price_update.get())).place(x=423,y=120)
                        
                            
                            
                        elif selected_optn=="Bookname":
                          
                           
                           isbn_book=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           isbn_book.place(x=250,y=15)
                           isbn_book.insert(0,"Enter the ISBN no ")
                           isbn_book.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_book))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=40)
                            
                            
                            
                           Bookname_update=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           Bookname_update.place(x=570,y=15)
                           Bookname_update.insert(0,"Bookname")
                           Bookname_update.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Bookname_update))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=40)
                            
                           Button(book_btn_sub_frame,width=17,cursor="hand2",border=0,text="Enter",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:selected_fun_btn(selected_optn,isbn_book.get(),Bookname_update.get())).place(x=423,y=120)
                        
                            
                        elif selected_optn=="Year":
                            
                           
                           isbn_book=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           isbn_book.place(x=250,y=15)
                           isbn_book.insert(0,"Enter the ISBN no ")
                           isbn_book.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_book))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=250,y=40)
                            
                            
                            
                           Year_update=Entry(book_btn_sub_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                           Year_update.place(x=570,y=15)
                           Year_update.insert(0,"Year")
                           Year_update.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Year_update))
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=15)
                           Frame(book_btn_sub_frame,width=221,height=2,bg="red").place(x=570,y=40)
                            
                           Button(book_btn_sub_frame,width=17,cursor="hand2",border=0,text="Enter",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:selected_fun_btn(selected_optn,isbn_book.get(),Year_update.get())).place(x=423,y=120)
                        
                            
                    
                    
                    
                    
                    
                    return
                
                
                books_show_frame=Frame(btns_frame,highlightbackground='blue',width=1020,height=260,highlightthickness=2,bg="white")
                books_show_frame.place(x=0,y=0)
                
                
                my_canvas=Canvas(books_show_frame,width=1000,height=300)
                my_canvas.pack(side=LEFT,fill=BOTH,expand=True)
            
                my_scrool_bar=Scrollbar(books_show_frame,orient=VERTICAL,command=my_canvas.yview)
                my_scrool_bar.pack(side=RIGHT,fill=Y)
            
           
            

            
                my_canvas.configure(yscrollcommand=my_scrool_bar.set)
                my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all")))
            
            
                second_frame=Frame(my_canvas)
                my_canvas.create_window((0,0),window=second_frame,anchor="nw")
            
                connection=sqlite3.connect("library_sys2.db")
                cursor=connection.cursor()
                cursor.execute("Select *from books_details")
                data=cursor.fetchall()
            
                coloum_name=('ISBN_no','Author_id',"publisher_id",'Genre','Quantity','price','book name','Year')
            
                for i,col in enumerate(coloum_name):
                   label = Label(second_frame, text=col, font=("Arial", 8, "bold"))
                   label.grid(row=0, column=i, padx=2, pady=5)
            
                for row, record in enumerate(data):
                  for col, value in enumerate(record):
                    label = Label(second_frame, text=value,font=(6))
                    label.grid(row=row+1, column=col, padx=18, pady=7)
            
                connection.commit()
                connection.close()
                
                
                books_list = ("Auhtor_id","Publisher_id","Genre","Qunatity","Price","Bookname","Year")
                books_select = StringVar()
                books_select.set("Select The options")
            
                year_menu=OptionMenu(btns_frame,books_select,*books_list)
            
            
                year_menu.config(highlightbackground="red", highlightcolor="red",fg="black",bg="white", borderwidth=2,width=22)
                year_menu.place(x=410,y=310)
                
                
                book_btn_sub_frame=Frame(btns_frame,width=1020,height=200,highlightbackground='white',highlightthickness=2,bg="white")
                book_btn_sub_frame.place(x=2,y=370)
                book_btn_sub_frame.propagate(False)
                
                
                
                
                btn= Button(btns_frame,width=10,cursor="hand2",border=0,text="Enter",bg="white",fg="blue",font=("Microsoft Yahei UI light",11,'bold'),command=selected_fun)
                btn.place(x=650,y=310)
                
                
        
                        
                    
                
                
                
                
                
                return
            
            def author_btn_page():
                
                
                def update_athr():
                    
                    auth_id=auth_id_entry.get()
                    auth_name=auth_name_entry.get()
                    
                    database_acces=False
                    database_acces2=False
                    k=False
                    
                    if (auth_id==''and auth_name=='')or(auth_id=='Enter the Author Id' and auth_name=='Enter the Author Name')or(auth_id=='' and auth_name=='Enter the Author Name')or(auth_id=='Enter the Author Id' and auth_name==''):
                        messagebox.showerror("Error message","Please fill the fileds")
                        k=True
                    elif auth_id!='Enter the Author Id' and auth_name!='Enter the Author Name':
                        database_acces=True
                        
                    
                        
                        
                    
                    
                    if database_acces==True:
                        for i in data:
                            if i[0]==auth_id:
                                print(i)
                                database_acces2=True
                            else:
                                k=False
                               
                    if database_acces2==True:
                        connection=sqlite3.connect("library_sys2.db")
                        cursor=connection.cursor()
                        cursor.execute('UPDATE author_details SET name = ? WHERE author_id = ?', (auth_name, auth_id))
                        messagebox.showinfo("Done",f"Book havind {auth_id} is updated")
                        connection.commit()
                        connection.close()
                    elif k==False:
                        messagebox.showerror("Error",f"Author haivind id {auth_id} is not available in database")  
                        
                    return
                
                def del_autr():
                    
                    auth_id=auth_id_entry.get()
                    
                    access_to_dbs= False
                    
                    if auth_id=='' or auth_id=='Enter the Author Id':
                        messagebox.showerror("Error","Please fiil the auther id")
                    elif auth_id!='' or auth_id!='Enter the Author Id':
                        for i in data:
                            print(i[0])
                            
                            if i[0]==auth_id:
                                 access_to_dbs=True
                                 break
                            else:
                                access_to_dbs=False
                    
                    if access_to_dbs==True:
                        connection=sqlite3.connect("library_sys2.db")
                        cursor=connection.cursor()
                        
                        cursor.execute('Delete from Books_details where  author_id = ?', (auth_id,))
                        cursor.execute('Delete from author_details where  author_id = ?', (auth_id,))
                        messagebox.showinfo("Done",f"Book havind {auth_id} is deleted")
                        connection.commit()
                        connection.close()
                    
                    elif access_to_dbs==False:
                        messagebox.showinfo("Info",f"The author having {auth_id} is unavailable in the database")
                        
                    
                    return
                
                
                
                
                books_show_frame=Frame(btns_frame,highlightbackground='blue',width=1020,height=80,highlightthickness=2,bg="white")
                books_show_frame.pack()
                
               # my_tree=ttk.Treeview(books_show_frame)
                #my_tree['columns']=("ID","Name")
                
                #my_tree.column("#0",width=0,stretch=NO)
                #my_tree.column("ID",anchor=W,minwidth=25)
                #my_tree.column("Name",anchor=CENTER,minwidth=40)
                
                #my_tree.heading("#0",text="",anchor=W)
                #my_tree.heading("ID",text="ID",anchor=W)
                #my_tree.heading("Name",text="Name",anchor=CENTER)
                

                
                connection=sqlite3.connect("library_sys2.db")
                cursor=connection.cursor()
                cursor.execute("Select *from author_details")
                data=cursor.fetchall()
                connection.commit()
                connection.close()
                
                
                #for i in record:
                 #my_tree.insert(parent='', index='end', text="parent",values=(i[0],i[1]))
                 
               # my_tree.pack()
                
                
                my_canvas=Canvas(books_show_frame,width=1000,height=240)
                my_canvas.pack(side=LEFT,fill=BOTH,expand=TRUE)
            
                my_scrool_bar=Scrollbar(books_show_frame,orient=VERTICAL,command=my_canvas.yview)
                my_scrool_bar.pack(side=RIGHT,fill=Y)
                
                my_scrool_bar_x = Scrollbar(books_show_frame, orient=HORIZONTAL, command=my_canvas.xview)
                my_scrool_bar_x.pack(side=BOTTOM, fill=X)
            
      
            

            
                my_canvas.config(yscrollcommand=my_scrool_bar.set)
                my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all")))
                
                
                second_frame=Frame(my_canvas)
                my_canvas.create_window((0,0),window=second_frame,anchor="nw")
                
                colum_name=("ID","Auhtor name")
                
                for i,col in enumerate(colum_name):
                     label = Label(second_frame, text=col, font=("Arial", 8, "bold"))
                     label.grid(row=0, column=i+5, padx=2, pady=5)
                     
                for row, record in enumerate(data):
                  for col, value in enumerate(record):
                     label = Label(second_frame, text=value,font=(6))
                     label.grid(row=row+1, column=col+5, padx=18, pady=7)
                
                
                auth_id_entry=Entry(btns_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                auth_id_entry.place(x=150,y=340)
                auth_id_entry.insert(0,"Enter the Author Id")
                auth_id_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(auth_id_entry))
                Frame(btns_frame,width=223,height=2,bg="red").place(x=150,y=368)
                Frame(btns_frame,width=223,height=2,bg="red").place(x=150,y=340)
                
                
                
                
                
                auth_name_entry=Entry(btns_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                auth_name_entry.place(x=600,y=340)
                auth_name_entry.insert(0,"Enter the Author Name")
                auth_name_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(auth_name_entry))
                Frame(btns_frame,width=223,height=2,bg="red").place(x=600,y=368)
                Frame(btns_frame,width=223,height=2,bg="red").place(x=600,y=340)
                
                
                update_bt=Button(btns_frame,width=15,cursor="hand2",border=0,text="Update",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=update_athr)
                update_bt.place(x=340,y=470)
                
                del_btn=Button(btns_frame,width=15,cursor="hand2",border=0,text="Delete",bg="Red",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=del_autr)
                del_btn.place(x=500,y=470)
                
            

                
                return
            
            def publisher_btn_page():
                
                
                def update_athr():
                    
                    pub_id=auth_id_entry.get()
                    pub_name=auth_name_entry.get()
                    
                    database_acces=False
                    database_acces2=False
                    k=False
                    
                    if (pub_id==''and pub_name=='')or(pub_id=='Enter the Publisher Id' and pub_name=='Enter the Publisher Name')or(pub_id=='' and pub_name=='Enter the Publisher Name')or(pub_id=='Enter the Publisher Id' and pub_name==''):
                        messagebox.showerror("Error message","Please fill the fileds")
                        k=True
                    elif pub_id!='Enter the Publisher Id' and pub_name!='Enter the Publisher Name':
                        database_acces=True
                        
                    
                        
                        
                    
                    
                    if database_acces==True:
                        for i in data:
                            if i[0]==pub_id:
                                print(i)
                                database_acces2=True
                            else:
                                k=False
                               
                    if database_acces2==True:
                        connection=sqlite3.connect("library_sys2.db")
                        cursor=connection.cursor()
                        cursor.execute('UPDATE publisher_details SET publisher_name = ? WHERE publisher_id = ?', (pub_name, pub_id))
                        messagebox.showinfo("Done",f"Book havind {pub_id} is updated")
                        connection.commit()
                        connection.close()
                    elif k==False:
                        messagebox.showerror("Error",f"Publisher haivind id {pub_id} is not available in database")  
                        
                    return
                
                
                def del_autr():
                    
                    pub_id=auth_id_entry.get()
                    
                    access_to_dbs= False
                    
                    if pub_id=='' or pub_id=='Enter the Publisher Id':
                        messagebox.showerror("Error","Please fiil the publisher id")
                    elif pub_id!='' or pub_id!='Enter the Publisher Id':
                        for i in data:
                            print(i[0])
                            
                            if i[0]==pub_id:
                                 access_to_dbs=True
                                 break
                            else:
                                access_to_dbs=False
                    
                    if access_to_dbs==True:
                        connection=sqlite3.connect("library_sys2.db")
                        cursor=connection.cursor()
                        
                        cursor.execute('Delete from Books_details where  publisher_id = ?', (pub_id,))
                        cursor.execute('Delete from publisher_details where  publisher_id = ?', (pub_id,))
                        messagebox.showinfo("Done",f"Publisher having {pub_id} is deleted")
                        connection.commit()
                        connection.close()
                    
                    elif access_to_dbs==False:
                        messagebox.showinfo("Info",f"The publisher having {pub_id} is unavailable in the database")
                        
                    
                    return
                
                
                
                books_show_frame=Frame(btns_frame,highlightbackground='blue',width=1020,height=280,highlightthickness=2,bg="white")
                books_show_frame.place(x=0,y=0)
                
                
                connection=sqlite3.connect("library_sys2.db")
                cursor=connection.cursor()
                cursor.execute("Select *from publisher_details")
                data=cursor.fetchall()
                connection.commit()
                connection.close()
                
                
                my_canvas=Canvas(books_show_frame,width=1000,height=240)
                my_canvas.pack(side=LEFT,fill=BOTH,expand=TRUE)
            
                my_scrool_bar=Scrollbar(books_show_frame,orient=VERTICAL,command=my_canvas.yview)
                my_scrool_bar.pack(side=RIGHT,fill=Y)
                
               
            
      
            

            
                my_canvas.config(yscrollcommand=my_scrool_bar.set)
                my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all")))
                
                
                second_frame=Frame(my_canvas)
                my_canvas.create_window((0,0),window=second_frame,anchor="nw")
                
                colum_name=("ID","Publisher name")
                
                for i,col in enumerate(colum_name):
                     label = Label(second_frame, text=col, font=("Arial", 8, "bold"))
                     label.grid(row=0, column=i+5, padx=2, pady=5)
                     
                for row, record in enumerate(data):
                  for col, value in enumerate(record):
                     label = Label(second_frame, text=value,font=(6))
                     label.grid(row=row+1, column=col+5, padx=18, pady=7)
                
                
                auth_id_entry=Entry(btns_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                auth_id_entry.place(x=150,y=340)
                auth_id_entry.insert(0,"Enter the Publisher Id")
                auth_id_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(auth_id_entry))
                Frame(btns_frame,width=223,height=2,bg="red").place(x=150,y=368)
                Frame(btns_frame,width=223,height=2,bg="red").place(x=150,y=340)
                
                
                
                
                
                auth_name_entry=Entry(btns_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
                auth_name_entry.place(x=600,y=340)
                auth_name_entry.insert(0,"Enter the Publisher Name")
                auth_name_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(auth_name_entry))
                Frame(btns_frame,width=223,height=2,bg="red").place(x=600,y=368)
                Frame(btns_frame,width=223,height=2,bg="red").place(x=600,y=340)
                
                
                update_bt=Button(btns_frame,width=15,cursor="hand2",border=0,text="Update",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=update_athr)
                update_bt.place(x=340,y=470)
                
                del_btn=Button(btns_frame,width=15,cursor="hand2",border=0,text="Delete",bg="Red",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=del_autr)
                del_btn.place(x=500,y=470)
                
            
                
                
                
                return
        
            
            def  hide_update_btn_indicator():
                book_table_btn_indicator.config(bg="white")
                Author_table_indicator.config(bg="white")
                pub_table_indicator.config(bg="white")
            
            def delete_pages_update():
              for frame in btns_frame.winfo_children():
                frame.destroy()
                
            def update_btns_indicator(obj,page):
                hide_update_btn_indicator()
                obj.configure(bg="black")
                delete_pages_update()
                page()
                
                
            title_frame=Frame(main_frame,bg='Blue',width=1037,height=100)
            disp_title_img=Label(title_frame,text="Update Books",bg="blue",fg='red',font=('bold',40))
            disp_title_img.place(x=330,y=15)
            title_frame.pack()
            Frame(main_frame,width=1035,height=5,highlightcolor='Black',bg='Black').place(x=0,y=100)
            
            
            update_but_frame=Frame(main_frame,width=1035,height=642,highlightbackground='black',highlightthickness=2,bg="white")
            update_but_frame.place(x=0,y=104)
            
            book_table_btn=Button(update_but_frame,width=20,cursor="hand2",border=0,text="Books",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:update_btns_indicator(book_table_btn_indicator,book_btn_page))
            book_table_btn.place(x=0,y=0)           
            book_table_btn_indicator=Frame(update_but_frame,bg="white",height=3,width=150)
            book_table_btn_indicator.place(x=36,y=40)
            
            
            Author_table_btn=Button(update_but_frame,width=20,cursor="hand2",border=0,text="Auhtors",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:update_btns_indicator(Author_table_indicator,author_btn_page))
            Author_table_btn.place(x=400,y=0)
            Author_table_indicator=Frame(update_but_frame,bg="white",height=3,width=150)
            Author_table_indicator.place(x=438,y=40)
            
            
            publisher_table_btn=Button(update_but_frame,width=20,cursor="hand2",border=0,text="Publishers",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:update_btns_indicator(pub_table_indicator,publisher_btn_page))
            publisher_table_btn.place(x=805,y=0)
            pub_table_indicator=Frame(update_but_frame,bg="white",height=3,width=150)
            pub_table_indicator.place(x=850,y=40)
            
            btns_frame=Frame(update_but_frame,width=1024,height=580,highlightbackground='white',highlightthickness=2,bg="white")
            btns_frame.place(x=1,y=50)
            btns_frame.propagate(False)
            
            
        def see_orders_page():
            
            
            
            def all_order_fun():
                #Label(see_orders_frame,text="1").pack()
                
                
                def on_canvas_configure(event):
                 canvas.configure(scrollregion=canvas.bbox("all"))

                canva_frame=Frame(see_orders_frame,width=1020,height=280)
                canva_frame.pack()
                
                x_scrollbar = Scrollbar(canva_frame, orient=HORIZONTAL)
                x_scrollbar.pack(side=BOTTOM, fill=X)

                
                y_scrollbar = Scrollbar(canva_frame)
                y_scrollbar.pack(side=RIGHT, fill=Y)


                canvas = Canvas(canva_frame, xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set,width=1020,height=350)
                canvas.pack(side=LEFT, fill=BOTH, expand=True)


                x_scrollbar.config(command=canvas.xview)
                y_scrollbar.config(command=canvas.yview)


                canvas.bind("<Configure>", on_canvas_configure)


                frame = Frame(canvas,width=1020,height=350)
                canvas.create_window((0, 0), window=frame, anchor="nw")
                
                
                
               # for i in range(50):
                #   Label(frame, text=f"Label {i+1}").grid(row=i, column=i)
                
                colum_name=("Order-Id","Customer-id","First-name","Last_name","ISBN","Bookname","address","quantity","Ph-No","Time","Status")
                
                for i,col in enumerate(colum_name):
                     label = Label(frame, text=col, font=("Arial", 8, "bold"))
                     label.grid(row=0, column=i+5, padx=2, pady=5)
                
                 
                connection=sqlite3.connect("library_sys2.db")
                cursor=connection.cursor() 
                cursor.execute("select o.order_id,o.Customer_id,c.First_name,c.Last_name,o.ISBN,b.book_name,o.address,o.quantity,o.mobile_no,o.time,o.status from orders o,Customer_details c,Books_details b where o.ISBN=b.ISBN and o.Customer_id=c.Customer_Id")
                data=cursor.fetchall()
                
                
                
                for row, record in enumerate(data):
                  for col, value in enumerate(record):
                     label = Label(frame, text=value,font=(6))
                     label.grid(row=row+1, column=col+5, padx=18, pady=7)
                
                
                return
            
            
            def deliver_order_fun():
                
                def on_canvas_configure(event):
                 canvas.configure(scrollregion=canvas.bbox("all"))

                canva_frame=Frame(see_orders_frame,width=1020,height=280)
                canva_frame.pack()
                
                x_scrollbar = Scrollbar(canva_frame, orient=HORIZONTAL)
                x_scrollbar.pack(side=BOTTOM, fill=X)

                
                y_scrollbar = Scrollbar(canva_frame)
                y_scrollbar.pack(side=RIGHT, fill=Y)


                canvas = Canvas(canva_frame, xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set,width=1020,height=350)
                canvas.pack(side=LEFT, fill=BOTH, expand=True)


                x_scrollbar.config(command=canvas.xview)
                y_scrollbar.config(command=canvas.yview)


                canvas.bind("<Configure>", on_canvas_configure)


                frame = Frame(canvas,width=1020,height=350)
                canvas.create_window((0, 0), window=frame, anchor="nw")
                
                
                
               # for i in range(50):
                #   Label(frame, text=f"Label {i+1}").grid(row=i, column=i)
                
                colum_name=("Order-Id","Customer-id","First-name","Last_name","ISBN","Bookname","address","quantity","Ph-No","Time","Status")
                
                for i,col in enumerate(colum_name):
                     label = Label(frame, text=col, font=("Arial", 8, "bold"))
                     label.grid(row=0, column=i+5, padx=2, pady=5)
                
                 
                connection=sqlite3.connect("library_sys2.db")
                cursor=connection.cursor() 
                cursor.execute("select o.order_id,o.Customer_id,c.First_name,c.Last_name,o.ISBN,b.book_name,o.address,o.quantity,o.mobile_no,o.time,o.status from orders o,Customer_details c,Books_details b where o.ISBN=b.ISBN and o.Customer_id=c.Customer_Id and o.status='Deliverd'")
                data=cursor.fetchall()
                
                
                
                for row, record in enumerate(data):
                  for col, value in enumerate(record):
                     label = Label(frame, text=value,font=(6))
                     label.grid(row=row+1, column=col+5, padx=18, pady=7)
                
                return
            
            def pending_order_fun():
                def on_canvas_configure(event):
                 canvas.configure(scrollregion=canvas.bbox("all"))

                canva_frame=Frame(see_orders_frame,width=1020,height=280)
                canva_frame.pack()
                
                x_scrollbar = Scrollbar(canva_frame, orient=HORIZONTAL)
                x_scrollbar.pack(side=BOTTOM, fill=X)

                
                y_scrollbar = Scrollbar(canva_frame)
                y_scrollbar.pack(side=RIGHT, fill=Y)


                canvas = Canvas(canva_frame, xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set,width=1020,height=350)
                canvas.pack(side=LEFT, fill=BOTH, expand=True)


                x_scrollbar.config(command=canvas.xview)
                y_scrollbar.config(command=canvas.yview)


                canvas.bind("<Configure>", on_canvas_configure)


                frame = Frame(canvas,width=1020,height=350)
                canvas.create_window((0, 0), window=frame, anchor="nw")
                
                
                
               # for i in range(50):
                #   Label(frame, text=f"Label {i+1}").grid(row=i, column=i)
                
                colum_name=("Order-Id","Customer-id","First-name","Last_name","ISBN","Bookname","address","quantity","Ph-No","Time","Status")
                
                for i,col in enumerate(colum_name):
                     label = Label(frame, text=col, font=("Arial", 8, "bold"))
                     label.grid(row=0, column=i+5, padx=2, pady=5)
                
                 
                connection=sqlite3.connect("library_sys2.db")
                cursor=connection.cursor() 
                cursor.execute("select o.order_id,o.Customer_id,c.First_name,c.Last_name,o.ISBN,b.book_name,o.address,o.quantity,o.mobile_no,o.time,o.status from orders o,Customer_details c,Books_details b where o.ISBN=b.ISBN and o.Customer_id=c.Customer_Id and o.status is NULL")
                data=cursor.fetchall()
                
                
                
                for row, record in enumerate(data):
                  for col, value in enumerate(record):
                     label = Label(frame, text=value,font=(6))
                     label.grid(row=row+1, column=col+5, padx=18, pady=7)
                return
            
            
            def hide_order_indicators():
                all_order_bt_indicator.config(bg="white")
                deliverd_order_btn_indicator.config(bg="white")
                pending_order_btn_indicator.config(bg="white")
            
            def del_order_btn_page():
                for frame in see_orders_frame.winfo_children():
                    frame.destroy()
                    
            def hide_ind_and_switch_page(obj,page):
                hide_order_indicators()
                obj.config(bg="black")
                del_order_btn_page()
                page()
                
                
            title_frame=Frame(main_frame,bg='Blue',width=1037,height=100)
            disp_title_img=Label(title_frame,text="See Orders",bg="blue",fg='red',font=('bold',40))
            disp_title_img.place(x=370,y=15)
            title_frame.pack()
            
            all_order_bt=Button(main_frame,width=20,cursor="hand2",border=0,text="All Orders",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:hide_ind_and_switch_page(all_order_bt_indicator,all_order_fun))
            all_order_bt.place(x=0,y=105)
            all_order_bt_indicator=Frame(main_frame,bg="white",height=3,width=150)
            all_order_bt_indicator.place(x=34,y=146)
            
            
            deliverd_order_btn=Button(main_frame,width=20,cursor="hand2",border=0,text="Delivered",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:hide_ind_and_switch_page(deliverd_order_btn_indicator,deliver_order_fun))
            deliverd_order_btn.place(x=400,y=105)
            deliverd_order_btn_indicator=Frame(main_frame,bg="white",height=3,width=150)
            deliverd_order_btn_indicator.place(x=437,y=146)
            
            pending_order_btn=Button(main_frame,width=20,cursor="hand2",border=0,text="Pending",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:hide_ind_and_switch_page(pending_order_btn_indicator,pending_order_fun))
            pending_order_btn.place(x=806,y=105)
            pending_order_btn_indicator=Frame(main_frame,bg="white",height=3,width=150)
            pending_order_btn_indicator.place(x=847,y=146)
            
            see_orders_frame=Frame(main_frame,bg='white',highlightbackground='Black',highlightthickness=2,width=1030,height=580)
            see_orders_frame.place(x=0,y=160)
            see_orders_frame.propagate(False)
            
            Frame(main_frame,width=1035,height=5,highlightcolor='Black',bg='Black').place(x=0,y=100)
        
        def sales_page():
            title_frame=Frame(main_frame,bg='Blue',width=1037,height=100)
            disp_title_img=Label(title_frame,text="Sales",bg="blue",fg='red',font=('bold',40))
            disp_title_img.place(x=450,y=15)
            title_frame.pack()
            Frame(main_frame,width=1035,height=5,highlightcolor='Black',bg='Black').place(x=0,y=100)
            
        def hide_indicators():
            but1_indicator.config(bg="blue")
            add_book_indicator.config(bg="blue")
            del_book_indicator.config(bg="blue")
            Update_book_indicator.config(bg="blue")
            see_orders_indicator.config(bg="blue")
            sales_butt_indicator.config(bg="blue")
            
        def delete_pages():
            for frame in main_frame.winfo_children():
                frame.destroy()
        
        def button_indicator(obj,page):
            hide_indicators()
            obj.configure(bg="red")
            delete_pages()
            page()
            
            
        ## figma import
        admin_screen2=Toplevel(root)
        admin_screen2.geometry("1300x750")
        admin_screen2.configure(bg="white")
        admin_screen2.resizable(FALSE,FALSE)
        admin_screen2.title("ADMIN PORTAL")
        
        side_frame=Frame(admin_screen2,width=270,height=750,bg="Blue")
        side_frame.grid(row=0,column=0)
        
        admin_label=Label(side_frame,text="ADMIN",bg="Blue",fg="white",font=("Microsoft Yahei UI light",18,'bold'))
        admin_label.place(x=76,y=10)
        
       
        def update_time():        
         current_datetime = datetime.datetime.now()

    
         day_name = current_datetime.strftime("%A")

    
         time_with_seconds = current_datetime.strftime("%H:%M:%S")

    
         day_label.config(text=day_name + "  "+time_with_seconds)

    
         side_frame.after(1000, update_time)

        
        
       
        
        day_label= Label(side_frame,bg="blue",fg="white",font=("Microsoft Yahei UI light",10,'bold'))
        day_label.place(x=50,y=54)
        
        update_time()
       
            
        
            
            
        
        
        
        logout_button=Button(side_frame,text='LOGOUT',fg="white",bg="blue",cursor="hand2",border=0,font=("Microsoft Yahei UI light",15,'bold'),command=back_from_admin)
        logout_button.place(x=70,y=700)
        but1_image=ImageTk.PhotoImage(file='Assets/Group 6.png')
        but1_fun=Button(side_frame,bg="blue",highlightthickness = 0,border=0,borderwidth=0,image=but1_image,relief='sunken',command=lambda:button_indicator(but1_indicator,Stock_page))
        but1_fun.place(x=10,y=100)
        
        but1_indicator=Frame(side_frame,bg="blue",height=2,width=220)
        but1_indicator.place(x=23,y=150)
        
        add_book_butt=ImageTk.PhotoImage(file='Assets/Group 1 (5).png')
        add_book_fun=Button(side_frame,bg="blue",highlightthickness = 0,borderwidth=0,image=add_book_butt,relief='sunken',command=lambda:button_indicator(add_book_indicator,add_book_page))
        add_book_fun.place(x=10,y=200)
        
        add_book_indicator=Frame(side_frame,bg="blue",height=2,width=220)
        add_book_indicator.place(x=23,y=250)
        
        #C:\Users\user\Downloads\Group 2.png
        
        del_book_butt=ImageTk.PhotoImage(file='Assets/Group 2.png')
        del_book_fun=Button(side_frame,bg="blue",highlightthickness = 0,borderwidth=0,image=del_book_butt,relief='sunken',command=lambda:button_indicator(del_book_indicator,del_book_page))
        del_book_fun.place(x=10,y=300)
        
        del_book_indicator=Frame(side_frame,bg="blue",height=2,width=220)
        del_book_indicator.place(x=23,y=350)
        
        
        Update_book_butt=ImageTk.PhotoImage(file='Assets/Group 3.png')
        Update_book_fun=Button(side_frame,bg="blue",highlightthickness = 0,borderwidth=0,image=Update_book_butt,relief='sunken',command=lambda:button_indicator(Update_book_indicator,Update_book_page))
        Update_book_fun.place(x=10,y=400)
        
        Update_book_indicator=Frame(side_frame,bg="blue",height=2,width=220)
        Update_book_indicator.place(x=23,y=450)
        
        see_orders_butt=ImageTk.PhotoImage(file='Assets/Group 4.png')
        see_orders_fun=Button(side_frame,bg="blue",highlightthickness = 0,borderwidth=0,image=see_orders_butt,relief='sunken',command=lambda:button_indicator(see_orders_indicator,see_orders_page))
        see_orders_fun.place(x=10,y=500)
        
        see_orders_indicator=Frame(side_frame,bg="blue",height=2,width=220)
        see_orders_indicator.place(x=23,y=550)
        
        
        sales_butt=ImageTk.PhotoImage(file='Assets/Group 5.png')
        sales_butt_fun=Button(side_frame,bg="blue",highlightthickness = 0,borderwidth=0,image=sales_butt,relief='sunken',command=lambda:button_indicator(sales_butt_indicator,sales_page))
        sales_butt_fun.place(x=10,y=600)
        
        sales_butt_indicator=Frame(side_frame,bg="blue",height=2,width=220)
        sales_butt_indicator.place(x=23,y=650)
        
        main_frame=Frame(admin_screen2,width=1037,height=750,bg='white',highlightbackground='Black',highlightthickness=2)
        main_frame.propagate(False)
        main_frame.place(x=260,y=0)
        
        
        
        admin_screen2.mainloop()
        return
    
    
    def Check_pass():
        pas_check=admin_user.get()
        
        if pas_check=='1234':
            messagebox.showinfo('SussesFully','Welcome to the admin portal')
            admin_screen.destroy()
            admin_portal_orignal()
        elif pas_check!='1234':
            
            messagebox.showerror("Invalid","Invalid Pass")
           
        return 
      
    k=0
    admin_screen=Toplevel(root)
    admin_screen.geometry("1100x500+300+200")
    admin_screen.title("ADMIN PORTAL")
    admin_screen.resizable(FALSE,FALSE)
    admin_screen.configure(bg="white")
    
    text=Label(admin_screen, text="Enter the Credentials",bg="white",fg="blue",font=("Microsoft Yahei UI light",25,'bold'))
    text.place(x=350,y=10)
    
    lock_img=ImageTk.PhotoImage(file="Assets/pngtree-lock-icon-for-your-project-png-image_5239757.jpg")
    Label(admin_screen,image=lock_img,bg="white").place(x=440,y=60)
    
    admin_user=Entry(admin_screen,width=40,border=0,fg="black")
    admin_user.place(x=380,y=300)
    admin_user.insert(0,"PASSWORD")
    admin_user.bind("<Button-1>",lambda event:entryclear.clear_ISBN(admin_user))
    Frame(admin_screen,width=350,height=2,bg="black").place(x=380,y=320)
    
    Enter_Button=Button(admin_screen,text="Enter",width=12,fg="white",bg="Blue",font=('Microsoft Yahei UI light)',10,'bold'),command=lambda:Check_pass())
    Enter_Button.place(x=450,y=350)
    
    temp_but=Button(admin_screen,text="click",width=10,command=lambda:back_menu_button())
    temp_but.grid(row=0,column=1)
    
    
    
    
    
    
    
    
    
    
    
    
    admin_screen.mainloop()
    
    
    
    
    
    return
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

##############################################   USER~~~~~~~~~~~~~~~~~~~~###################################
def user_portal():
    def get_mainportal():
        user_screen.destroy()
        signin_screen()       
        return
    
    
    def user_account():
        def user_page():  #### back button
            user_registration_screeen.destroy()
            user_portal()
            return
        
        def check_pass_add_databse():
            
            #Customer_ID, first_name, last_name, email, phone, 
            
            F_name=First_name.get()
            L_name=last_name.get()
            Email=email.get()
            ph_no=phone_no.get()
            selected_gender = gender_var.get()
            
            database_access=FALSE
            if F_name=="" and L_name=="" and Email=="" and ph_no=="" and selected_gender=="":
               messagebox.showerror("FIELDS","Please Fill the all entries")
            elif (F_name=="First name") and (L_name=="Last name") and (Email=="Email") and (ph_no=="phone NO") and selected_gender=="": 
                messagebox.showinfo("FIELDS","Please Fill the all entries")
            elif F_name=="" or L_name=="" or Email=="" or ph_no=="" or selected_gender=="":
               messagebox.showerror("FIELDS","Please Fill the all entries")
            elif F_name!="" and L_name!="" and Email!="" and ph_no!="" and selected_gender!="":
                database_access=True
            
            
            if database_access==True:
                email_acces=True
                empty_rec=False
                def generate_customer_id(prefix, length):
                   random_digits = ''.join(random.choices(string.digits, k=length))
                   return prefix + random_digits
                
                connection=sqlite3.connect("library_sys2.db")
                cursor=connection.cursor()
                cursor.execute("Select  *from Customer_details")
                data=cursor.fetchall()
                #print(data)
                if data==[]:
                    empty_rec=True
                    print("record is empty")
                if data!=[]:
                 print("data is not empty")   
                  
                 for record in data:
                  print(record[3])
                  if record[3]==Email:
                     print(record[3])
                      
                     messagebox.showwarning("ALREADY CREATED","Your account is already created")
                     email_acces=True
                     break
               
                  else:
                     email_acces=False
                
                if email_acces==False or empty_rec==True:
                   cust_id=generate_customer_id('Cust-',3)
                   values=values=(cust_id,F_name,L_name,Email,ph_no,selected_gender)
                   queryy="Insert into Customer_details(Customer_Id,First_name,Last_name,email,phone_no,gender) values(?,?,?,?,?,?)"
                   cursor.execute(queryy,values)
                   messagebox.showinfo("DONE","Account is created")
                
              
                connection.commit()
                connection.close()
            
         
            
            return
        
     
        
        ###  THIS FUNCTION DEAL WITH JUST CUSTOMER UPDATE DELETE AND OTHER OPEARTIONS ###############
        user_screen.destroy()
        user_registration_screeen=Toplevel(root)
        user_registration_screeen.title("CUSTOMER REGISTRATION")
        #user_registration_screeen.geometry("700x500")
        user_registration_screeen.config(bg="white")
        Label(user_registration_screeen,text="Registration",fg="Black",bg="white",font=('Microsoft Yahei UI light)',20,'bold')).place(x=0,y=5)
        Frame(user_registration_screeen,bg="#FFBF00",width=40,height=5).place(x=1,y=47)
        
       
        
        
        
        image1=ImageTk.PhotoImage(file="Assets/bg2.jpg")
    
        Label(user_registration_screeen,image=image1,bg="white").grid(row=0,column=0)
     #creating signup frame text in it
    

        heading=Label(user_registration_screeen, text="Sign up", fg="#C71585", bg="white", font=("Microsoft Yahei UI light",28,'bold'))
        heading.place(x=700,y=110)
    
        First_name=Entry(user_registration_screeen,fg="black",border=0,highlightcolor="red",highlightbackground="blue",highlightthickness=0,width=10,font=("Microsoft Yahei UI light",11,'bold'))
        First_name.place(x=640,y=230)
        First_name.insert(0,"First name")
    
    
        Frame(user_registration_screeen,width=100,height=2,bg="#FF1493").place(x=640,y=260)
        First_name.bind("<Button-1>",lambda event:entryclear.clear_ISBN(First_name))
    
        last_name=Entry(user_registration_screeen,fg="black",border=0,width=11,font=("Microsoft Yahei UI light",11,'bold'))
        last_name.place(x=820,y=230)
        last_name.insert(0,"Last name")
    
    
        Frame(user_registration_screeen,width=100,height=2,bg="#FF1493").place(x=820,y=260)
        last_name.bind("<Button-1>",lambda event:entryclear.clear_ISBN(last_name))
    
        email=Entry(user_registration_screeen,fg="black",border=0,width=24,font=("Microsoft Yahei UI light",11,'bold'))
        email.place(x=640,y=300)
        email.insert(0,"Email")
    
    
        Frame(user_registration_screeen,width=280,height=2,bg="#FF1493").place(x=640,y=328)
        email.bind("<Button-1>",lambda event:entryclear.clear_ISBN(email))
    
        phone_no=Entry(user_registration_screeen,fg="black",border=0,width=20,font=("Microsoft Yahei UI light",11,'bold'))
        phone_no.place(x=640,y=365)
        phone_no.insert(0,"phone NO")
    
        Frame(user_registration_screeen,width=280,height=2,bg="#FF1493").place(x=640,y=392)
        phone_no.bind("<Button-1>",lambda event:entryclear.clear_ISBN(phone_no))
        
        Label(user_registration_screeen,text="Gender",bg="white",font=("Microsoft Yahei UI light",11,'bold')).place(x=640,y=420)
        
      

        
        gender_var=StringVar()
        options = [("Male", "Male"), ("Female", "Female"), ("Rather Not Say", "Rather Not Say")]
       
        itr=0
        for text, value in options:
           checkbox = Checkbutton(user_registration_screeen,bg="white", text=text, variable=gender_var, onvalue=value, offvalue="")
           checkbox.place(x=640+itr,y=455)
           
           itr=itr+75
        
        back_img=ImageTk.PhotoImage(file="Assets/left-arrow.png")
        back_butt=Button(user_registration_screeen,image=back_img,border=0,bg="#FF3366",command=user_page)
        back_butt.place(x=5,y=3)
       
        
      
        
        
    
        
    
        register=Button(user_registration_screeen, text="Register", width=24, pady=4, bg="#FF1493",fg="White",font=("Microsoft Yahei UI light",9,'bold'),command=check_pass_add_databse)
        register.place(x=655,y=515)
    
    
    
    
    
    
        user_registration_screeen.mainloop()
        return
    
    def cart_order_place():
        
        def main_portal():
            cart_screen.destroy()
            user_portal()
            return
        
        
        def place_order_databse():
            
            name=name_entry.get()
            email_add=email_entry.get()
            address=address_entry.get()
            isbn=Isbn_entry.get()
            quant_book=quantity_entry.get()
            db=False
            if name=="" and email_add=="" and address=="" and isbn=="" and quant_book=="0":
                messagebox.showerror("Error","Please fill all the fileds")
                
            elif name!="" and email_add!="" and address!="" and isbn!="" and quant_book=="0":
                messagebox.showinfo("Attention","Please select the quantity")
                
            elif name!="" and email_add!="" and address!="" and isbn!="" and quant_book!="0":
                db=True
                
            if db==True:
             databse_accs=False
             connection=sqlite3.connect("library_sys2.db")
             cursor=connection.cursor()
             cursor.execute("select *from Customer_details")
             data=cursor.fetchall()
             cursor.execute("select quantity from Books_details where ISBN=?",(isbn,))
             quantity_database=cursor.fetchone()
             print(quantity_database)
             cursor.execute("select price from Books_details where ISBN=?",(isbn,))
             price_b=cursor.fetchone()
             print(price_b)
             for record in data:
                print(record)
                
                if record[3]==email_add:
                 custer_id=record[0]
                 phone_no=record[4]
                 databse_accs=True
                 break
                else:
                    databse_accs=False
            
            def generate_order_id(prefix, length):
                   random_digits = ''.join(random.choices(string.digits, k=length))
                   return prefix + random_digits
            databse_accs2=True   
            if databse_accs==True:
              if quantity_database[0]<int(quant_book):
                 messagebox.showwarning("AVAILABILITY",f"OUT OF STOCK total {quantity_database[0]} are avaliable")
                 databse_accs2=False
              
              if databse_accs2==True:
                total_price=int(price_b[0])* int(quant_book)
                order_id=generate_order_id('Oid-',3)
                current_time = datetime.datetime.now()
                values=(order_id,isbn,custer_id,address,quant_book,phone_no,current_time)
                query="Insert into orders(order_id,ISBN,Customer_id,address,quantity,mobile_no,time) values(?,?,?,?,?,?,?)"
              
                cursor.execute(query,values)
                messagebox.showinfo("DONE",f"YOUR order has been placed \n 1. orderID->{order_id} \n 2. TOTOAL PRICE->{total_price}")
                
                connection.commit()
                connection.close()
                cart_screen.destroy()         
            
            if databse_accs==False:
                messagebox.showwarning("ACCOUNT","Please create your account first")
                connection.commit()
                connection.close()
                 
            
                
            #print(custer_id,phone_no)
            
            return
        
        
        
        
        cart_screen=Toplevel(root)
        cart_screen.title("PLACE THE ORDER")
        cart_screen.geometry("500x700+650+100")
        cart_screen.config(bg="white")
        
        image_header=ImageTk.PhotoImage(file="Assets/Group 1 (6).png")
        img_label=Label(cart_screen,image=image_header)
        img_label.place(x=-2,y=0)
        
        
        name_label=Label(cart_screen,text="Name",bg="white",fg="black",font=('Microsoft Yahei UI light)',15))
        name_label.place(x=10,y=120)
        
        name_entry=Entry(cart_screen,width=29,bg="white",highlightthickness=2,borderwidth=1,font=("Helvetica", 13))
        name_entry.place(x=14,y=150)
        
        
        
        email_label=Label(cart_screen,text="Email",bg="white",fg="black",font=('Microsoft Yahei UI light)',15))
        email_label.place(x=10,y=200)
        
        email_entry=Entry(cart_screen,width=29,bg="white",highlightthickness=2,borderwidth=1,font=("Helvetica", 13))
        email_entry.place(x=14,y=230)
        
        
        
        address_label=Label(cart_screen,text="Address",bg="white",fg="black",font=('Microsoft Yahei UI light)',15))
        address_label.place(x=10,y=280)
        
        address_entry=Entry(cart_screen,width=29,bg="white",highlightthickness=2,borderwidth=1,font=("Helvetica", 13))
        address_entry.place(x=14,y=315)
        
        
        
        Isbn_label=Label(cart_screen,text="ISBN",bg="white",fg="black",font=('Microsoft Yahei UI light)',15))
        Isbn_label.place(x=10,y=370)
        
        Isbn_entry=Entry(cart_screen,width=29,bg="white",highlightthickness=2,borderwidth=1,font=("Helvetica", 13))
        Isbn_entry.place(x=14,y=400)
        
        
        quantity_label=Label(cart_screen,text="Quantity",bg="white",fg="black",font=('Microsoft Yahei UI light)',15))
        quantity_label.place(x=10,y=450)
        
        quantity_entry=Entry(cart_screen,width=22,bg="white",highlightthickness=2,borderwidth=1,font=("Helvetica", 13))
        quantity_entry.place(x=63,y=490)
        quantity_entry.insert(0,"0")
        
        
        def increment_qunat():
            current_value = int(quantity_entry.get())
            new_value = current_value + 1
            quantity_entry.delete(0, END)
            quantity_entry.insert(0, str(new_value))
        
        def dec_quant():
            current_value = int(quantity_entry.get())
            if current_value > 0:
              new_value = current_value - 1
              quantity_entry.delete(0, END)
              quantity_entry.insert(0, str(new_value))
        
        dec_but=Button(cart_screen,text="-",bg="white",fg="red",width=4,command=dec_quant)
        dec_but.place(x=14,y=490)
        
        inc_but=Button(cart_screen,text="+",bg="white",fg="blue",width=4,command=increment_qunat)
        inc_but.place(x=340,y=490)
        
        place_order_but=Button(cart_screen,width=25,cursor="hand2",border=0,text="Place Order",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=place_order_databse)
        place_order_but.place(x=100,y=600)
        
        
        
        
        
        cart_screen.mainloop()
        
        
        return
    
    def track_order_fun():
        
        def tracking_page():
                        
         def show_orders():
             
             order_frame=Frame(order_show_frame,highlightbackground='blue',width=700,height=400,highlightthickness=2,bg="white")
             order_frame.place(x=0,y=100)
             
             
             
             my_canvas=Canvas(order_frame,width=665,height=390)
             my_canvas.pack(side=LEFT,fill=BOTH,expand=TRUE)
    
            
             my_scrool_bar=Scrollbar(order_frame,orient=VERTICAL,command=my_canvas.yview)
             my_scrool_bar.pack(side=RIGHT,fill=Y)
                
               
            
      
            

            
             my_canvas.config(yscrollcommand=my_scrool_bar.set)
             my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all")))
                
                
             second_frame=Frame(my_canvas)
             my_canvas.create_window((0,0),window=second_frame,anchor="nw")
             
             
             colum_name=("Tracking-ID","ISBN","Address","quantity","Time")
                
             for i,col in enumerate(colum_name):
                     label = Label(second_frame, text=col, font=("Arial", 9, "bold"))
                     label.grid(row=0, column=i+5, padx=2, pady=5)
                     
             
             
                     
             connection=sqlite3.connect("library_sys2.db")
             cursor=connection.cursor()
             
             
             
             cursor.execute("Select Customer_Id from Customer_details where email=?",(email_entry.get(),))
             cust_id=cursor.fetchone()
             print(cust_id)
             if cust_id!=None:
               cursor.execute("Select order_id,ISBN,address,quantity,time from orders where customer_id=? and status is NULL",(cust_id[0],))
               data=cursor.fetchall()
             
               for row, record in enumerate(data):
                  for col, value in enumerate(record):
                     label = Label(second_frame, text=value,font=(7))
                     label.grid(row=row+1, column=col+5, padx=18, pady=7)
             else:
                 messagebox.showinfo("UNAVAIABILITY","You does not placed any order yet")
                 
             connection.commit()
             connection.close()
             
             
             return
            
         email_entry=Entry(order_show_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
         email_entry.place(x=180,y=70)
         email_entry.insert(0,"Enter the Email Id")
         email_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(email_entry))
         Frame(order_show_frame,width=223,height=2,bg="red").place(x=180,y=67)
         Frame(order_show_frame,width=223,height=2,bg="red").place(x=180,y=100)
         
         enter_btn=Button(order_show_frame,width=6,text="Enter",border=0,bg="White",cursor="hand2",fg="blue",font=("Microsoft Yahei UI light",12,'bold'),command=show_orders)
         enter_btn.place(x=430,y=65)
         
         return
        
        def confirm_update_page():
            ## in cnfirm just user jo ha cnfrm kre ga quant minus + add in sales make the sales table also
            
            
         def get_data_and_update():
             
             def get_data_and_update_quant():
                 track_no=track_entry.get()
                 
                 if track_no=="" or track_no=="Tracking Id":
                     messagebox.showerror("Error","Please fill the fields")
                 elif track_no!="" and  track_no!="Tracking Id":
                     connection=sqlite3.connect("library_sys2.db")
                     cursor=connection.cursor()
                     cursor.execute("Select ISBN, Quantity from orders where order_id=?",(track_no,))
                     isbn=cursor.fetchone()
                     print(isbn)
                     if isbn==None:
                         messagebox.showerror("Invalid","no isbn")
                     else:
                         cursor.execute("Select quantity from Books_details where ISBN=? ",(isbn[0],))
                         actual_quant=cursor.fetchone()
                         diff_quant=int(actual_quant[0])-int(isbn[1])
                         cursor.execute("Update  Books_details set quantity=? where isbn=?",(int(diff_quant),isbn[0],))
                         connection.commit()
                         cursor.execute("Update orders set status='Deliverd' where order_id=?",(track_no,))
                         connection.commit()
                         
                         messagebox.showinfo("Thanks","Your order has been confirmed Thank you for using Khoso management system")
                         
                         
                         
                 
                 
                 
                 return
             
             
             email=email_entry.get()
             databse_acc=BooleanVar()
             if email=="" or email=="Email Id":
                 messagebox.showerror("Error","Please fill the fields")
             else:
                 databse_acc=True
             
             if databse_acc==True:
                 connection=sqlite3.connect("library_sys2.db")
                 cursor=connection.cursor()
                 cursor.execute("Select Customer_Id from Customer_details where email=?",(email,))
                 cust_id=cursor.fetchone()
                 
                 if cust_id==None:
                     messagebox.showinfo("Email","Inavlid email or may account cant be created")
                 else:
                     print(cust_id[0])
                     cursor.execute("Select order_id,ISBN,address,quantity,time from orders where customer_id=? and status is NULL",(cust_id[0],))
                     data=cursor.fetchall()
                     for row, record in enumerate(data):
                      for col, value in enumerate(record):
                       label = Label(second_frame, text=value,font=(7))
                       label.grid(row=row+1, column=col+5, padx=18, pady=7)
                       
                     track_entry=Entry(order_show_frame,fg="black",border=1,bg="white",width=16,font=("Microsoft Yahei UI light",11,'bold'))
                     track_entry.place(x=220,y=390)
                     track_entry.insert(0,"Tracking Id")
                     track_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(track_entry))
                     Frame(order_show_frame,width=180,height=2,bg="red").place(x=220,y=390)
                     Frame(order_show_frame,width=180,height=2,bg="red").place(x=220,y=415)
                     track_entr_btn=Button(order_show_frame,width=6,text="Confirm",border=0,bg="White",cursor="hand2",fg="blue",font=("Microsoft Yahei UI light",10,'bold'),command=get_data_and_update_quant)
                     track_entr_btn.place(x=405,y=390)
                     
                 
             return
         
         order_frame=Frame(order_show_frame,highlightbackground='blue',width=700,height=200,highlightthickness=2,bg="white")
         order_frame.place(x=0,y=14)
             
             
             
         my_canvas=Canvas(order_frame,width=665,height=260)
         my_canvas.pack(side=LEFT,fill=BOTH,expand=TRUE)
    
            
         my_scrool_bar=Scrollbar(order_frame,orient=VERTICAL,command=my_canvas.yview)
         my_scrool_bar.pack(side=RIGHT,fill=Y)
                
               
         my_canvas.config(yscrollcommand=my_scrool_bar.set)
         my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all")))
                
                
         second_frame=Frame(my_canvas)
         my_canvas.create_window((0,0),window=second_frame,anchor="nw")
             
             
         colum_name=("Tracking-ID","ISBN","Address","quantity","Time")
                
         for i,col in enumerate(colum_name):
                     label = Label(second_frame, text=col, font=("Arial", 9, "bold"))
                     label.grid(row=0, column=i+5, padx=2, pady=5)
                     
         #cursor.execute("Select order_id,ISBN,address,quantity,time from orders where customer_id=?",(cust_id[0],))
         #data=cursor.fetchall()
         #for row, record in enumerate(data):
          #            for col, value in enumerate(record):
           #            label = Label(second_frame, text=value,font=(7))
            #           label.grid(row=row+1, column=col+5, padx=18, pady=7)
                       
         email_entry=Entry(order_show_frame,fg="black",border=1,bg="white",width=16,font=("Microsoft Yahei UI light",11,'bold'))
         email_entry.place(x=220,y=320)
         email_entry.insert(0,"Email Id")
         email_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(email_entry))
         Frame(order_show_frame,width=180,height=2,bg="red").place(x=220,y=320)
         Frame(order_show_frame,width=180,height=2,bg="red").place(x=220,y=345)
         email_entr_btn=Button(order_show_frame,width=6,text="Enter",border=0,bg="White",cursor="hand2",fg="blue",font=("Microsoft Yahei UI light",10,'bold'),command=get_data_and_update)
         email_entr_btn.place(x=400,y=320)
         return
        
        
        def Update_track_page():
            # tracking ..../
         def update_databse():
             email=email_entry.get()
             
             def enter_2_btn_update_work():
                 selected_input=books_select.get()
                 print(selected_input)
                 if selected_input!="" and selected_input=="Select The options":
                     messagebox.showinfo("Error","Please select from the dropdown menu")
                 elif selected_input!="" and selected_input!="Select The options":
                     deelte_pages()
                     
                     
                     def isbn_update():
                         track_no=tracking_entry.get()
                         isbn_no=isbn_entry.get()
                         databse_accees=False
                         if (isbn_no=="" and track_no=="")  or (isbn_no=="ISBN" and track_no=="Tracking Id"):
                             messagebox.showerror("Error","Please fill the all fields")
                         elif (isbn_no!="" and track_no!="")  or (isbn_no!="ISBN" and track_no!="Tracking Id"):
                             databse_accees=True
                             connection=sqlite3.connect("library_sys2.db")
                             cursor=connection.cursor()
                             cursor.execute("Select ISBN from Books_details where ISBN=? ",(isbn_no,))
                             isbn_true=cursor.fetchone()
                             print(isbn_true)
                             if isbn_true==None:
                                 databse_accees=False
                                 messagebox.showinfo("INFO",f"ISBN{isbn_no} is not present in the database")
                                 connection.commit()
                                 connection.close()
                                 return
                             else:
                                 databse_accees=True
                             if databse_accees==True:
                                 cursor.execute("Update orders set ISBN=? where order_id=?",(isbn_no,track_no,))
                                 connection.commit()
                                 messagebox.showinfo("DONE",f"Book having ISBN[{isbn_no}] is changed")
                                 
                         
                         return
                     
                     def address_update():
                         track_no=tracking_entry.get()
                         address=Address_entry.get()
                         
                         if (address=="" and track_no=="")  or (address=="Address" and track_no=="Tracking Id"):
                             messagebox.showerror("Error","Please fill the all fields")
                         elif (address!="" and track_no!="")  or (address!="Address" and track_no!="Tracking Id"):
                             connection=sqlite3.connect("library_sys2.db")
                             cursor=connection.cursor()
                             cursor.execute("Update orders set address=? where order_id=?",(address,track_no,))
                             connection.commit()
                             connection.close()
                             messagebox.showinfo("DONE","Address has been   changed")
                             
                         return
                     
                     
                     def quant_update():
                         track_no=tracking_entry.get()
                         quantity=quant_entry.get()
                         
                         if (track_no=="" and quantity=="") or (track_no=="Tracking Id" and quantity=="Quantity"):
                             messagebox.showerror("Invalid","Please fill the all fields")
                         elif (track_no!="" and quantity!="") or (track_no!="Tracking Id" and quantity!="Quantity"):
                             connection=sqlite3.connect("library_sys2.db")
                             cursor=connection.cursor()
                             cursor.execute("Update orders set quantity=? where order_id=?",(quantity,track_no,))
                             connection.commit()
                             connection.close()
                             messagebox.showinfo("DONE","Qunatity has been   changed")
                         return
                     
                     
                     
                     
                     
                     if selected_input=="ISBN":
                         tracking_entry=Entry(enter2_frame,fg="black",border=1,bg="white",width=16,font=("Microsoft Yahei UI light",11,'bold'))
                         tracking_entry.place(x=115,y=15)
                         tracking_entry.insert(0,"Tracking Id")
                         tracking_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(tracking_entry))
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=115,y=15)
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=115,y=44)
                         
                         
                         isbn_entry=Entry(enter2_frame,fg="black",border=1,bg="white",width=16,font=("Microsoft Yahei UI light",11,'bold'))
                         isbn_entry.place(x=380,y=15)
                         isbn_entry.insert(0,"ISBN")
                         isbn_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(isbn_entry))
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=380,y=15)
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=380,y=44)
                         ### function for updating the data in the data base 
                         isbn_enter=Button(enter2_frame, text="Enter", width=20, bg="blue", fg="white", font=("Microsoft Yahei UI light",8,'bold'),command=isbn_update)
                         isbn_enter.place(x=245, y=60)
                         print("isbn")
                     elif selected_input=="Address":
                         tracking_entry=Entry(enter2_frame,fg="black",border=1,bg="white",width=16,font=("Microsoft Yahei UI light",11,'bold'))
                         tracking_entry.place(x=115,y=15)
                         tracking_entry.insert(0,"Tracking Id")
                         tracking_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(tracking_entry))
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=115,y=15)
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=115,y=44)
                         
                         
                         Address_entry=Entry(enter2_frame,fg="black",border=1,bg="white",width=16,font=("Microsoft Yahei UI light",11,'bold'))
                         Address_entry.place(x=380,y=15)
                         Address_entry.insert(0,"Address")
                         Address_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(Address_entry))
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=380,y=15)
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=380,y=44)
                         ### function for updating the data in the data base 
                         add_enter=Button(enter2_frame, text="Enter", width=20, bg="blue", fg="white", font=("Microsoft Yahei UI light",8,'bold'),command=address_update)
                         add_enter.place(x=245, y=60)
                         print("address")
                     elif selected_input=="Quantity":
                         tracking_entry=Entry(enter2_frame,fg="black",border=1,bg="white",width=16,font=("Microsoft Yahei UI light",11,'bold'))
                         tracking_entry.place(x=115,y=15)
                         tracking_entry.insert(0,"Tracking Id")
                         tracking_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(tracking_entry))
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=115,y=15)
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=115,y=44)
                         
                         
                         quant_entry=Entry(enter2_frame,fg="black",border=1,bg="white",width=16,font=("Microsoft Yahei UI light",11,'bold'))
                         quant_entry.place(x=380,y=15)
                         quant_entry.insert(0,"Quantity")
                         quant_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(quant_entry))
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=380,y=15)
                         Frame(enter2_frame,width=180,height=2,bg="red").place(x=380,y=44)
                         ### function for updating the data in the data base 
                         quant_enter=Button(enter2_frame, text="Enter", width=20, bg="blue", fg="white", font=("Microsoft Yahei UI light",8,'bold'),command=quant_update)
                         quant_enter.place(x=245, y=60)
                         print("qunat")
                 return
             
             def deelte_pages():
                 for frame in enter2_frame.winfo_children():
                     frame.destroy()
           
             
            
             if (email!="" and email=="Enter the Email Id") or email=="":
                 messagebox.showerror("Error","Please fill the email field")
             if email!="" and email!="Enter the Email Id":
                 connection=sqlite3.connect("library_sys2.db")
                 cursor=connection.cursor()
                 cursor.execute("Select Customer_Id from Customer_details where email=?",(email,))
                 cust_id=cursor.fetchone()
                 if cust_id==None:
                     messagebox.showinfo("Unavailable",f"The email[{email}] is not in the database")
                     return
                 else:
                     cursor.execute("Select order_id,ISBN,address,quantity,time from orders where customer_id=?  and status is NULL",(cust_id[0],))
                     data=cursor.fetchall()
                     for row, record in enumerate(data):
                      for col, value in enumerate(record):
                       label = Label(second_frame, text=value,font=(7))
                       label.grid(row=row+1, column=col+5, padx=18, pady=7)
                 books_list = ("ISBN","Address","Quantity")
                 books_select = StringVar()
                 books_select.set("Select The options")
            
                 year_menu=OptionMenu(order_show_frame,books_select,*books_list)
             
            
                 year_menu.config(highlightbackground="red", highlightcolor="red",fg="black",bg="white", borderwidth=1,width=18)
                 year_menu.place(x=390,y=325)
                 enter2_btn=Button(order_show_frame,width=6,text="Enter",border=0,bg="White",cursor="hand2",fg="blue",font=("Microsoft Yahei UI light",10,'bold'),command=enter_2_btn_update_work)
                 enter2_btn.place(x=590,y=330)
                 # set the frame for the options selected + also pagging system
                 enter2_frame=Frame(order_show_frame,width=687,height=120,bg='white',highlightbackground='red',highlightthickness=1)
                 enter2_frame.place(x=1,y=380)
                 enter2_frame.propagate(False)
                 
                     
                 
             return
         
         
         order_frame=Frame(order_show_frame,highlightbackground='blue',width=700,height=200,highlightthickness=2,bg="white")
         order_frame.place(x=0,y=14)
             
             
             
         my_canvas=Canvas(order_frame,width=665,height=260)
         my_canvas.pack(side=LEFT,fill=BOTH,expand=TRUE)
    
            
         my_scrool_bar=Scrollbar(order_frame,orient=VERTICAL,command=my_canvas.yview)
         my_scrool_bar.pack(side=RIGHT,fill=Y)
                
               
         my_canvas.config(yscrollcommand=my_scrool_bar.set)
         my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all")))
                
                
         second_frame=Frame(my_canvas)
         my_canvas.create_window((0,0),window=second_frame,anchor="nw")
             
             
         colum_name=("Tracking-ID","ISBN","Address","quantity","Time")
                
         for i,col in enumerate(colum_name):
                     label = Label(second_frame, text=col, font=("Arial", 9, "bold"))
                     label.grid(row=0, column=i+5, padx=2, pady=5)
                     
         email_entry=Entry(order_show_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
         email_entry.place(x=40,y=330)
         email_entry.insert(0,"Enter the Email Id")
         email_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(email_entry))
         Frame(order_show_frame,width=223,height=2,bg="red").place(x=40,y=330)
         Frame(order_show_frame,width=223,height=2,bg="red").place(x=40,y=360)
         
         enter_btn=Button(order_show_frame,width=6,text="Enter",border=0,bg="White",cursor="hand2",fg="blue",font=("Microsoft Yahei UI light",10,'bold'),command=update_databse)
         enter_btn.place(x=260,y=330)
         
         return
        
        def delete_track_page():
            
            
         def del_order_fun():
             email=email_entry.get()
             order_no=order_id_entry.get()
             
             if email=="":
                 messagebox.showerror("Error","Please fill the email address to get record")
             if email!="" and email!="Enter the Email Id":
                 connection=sqlite3.connect("library_sys2.db")
                 cursor=connection.cursor()
                 cursor.execute("Select Customer_Id from Customer_details where email = ?",(email,))
                 cust_no=cursor.fetchone()
                 if cust_no == None:
                     messagebox.showinfo("Hey","Inavlid email")
                 else:
                     cursor.execute("Select order_id,ISBN,address,quantity,time from orders where customer_id=? and status is NULL",(cust_no[0],))
                     data=cursor.fetchall()
                     for row, record in enumerate(data):
                       for col, value in enumerate(record):
                        label = Label(second_frame, text=value,font=(7))
                        label.grid(row=row+1, column=col+5, padx=18, pady=7)
             if email!="" and order_no!="" and order_no!="Enter the Order Id":
                 cursor.execute("Delete from orders where order_id=?",(order_no,))
                 messagebox.showinfo("Done",f"Your order having Tracking no {order_no} is deleted")
                 connection.commit()
             if email=="Enter the Email Id" and order_no=="Enter the Order Id":
                 messagebox.showinfo("Error","Please fill the all fields")
             return
         
         
            
         email_entry=Entry(order_show_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
         email_entry.place(x=70,y=370)
         email_entry.insert(0,"Enter the Email Id")
         email_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(email_entry))
         Frame(order_show_frame,width=223,height=2,bg="red").place(x=70,y=370)
         Frame(order_show_frame,width=223,height=2,bg="red").place(x=70,y=400)
         
         
         order_id_entry=Entry(order_show_frame,fg="black",border=1,bg="white",width=20,font=("Microsoft Yahei UI light",11,'bold'))
         order_id_entry.place(x=390,y=370)
         order_id_entry.insert(0,"Enter the Order Id")
         order_id_entry.bind("<Button-1>", lambda event:entryclear.clear_ISBN(order_id_entry))
         Frame(order_show_frame,width=223,height=2,bg="red").place(x=390,y=370)
         Frame(order_show_frame,width=223,height=2,bg="red").place(x=390,y=400) 
         
         enter_bt=Button(order_show_frame,width=20,text="Enter",border=0,bg="blue",cursor="hand2",fg="white",font=("Microsoft Yahei UI light",8,'bold'),command=del_order_fun)
         enter_bt.place(x=250,y=440)
         
         
         order_frame=Frame(order_show_frame,highlightbackground='blue',width=700,height=200,highlightthickness=2,bg="white")
         order_frame.place(x=0,y=14)
             
             
             
         my_canvas=Canvas(order_frame,width=665,height=260)
         my_canvas.pack(side=LEFT,fill=BOTH,expand=TRUE)
    
            
         my_scrool_bar=Scrollbar(order_frame,orient=VERTICAL,command=my_canvas.yview)
         my_scrool_bar.pack(side=RIGHT,fill=Y)
                
               
         my_canvas.config(yscrollcommand=my_scrool_bar.set)
         my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all")))
                
                
         second_frame=Frame(my_canvas)
         my_canvas.create_window((0,0),window=second_frame,anchor="nw")
             
             
         colum_name=("Tracking-ID","ISBN","Address","quantity","Time")
                
         for i,col in enumerate(colum_name):
                     label = Label(second_frame, text=col, font=("Arial", 9, "bold"))
                     label.grid(row=0, column=i+5, padx=2, pady=5)
         
         
         return
        
        
        
        
        track_screen=Toplevel(root)
        track_screen.title("Tracking")
        track_screen.geometry("700x700")
        track_screen.config(bg="white")
       # track_screen.propagate(False,False)
        
        def hide_indicators():
            trac_but_frame.config(bg="white")
            confirm_but_frame.config(bg="white")
            update_but_frame.config(bg="white")
            delete_but_frame.config(bg="white")
        
        def delete_pages():
            for frame in order_show_frame.winfo_children():
                frame.destroy()
            
            return
        
        def update_btn_indicator(obj,page):
            hide_indicators()
            obj.config(bg="black")
            delete_pages()
            page()
        
            
        header_image=ImageTk.PhotoImage(file="C:/Users/user/Downloads/Group 1 (7).png")
        Label(track_screen,image=header_image).pack()
        track_butt=Button(track_screen,width=14,cursor="hand2",border=0,text="Track",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:update_btn_indicator(trac_but_frame,tracking_page))#,command=lambda:update_btns_indicator(book_table_btn_indicator,book_btn_page))
        track_butt.place(x=10,y=150)
        trac_but_frame=Frame(track_screen,bg="white",height=3,width=150)
        trac_but_frame.place(x=14,y=195)
        
        confirm_butt=Button(track_screen,width=14,cursor="hand2",border=0,text="confirm",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:update_btn_indicator(confirm_but_frame,confirm_update_page))#,command=lambda:update_btns_indicator(book_table_btn_indicator,book_btn_page))
        confirm_butt.place(x=170+35-15,y=150)
        confirm_but_frame=Frame(track_screen,bg="white",height=3,width=150)
        confirm_but_frame.place(x=194,y=195)
        
        
        Update_butt=Button(track_screen,width=14,cursor="hand2",border=0,text="Update",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:update_btn_indicator(update_but_frame,Update_track_page))#,command=lambda:update_btns_indicator(book_table_btn_indicator,book_btn_page))
        Update_butt.place(x=170+168+35-5,y=150)
        update_but_frame=Frame(track_screen,bg="white",height=3,width=150)
        update_but_frame.place(x=170+168+35-5+4,y=195)
        
        delete_butt=Button(track_screen,width=13,cursor="hand2",border=0,text="Delete",bg="blue",fg="white",font=("Microsoft Yahei UI light",11,'bold'),command=lambda:update_btn_indicator(delete_but_frame,delete_track_page))#,command=lambda:update_btns_indicator(book_table_btn_indicator,book_btn_page))
        delete_butt.place(x=170+168+168+35+5,y=150)
        delete_but_frame=Frame(track_screen,bg="white",height=3,width=140)
        delete_but_frame.place(x=170+168+168+35+5+4,y=195)
        
        
        
        order_show_frame=Frame(track_screen,width=699,height=500,bg='white',highlightbackground='white',highlightthickness=0)
        order_show_frame.propagate(False)
        order_show_frame.place(x=0,y=199)
        
        
        
        
        
        track_screen.mainloop()
        
        return
    
    user_screen=Toplevel(root)
    user_screen.title("USER PORTAL")
    user_screen.geometry("1300x750")
    #user_screen.resizable(False,False)
    user_screen.config(bg="White")
    
    main_image=ImageTk.PhotoImage(file="Assets/Frame 1.png")
    
    Label(user_screen,image=main_image).pack()
    
    home_image=ImageTk.PhotoImage(file="Assets/home.png")
    home_but=Button(user_screen,border=0,borderwidth=0,image=home_image,bg="white",command=get_mainportal)
    home_but.place(x=0,y=190)
    Label(user_screen,text="HOME",bg="white",fg="black",font=('Microsoft Yahei UI light)',15,'bold')).place(x=50,y=210)
    
    user_account_icon=ImageTk.PhotoImage(file="Assets/user account icon.jpg")
    user_account_button=Button(user_screen,border=0,borderwidth=0,image=user_account_icon,bg="white",command=user_account)
    user_account_button.place(x=1180,y=190)
    
    user_cart_icon=ImageTk.PhotoImage(file="Assets/shopping-cart.png")
    user_cart_butt=Button(user_screen,border=0,borderwidth=0,image=user_cart_icon,bg="white",command=cart_order_place)
    user_cart_butt.place(x=1240,y=190)
    
    books_show_frame=Frame(user_screen,highlightbackground='blue',width=1299,height=400,highlightthickness=2,bg="white")
    books_show_frame.place(x=0,y=250)
    
    track_order_icon=ImageTk.PhotoImage(file="Assets/tracking.png")
    track_order_butt=Button(user_screen,border=0,borderwidth=0,image=track_order_icon,bg="white",command=track_order_fun)
    track_order_butt.place(x=1100,y=184)
    
    
    my_canvas=Canvas(books_show_frame,width=1265,height=240)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=TRUE)
    
            
    my_scrool_bar=Scrollbar(books_show_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrool_bar.pack(side=RIGHT,fill=Y)
                
               
            
      
            

            
    my_canvas.config(yscrollcommand=my_scrool_bar.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all")))
                
                
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")
    
    
    
    connection=sqlite3.connect("library_sys2.db")
    cursor=connection.cursor()
    cursor.execute("Select b.ISBN,b.book_name,a.name,p.publisher_name,b.genre,b.price from Books_details b , author_details a , publisher_details p where (b.author_id=a.author_id) and (b.publisher_id=p.publisher_id)")
    data=cursor.fetchall()
    connection.commit()
    connection.close()
    
    colum_name=("ISBN-NO","BOOKNAme","AUTHOR","Publisher","Genre","Price")
                
    for i,col in enumerate(colum_name):
                     label = Label(second_frame, text=col, font=("Arial", 8, "bold"))
                     label.grid(row=0, column=i+5, padx=2, pady=5)
                     
                     
    for row, record in enumerate(data):
                  for col, value in enumerate(record):
                     label = Label(second_frame, text=value,font=(8))
                     label.grid(row=row+1, column=col+5, padx=18, pady=7)
    
 
                
                
    #for i in data:
     #    book_table.insert(parent='', index='end', text="parent",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    
    user_screen.mainloop()
    return
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def team_portal():
    
    team_screen=Toplevel(root)
    
    team_screen.geometry("500x500")
    team_screen.propagate(False)
    team_screen.config(bg="black")
    
    Label(team_screen,text="This project is only made by mairaj-> one man army",bg="black",fg="white",font=(40)).pack()
    
    team_screen.mainloop()
    
    return


def signin_screen()  :
    
     
     
      root.iconify()   
      def admin_del():
          screen1.destroy()
          administration_portal()
          return
          
      
      def user_del():
          screen1.after(100)
          screen1.destroy()
          user_portal()
          return
      
      def team_del():
          screen1.after(100)
          screen1.destroy()
          team_portal()
          return
        
      
      screen1=Toplevel(root)
      
      screen1.title("ONLINE BOOK MANAGEMENT SYSTEM")
      screen1.geometry("1650x920")
      screen1.config(bg="black")
      screen1.resizable(FALSE,FALSE)
      #Label(screen1, text="Library management system", bg="black",fg="white",font=('Calibiri(Body)',40,'bold')).pack()
      if flag==False:
        root.destroy()
        
        
      book_image=ImageTk.PhotoImage(file="Assets/resize-1678907083105117588books.jpg")
      Label(screen1,image=book_image).pack()
      
      Label(screen1, text="Welcome to KHOSO Book Store",fg="white",bg="black",font=('Microsoft Yahei UI light)',30,'bold')).pack()

      admin_image=ImageTk.PhotoImage(file="Assets/images.png")
      
      admin_lable=Label(screen1,image=admin_image,bg="black")
      admin_lable.place(x=320,y=525)
      
      admin_button=Button(screen1,text="Admin",width=12,fg="white",bg="orange",font=('Microsoft Yahei UI light)',13,'bold'),command=admin_del)
      admin_button.place(x=330,y=750)
     
      user_image=ImageTk.PhotoImage(file="Assets/userimg.jpg")# jpg is not working
      user_label=Label(screen1,image=user_image,bg="black")
      user_label.place(x=715,y=495)
      
      user_button=Button(screen1,text="User",width=12,fg="white",bg="orange",font=('Microsoft Yahei UI light)',13,'bold'),command=user_del)
      user_button.place(x=753,y=750)
      
      team_img=ImageTk.PhotoImage(file="Assets/mem.jpg")
      team_label=Label(screen1,image=team_img,bg="black")
      team_label.place(x=1110,y=515)
      
      team_button=Button(screen1,text="Team",width=12,bg="orange",fg="white",font=('Microsoft Yahei UI light)',13,'bold'),command=team_del)
      team_button.place(x=1145,y=750)
     
     
     
     
     
     
     
     
     
     
     
     
      screen1.mainloop()











###############################################################################################################################################################
def signin():
  
   username=user.get()
   password=passwrd.get()
   
   flag1=False
   flag2=False
   k=TRUE
   connection=sqlite3.connect("library_sys2.db")
   cursor=connection.cursor()
   cursor.execute("SELECT * FROM user_details")
   records=cursor.fetchall()
   for record in records:
       if username==record[2] and password==record[3]:
           signin_screen()
           k=False
           break            
       elif username==record[2] :
            flag1=True
       elif password==record[3]:
           flag2=True
   if username==password:
       print("")
                       
   elif flag1:
       messagebox.showerror("Invalid","Invalid password")
   elif flag2:
       messagebox.showerror("Invalid","Invalid username")
   elif k:
       messagebox.showerror("Invalid", "Invalid username and password")
       
            

   


def clear_showbar(event):
    user.delete(0,END)

def clear_showbar1(event):
    passwrd.delete(0,END)
    passwrd.config(show="*")
    
def hide_pass_png(event):
    passwrd.config(show="")
    
def see_pass_png(event):
    passwrd.config(show="*")
    
img=PhotoImage(file="Assets/login resize.png")
Label(root,image=img,bg="white").place(x=50,y=50)

frame=Frame(root, width=500, height=500,bg="white").place(x=540,y=50)

label_heading=Label(frame, text="Sign In", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI light",23,'bold'))
label_heading.place(x=730,y=85)




       
     

user=Entry(frame, fg="black",border=0,bg="white",width=30,font=("Microsoft Yahei UI light",11,'bold'))
user.place(x=620,y=180)
user.insert(0,"Username")
user.bind("<Button-1>", clear_showbar)




Frame(frame,width=350,height=2,bg="black").place(x=620,y=210)

#password section

passwrd=Entry(frame,fg="black",border=0,bg="white",width=30,font=("Microsoft Yahei UI light",11,'bold'))
passwrd.place(x=620,y=260)
passwrd.insert(0,"Password")
Frame(frame,width=350,height=2,bg="black").place(x=620,y=290)
passwrd.bind("<Button-1>", clear_showbar1)



#sigin button
flag=TRUE
sign_in_button=Button(frame, width=30, pady=7, text="Sign in",bg="blue",fg="white",border=0,command=signin_screen)
sign_in_button.place(x=675,y=330)

#signup option
sign_up=Label(frame,text="Don't have an account?",fg="black",bg="white",border=0,font=("Microsoft Yahei UI light",9))
sign_up.place(x=685,y=383)

eyeimage=PhotoImage(file="Assets/9883471.png")
eye_button=Button(frame,image=eyeimage,border=0,bg="white")
eye_button.place(x=940,y=258)
eye_button.bind("<ButtonRelease-1>",see_pass_png)
eye_button.bind("<ButtonPress-1>",hide_pass_png)

sign_up_text=Button(frame,width=6,text="sign up",border=0,bg="white",cursor="hand2",fg="blue",font=("Microsoft Yahei UI light",8,'bold'),command=new_login)
sign_up_text.place(x=851,y=382)

forgot_pass=Button(frame,width=15,text="Forgot Password?",border=0,bg="White",cursor="hand2",fg="blue",font=("Microsoft Yahei UI light",8,'bold'),command=forgot_ui)
forgot_pass.place(x=835,y=295)

connection.commit()
connection.close()
root.mainloop()