from tkinter import *
from tkinter import messagebox
import sqlite3

f = ('Times', 14)

con = sqlite3.connect('userdata.db')    #Creating Rows and Columns of Databases
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    Name text, 
                    Email text, 
                    Contact number, 
                    Gender text, 
                    State text,
                    IFSC text,
                    Review text,
                    Rating text
                )
            ''')
con.commit()

            

ws = Tk()                                   #Initializing the tkinter window
ws.title('Customer FeedBack Form')
ws.geometry('1040x940')
ws.config(bg='#0B5A81')


def insert_record():                            #Function to insert values into databases
    check_counter=0
    warn = ""
    if register_name.get() == "":
       warn = "Name can't be empty"
    else:
        check_counter += 1
        
    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if register_mobile.get() == "":
       warn = "Contact can't be empty"
    else:
        check_counter += 1
    
    if  var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if variable.get() == "":
       warn = "Please Select Your State"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Please Enter IFSC Code"
    else:
        check_counter += 1
    
    if check_counter == 6:        
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :state, :IFSC, :Review,:Rating)", {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': var.get(),
                            'state': variable.get(),
                            'IFSC': register_pwd.get(),
                            'Review': register_review.get(),
                            'Rating': var1.get()

            })
            con.commit()
            messagebox.showinfo('confirmation', 'Your Form has been submitted')

        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)

var = StringVar()
var.set('male')                    #Default value for gender is male 

var1=StringVar()
var1.set('1')                      #Default value for Rating is 1

countries = []
variable = StringVar()
world = open('States.txt', 'r')
for country in world:
    country = country.rstrip('\n')
    countries.append(country)
variable.set(countries[22])

# widgets
right_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',
    relief=SOLID, 
    width=500,
    height=940
)

Label(
    right_frame, 
    text="Enter Name", 
    bg='#CCCCCC',
    font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Email", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Contact Number", 
    bg='#CCCCCC',
    font=f
    ).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Gender", 
    bg='#CCCCCC',
    font=f
    ).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select State", 
    bg='#CCCCCC',
    font=f
    ).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter IFSC Code", 
    bg='#CCCCCC',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Please Enter your review", 
    bg='#CCCCCC',
    font=f
    ).grid(row=6, column=0, sticky=W, pady=10)
Label(
        right_frame,
        text="Please rate our bank services",
        bg='#CCCCCC',
        font=f
    ).grid(row=7, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10, 
    pady=10,
    )

rating_frame=LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10, 
    pady=10,
)



register_name = Entry(
    right_frame, 
    font=f
    )

register_email = Entry(
    right_frame, 
    font=f,
)

register_mobile = Entry(
    right_frame, 
    font=f
    )


male_rb = Radiobutton(
    gender_frame, 
    text='Male',
    bg='#CCCCCC',
    variable=var,
    value='male',
    font=('Times', 10),
    
)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    bg='#CCCCCC',
    variable=var,
    value='female',
    font=('Times', 10),
  
)

others_rb = Radiobutton(
    gender_frame,
    text='Others',
    bg='#CCCCCC',
    variable=var,
    value='others',
    font=('Times', 10)
   
)

rate_1=Radiobutton(
    rating_frame,
    text='1',
    bg='#CCCCCC',
    variable=var1,
    value='1',
    font=('Times', 10)
)

rate_2=Radiobutton(
    rating_frame,
    text='2',
    bg='#CCCCCC',
    variable=var1,
    value='2',
    font=('Times', 10)
)

rate_3=Radiobutton(
    rating_frame,
    text='3',
    bg='#CCCCCC',
    variable=var1,
    value='3',
    font=('Times', 10)
)

rate_4=Radiobutton(
    rating_frame,
    text='4',
    bg='#CCCCCC',
    variable=var1,
    value='4',
    font=('Times', 10)
)

rate_5=Radiobutton(
    rating_frame,
    text='5',
    bg='#CCCCCC',
    variable=var1,
    value='5',
    font=('Times', 10)
)


register_country = OptionMenu(            
    right_frame, 
    variable, 
    *countries)

register_country.config(
    width=15, 
    font=('Times', 12)
)
register_pwd = Entry(
    right_frame, 
    font=f,
    
)

register_review=Entry(
    right_frame,
    font=f,
    width=50,
)

register_btn = Button(
    right_frame, 
    width=15, 
    text='Submit', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)


# widgets placement
register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20) 
register_mobile.grid(row=2, column=1, pady=10, padx=20)
register_country.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
register_review.grid(row=6,column=1,pady=10,padx=20)
register_btn.grid(row=8, column=1, pady=10, padx=20)
right_frame.pack(expand=1, fill=BOTH)

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)

rating_frame.grid(row=7, column=1, pady=10, padx=20)
rate_1.pack(expand=True, side=LEFT)
rate_2.pack(expand=True, side=LEFT)
rate_3.pack(expand=True, side=LEFT)
rate_4.pack(expand=True, side=LEFT)
rate_5.pack(expand=True, side=LEFT)

# infinite loop
ws.mainloop()