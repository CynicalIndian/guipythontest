#==========================#
#   IMPORTS                #
#==========================#
import MySQLdb as mysql
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import scrolledtext

#Create Instance
win = tk.Tk()

#Add a title
win.title("Diwakar's Project")

#Establishing connection with the Database
conn = mysql.connect(user='root', password='admin',
host='127.0.0.1', db='Em_DB')

# create cursor
cursor = conn.cursor()
cursor1 = conn.cursor()
cursor2 = conn.cursor()
cursor3 = conn.cursor()
cursor4 = conn.cursor()
cursor5 = conn.cursor()
cursor6 = conn.cursor()
cursor7 = conn.cursor()
cursor8 = conn.cursor()
cursor9 = conn.cursor()
cursor10 = conn.cursor()

#EmployeeInfo TAB
tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Employee Info")
tabControl.pack(expand=1, fill="both")
EmployeeInfo = ttk.LabelFrame(tab1, text='Employee Information')
EmployeeInfo.grid(column=0,row=0,sticky='W')

#HEADING LABEL FOR EMPLOYEE INFO TAB
a_Label = ttk.Label(EmployeeInfo, text="Welcome to the Employee Information Database")
a_Label.config(font = ("Times New Roman", 22))
a_Label.grid(column=0, row=1)

a1_Label = ttk.Label(EmployeeInfo, text="Please Enter The Correct Name")
a1_Label.config(font = ("Times New Roman", 10))
a1_Label.grid(column=0, row=3)

a2_Label = ttk.Label(EmployeeInfo, text = "EMPLOYEE INFO")
a2_Label.config(fon = ("Times New Roman", 10))
a2_Label.grid(column=0, row=4)

#HEADING LABEL FOR PROJECTINFO

#AddEmp TAB
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Project Info")
tabControl.pack(expand=2, fill = "both")
ProjectInfo = ttk.LabelFrame(tab2, text='PROJECT Info')
ProjectInfo.grid(column=0,row=0,sticky='W')


b_Label = ttk.Label(ProjectInfo, text="Welcome to the Project Information Database")
b_Label.config(font = ("Times New Roman", 22))
b_Label.grid(column=0, row=29)

b1_Label = ttk.Label(ProjectInfo, text="Please Enter The Correct Employee Name")
b1_Label.config(font = ("Times New Roman", 10),justify="left")
b1_Label.grid(column=0, row=30)

#AddEmp TAB
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Add Employee")
tabControl.pack(expand=3, fill = "both")
AddEmp = ttk.LabelFrame(tab3, text='Add New Employee')
AddEmp.grid(column=0,row=0,sticky='W')

#HEADING LABEL FOR THE ADDEMPLOYEE TAB
c_Label = ttk.Label(AddEmp, text="Add EMPLOYEE")
c_Label.config(font = ("Times New Roman", 22))
c_Label.grid(column=0, row=1)

c1_Label = ttk.Label(AddEmp, text="You will be adding and employee onto the Database, please enter the details carefully")
c1_Label.config(font = ("Times New Roman", 10),justify="left")
c1_Label.grid(column=1, row=3)

#label for name_retuned
name_return_Label = ttk.Label(EmployeeInfo, text="Name")
name_return_Label.config(font = ("Times New Roman", 10))
name_return_Label.grid(column=1, row=5)

#label for position_returned
position_return_Label = ttk.Label(EmployeeInfo, text="Position")
position_return_Label.config(font = ("Times New Roman", 10))
position_return_Label.grid(column=1, row=6)

#label for rank_retuned
rank_return_Label = ttk.Label(EmployeeInfo, text="Rank")
rank_return_Label.config(font = ("Times New Roman", 10))
rank_return_Label.grid(column=1, row=10)

#label for contact_returned
contact_return_Label = ttk.Label(EmployeeInfo, text="Phone Number")
contact_return_Label.config(font = ("Times New Roman", 10))
contact_return_Label.grid(column=1, row=14)

#label for Email_retuned
email_return_Label = ttk.Label(EmployeeInfo, text="Email")
email_return_Label.config(font = ("Times New Roman", 10))
email_return_Label.grid(column=1, row=18)

