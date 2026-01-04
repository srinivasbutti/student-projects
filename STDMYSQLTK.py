"""
1. back end creation  i.e database=>table
2. creating api with required fields
3. inserting data into database/table

mysql> create database stddb;
Query OK, 1 row affected (0.00 sec)

mysql> use stddb;
Database changed
mysql> create table reg(name varchar(20),contact bigint(15),email varchar(20),gender varchar(10),city varchar(20),state varchar(20) );
Query OK, 0 rows affected (0.05 sec)

hno
street
disrict
zipcode

aadhar
pan
"""

from tkinter import *
from  tkinter import  ttk
#importing connection
import  mysql.connector

#establishing connection
conn = mysql.connector.connect(
   user='root', password='root',host='localhost', database='stddb')
#defining register function
def register():
    #getting form data
    name1=name.get()
    con1=contact.get()
    email1=email.get()
    gen1=gender.get()
    city1=city.get()
    state1=state.get()
    #applying empty validation
    if name1=='' or con1==''or email1=='' or gen1==''or city1==''or state1=='':
        message.set("Fill The Empty Field(s)!!!")
    else:
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = (
           "INSERT INTO REG(NAME, CONTACT, EMAIL, GENDER, CITY, STATE) VALUES (%s, %s, %s, %s, %s, %s)"
       )
       if gen1==1:
        data = (name1, con1,email1,"Male",city1,state1)
       else:
        data = (name1, con1, email1, "Female", city1, state1)
       try:
           #executing the sql command
           cursor.execute(insert_stmt,data)
           #commit changes in database
           conn.commit()
       except:
           conn.rollback()
       message.set("Data Stored Successfully")
       
    
#defining Registrationform function
def Registrationform():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Student Registration Form")
    #setting height and width of screen
    reg_screen.geometry("350x400")
    #declaring variable
    global message
    global name
    global contact
    global email
    global gender
    global city
    global state
    
    name = StringVar()
    contact = StringVar()
    email=StringVar()
    gender=IntVar()
    city=StringVar()
    state=StringVar()
    message=StringVar()
    
    #Creating layout of Registration form
    Label(reg_screen,width="300", text="Please enter details below", bg="white",fg="blue").pack()
    
    #name Label
    Label(reg_screen, text="Name * ").place(x=30,y=40)
    #name textbox
    Entry(reg_screen, textvariable=name).place(x=90,y=42)
    #contact Label
    Label(reg_screen, text="Contact * ").place(x=20,y=80)
    #contact textbox
    Entry(reg_screen, textvariable=contact).place(x=90,y=82)
    # email Label
    Label(reg_screen, text="Email * ").place(x=20, y=120)
    # email textbox
    Entry(reg_screen, textvariable=email).place(x=90, y=122)
    # gender Label
    Label(reg_screen, text="Gender * ").place(x=20, y=160)
    # gender radiobutton
    Radiobutton(reg_screen,text="Male",variable=gender,value=1).place(x=90,y=162)
    Radiobutton(reg_screen, text="Female", variable=gender,value=2).place(x=150, y=162)

    # city Label
    Label(reg_screen, text="City * ").place(x=20, y=200)
    # city combobox
    city = ttk.Combobox(reg_screen, width=27, textvariable=city)
    city['values'] = ('Hassan','Delhi','madhurai','Amaravathi',' HYDERABAD','vizag','kakinada','Vijayawada',' Bhopal',
                              'Tirupathi', ' Patna', ' Indore', ' Nagpur',
                              ' Mumbai',  ' Pune', ' Gwalior',' Jabalpur',
                              'Shillong', 'Bangalore','Mysore' )
    city.current()
    city.place(x=90,y=202)

    # state Label
    Label(reg_screen, text="State * ").place(x=20, y=240)
    # state combobox
    state = ttk.Combobox(reg_screen, width=27, textvariable=state)
    state['values'] = ('Delhi','Tamilnadu','TELANGANA','Maharashtra',
                              ' Madhya Pradesh',
                              ' ANDHRA PRADESH',
                              ' Gujrat',' Rajasthan',
                              'Meghalaya','Karnataka',
                              'chattisgarh','Kashmir',
                              'punjab','Assam','Sikkim','Kerala')
    state.current()
    state.place(x=90, y=242)
    #Label for displaying login status[success/failed]
    Label(reg_screen, text="",textvariable=message,fg='red').place(x=95,y=264)
    #Login button
    Button(reg_screen, text="Register", width=10, height=1, bg="green",fg='white',command=register).place(x=120,y=300)
    
    reg_screen.mainloop()
#calling function Registrationform
Registrationform()