#label for project_returned
proj_name_return_Label = ttk.Label(EmployeeInfo, text="Project Name")
proj_name_return_Label.config(font = ("Times New Roman", 10))
proj_name_return_Label.grid(column=1, row=22)

#label for supervisor_retuned
supervisor_return_Label = ttk.Label(EmployeeInfo, text="Supervisor Name")
supervisor_return_Label.config(font = ("Times New Roman", 10))
supervisor_return_Label.grid(column=1, row=26)

#CTC tab
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text="Current CTC")
tabControl.pack(expand=4, fill = "both")
CurrCTC = ttk.LabelFrame(tab4, text='Check Current CTC')
CurrCTC.grid(column=0,row=0,sticky='W')

#HEADING LABEL For the Check Current CTC tab1
d_Label = ttk.Label(CurrCTC, text="Check the Current CTC here")
d_Label.config(font = ("Times New Roman", 22))
d_Label.grid(column=0, row=1)



#==========================#
#Events                    #
#==========================#

#Button Click Event Function
def click_me():

    name_returned.delete(0, tk.END)
    position_returned.delete(0, tk.END)
    rank_returned.delete(0, tk.END)
    contact_returned.delete(0, tk.END)
    email_returned.delete(0, tk.END)
    project_returned.delete(0, tk.END)
    supervisor_returned.delete(0, tk.END)
    action.config(text="I have been clicked")
    #select name from Database taking input from user
    cursor.execute("SELECT Em_Name FROM Em_Info where Em_Name = %s",([name_entered.get()],))
    #select position from Database
    cursor1.execute("SELECT Em_Pos FROM Em_Info where Em_Name = %s",([name_entered.get()],))
    #select Rank from Database
    cursor2.execute("SELECT Em_Rank FROM Em_Info where Em_Name = %s",([name_entered.get()],))
    #Selct Contact number from Database
    cursor3.execute("SELECT Em_Con_Mob FROM Em_Info where Em_Name = %s",([name_entered.get()],))
    #select Email from Database
    cursor4.execute("SELECT Em_Con_Email FROM Em_Info where Em_Name = %s",([name_entered.get()],))
    #select Project Assigned from Database
    cursor5.execute("SELECT Em_Project_Assigned FROM Em_Info where Em_Name = %s",([name_entered.get()],))
    #select Employee Supervisor from Database
    cursor6.execute("SELECT Em_Supervisor FROM Em_Info where Em_Name = %s",([name_entered.get()],))

    data = cursor.fetchone()
    name_returned.insert(tk.INSERT, data)


    data1 = cursor1.fetchone()
    position_returned.insert(tk.INSERT, data1)


    data2 = cursor2.fetchone()
    rank_returned.insert(tk.INSERT, data2)


    data3 = cursor3.fetchone()
    contact_returned.insert(tk.INSERT, data3)


    data4 = cursor4.fetchone()
    email_returned.insert(tk.INSERT, data4)


    data5 = cursor5.fetchone()
    project_returned.insert(tk.INSERT, data5)


    data6 = cursor6.fetchone()
    supervisor_returned.insert(tk.INSERT, data6)

#New Button Event
def click_me1():
    proj_name_returned.delete(0, tk.END)
    action1.configure(text = 'working')
    #select Project name from Database taking input from user
    cursor7.execute("SELECT Em_Project_Assigned FROM Em_Info where Em_Name = %s",([p_name_entered.get()],))
    data7 = cursor7.fetchone()
    proj_name_returned.insert(tk.INSERT, data7)
#Another button Event

def click_me2():

    action2.configure(text='hey')
    cursor9.execute('INSERT into em_info (Em_Rank,Em_Name,Em_Pos,Em_Con_Mob,Em_Con_Email,Em_Project_Assigned,Em_Supervisor) values (%s, %s, %s, %s, %s, %s, %s)',(rank_inserted.get(),name_inserted.get(),position_inserted.get(),contact_inserted.get(),email_inserted.get(),proj_name_inserted.get(),supervisor_inserted.get(),))
    conn.commit();
    name_inserted.delete(0, tk.END)
    position_inserted.delete(0, tk.END)
    rank_inserted.delete(0, tk.END)
    contact_inserted.delete(0, tk.END)
    email_inserted.delete(0, tk.END)
    proj_name_inserted.delete(0, tk.END)
    supervisor_inserted.delete(0, tk.END)
    conn.commit();

def click_me3():

    ctc_returned.delete(0, tk.END)
    action3.configure(text='Hello There')
    cursor10 = conn.cursor()
    cursor10.execute('select @sum');

    data8 = cursor10.fetchone()
    ctc_returned.insert(tk.INSERT, data8)
#Exit GUI Cleanly Event
def _quit():
    win.quit()
    win.destroy()
    exit()

#Display an About messagebox Event
def _AboutmsgBox():
    msg.showinfo('DBMS MINI PROJECT','A GUI python Program which uses MySQL \n Made by Diwakar Ghoshal')

# Display a WARNING messagebox Event
def _WarningmsgBox():
    msg.showwarning('WARNING','This is a warning message, you are trying something which might break this program \n please dont do that')

# Display an ERROR messagebox event

def _ErrmsgBox():
    msg.showerror('Error','This is an error message, you made a mistake, oopsie')
#============================#
#Buttons                     #
#============================#

#Adding a Button
action = ttk.Button(EmployeeInfo, text="Click this for Emp", command=click_me)
action.grid(column=2, row=3, columnspan =3)

#Adding a Button
action1 = ttk.Button(ProjectInfo, text="Click this for Proj", command=click_me1)
action1.grid(column=2, row=30)

#Adding a Button
action2 = ttk.Button(AddEmp, text="Click this add Emp", command=click_me2)
action2.grid(column=2, row=4, columnspan =3)

#Adding a Button
action3 = ttk.Button(CurrCTC, text="Click this to see Current CTC", command=click_me3)
action3.grid(column=2, row=4, columnspan =3)
#=========================#
#Text Boxes               #
#=========================#

######################## TAB1 #######################################
#Adding a text box for accepting employee name from user for search function
name = tk.StringVar()
name_entered = ttk.Entry(EmployeeInfo, width = 20, textvariable=name)
name_entered.grid(column=1, row=3)

#Text Box for Name Return
name_return = tk.StringVar()
name_returned = ttk.Entry(EmployeeInfo, width = 20, textvariable=name_return)
name_returned.grid(column=2, row=5)

#Text Box for Position Return
pos_return = tk.StringVar()
position_returned = ttk.Entry(EmployeeInfo, width = 20, textvariable=pos_return)
position_returned.grid(column=2, row=6)

#Text Box for Name Return
rank_return = tk.StringVar()
rank_returned = ttk.Entry(EmployeeInfo, width = 20, textvariable=rank_return)
rank_returned.grid(column=2, row=10)

#Text Box for contact Return
contact_return = tk.StringVar()
contact_returned = ttk.Entry(EmployeeInfo, width = 20, textvariable=contact_return)
contact_returned.grid(column=2, row=14)

#Text Box for email Return
email_return = tk.StringVar()
email_returned = ttk.Entry(EmployeeInfo, width = 20, textvariable=email_return)
email_returned.grid(column=2, row=18)

#Text Box for project Return
proj_return = tk.StringVar()
project_returned = ttk.Entry(EmployeeInfo, width = 20, textvariable=proj_return)
project_returned.grid(column=2, row=22)

#Text Box for Supervisor Return
sup_return = tk.StringVar()
supervisor_returned = ttk.Entry(EmployeeInfo, width = 20, textvariable=sup_return)
supervisor_returned.grid(column=2, row=26)

#####################################################################

######################## TAB2 #######################################
#Adding a text box for accepting employee name from user for search function to find the Projects They are working on and other Information
p_name = tk.StringVar()
p_name_entered = ttk.Entry(ProjectInfo, width = 20, textvariable=p_name)
p_name_entered.grid(column=1, row=30)

#label for supervisor_retuned
p_name_return_Label = ttk.Label(ProjectInfo, text="Project Name")
p_name_return_Label.config(font = ("Times New Roman", 10))
p_name_return_Label.grid(column=2, row=32)

#Text Box for Project Return
proj_name_return = tk.StringVar()
proj_name_returned = ttk.Entry(ProjectInfo, width = 20, textvariable=proj_name_return)
proj_name_returned.grid(column=2, row=34)

#####################################################################

######################## TAB 3 #######################################
#label for name_insert
name_insert_Label = ttk.Label(AddEmp, text="Name")
name_insert_Label.config(font = ("Times New Roman", 10))
name_insert_Label.grid(column=1, row=5)

#text box for name_insert_Label
name_insert = tk.StringVar()
name_inserted = ttk.Entry(AddEmp, width = 20, textvariable=name_insert)
name_inserted.grid(column=2, row=5)

#label for position_insert
position_insert_Label = ttk.Label(AddEmp, text="Position")
position_insert_Label.config(font = ("Times New Roman", 10))
position_insert_Label.grid(column=1, row=6)

position_insert = tk.StringVar()
position_inserted = ttk.Entry(AddEmp, width = 20, textvariable=position_insert)
position_inserted.grid(column=2,row=6)


#label for rank_insert
rank_insert_Label = ttk.Label(AddEmp, text="Rank")
rank_insert_Label.config(font = ("Times New Roman", 10))
rank_insert_Label.grid(column=1, row=10)

rank_insert = tk.StringVar()
rank_inserted = ttk.Entry(AddEmp, width = 20, textvariable=rank_insert)
rank_inserted.grid(column=2,row=10)

#label for contact_insert
contact_insert_Label = ttk.Label(AddEmp, text="Phone Number")
contact_insert_Label.config(font = ("Times New Roman", 10))
contact_insert_Label.grid(column=1, row=14)


contact_insert = tk.StringVar()
contact_inserted = ttk.Entry(AddEmp, width = 20, textvariable=contact_insert)
contact_inserted.grid(column=2,row=14)

#label for Email_insert
email_insert_Label = ttk.Label(AddEmp, text="Email")
email_insert_Label.config(font = ("Times New Roman", 10))
email_insert_Label.grid(column=1, row=18)

email_insert = tk.StringVar()
email_inserted = ttk.Entry(AddEmp, width = 20, textvariable=email_insert)
email_inserted.grid(column=2,row=18)

#label for project_insert
proj_name_insert_Label = ttk.Label(AddEmp, text="Project Name")
proj_name_insert_Label.config(font = ("Times New Roman", 10))
proj_name_insert_Label.grid(column=1, row=20)

proj_name_insert = tk.StringVar()
proj_name_inserted = ttk.Entry(AddEmp, width = 20, textvariable=proj_name_insert)
proj_name_inserted.grid(column=2,row=20)

#label for supervisor_insert
supervisor_insert_Label = ttk.Label(AddEmp, text="Supervisor Name")
supervisor_insert_Label.config(font = ("Times New Roman", 10))
supervisor_insert_Label.grid(column=1, row=22)

supervisor_insert = tk.StringVar()
supervisor_inserted = ttk.Entry(AddEmp, width = 20, textvariable=supervisor_insert)
supervisor_inserted.grid(column=2,row=22)

###num = cursor8.execute('SELECT Em_Rank FROM em_info ORDER BY Slno DESC LIMIT 1')
###num = num+1;
###gar = tk.StringVar()
###garb = ttk.Entry(AddEmp, width = 20, textvariable=gar)
###garb.grid(column=2,row=22)
###garb.insert(tk.INSERT,num)

#####################################################################
##################################TAB 4###################################
#label for supervisor_retuned
ctc_return_Label = ttk.Label(CurrCTC, text="Name")
ctc_return_Label.config(font = ("Times New Roman", 10))
ctc_return_Label.grid(column=1, row=5)

#Text Box for Project Return
ctc_return = tk.StringVar()
ctc_returned = ttk.Entry(CurrCTC, width = 20, textvariable=ctc_return)
ctc_returned.grid(column=2, row=5)

#=========================#
#Menu Bar                 #
#=========================#

#creating a menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

#Option Menu
option_menu = Menu(menu_bar, tearoff=0)
option_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="Options", menu=option_menu)

#help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=_AboutmsgBox)
help_menu.add_command(label="Warning", command=_WarningmsgBox)
help_menu.add_command(label="Error",command=_ErrmsgBox)

#=============================#
#Start the GUI                #
#=============================#
win.mainloop()

conn.close()
