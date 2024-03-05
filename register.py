import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
purple = '#BEA7E5'
bgcolor = '#FFFAFF'
class SignUpPage():
    def __init__(self):
        self.root = tk.Tk()
        # self.registerWindow.title("Registration Page")
        self.root.title("Registration Page")
        # self.registerWindow.geometry('600x500')
        self.root.geometry('900x700+320+50')
        # self.registerWindow.config(background=bgcolor)
        self.root.config(background=bgcolor)
        self.heading = tk.Label(self.root, fg='#D8315B', text='Create New Account', bg=bgcolor, font=('Helvetica', 25))
        self.heading.place(relx=0.5, rely=0.08, anchor='center',)        
        
        self.frame = tk.Frame(self.root, background=bgcolor)
        self.frame.place(x=200, y=120, )
        
        self.usernameLabel = tk.Label(self.frame, fg='#1E1B18', bg=bgcolor, text='Username', font=('Helvetica', 14))
        self.usernameLabel.grid(row=0, column=0,)
        # self.usernameLabel.grid(row=0,column=0, padx=10, pady=(0,40), sticky='e')
        self.usernameEntry = tk.Entry(self.frame, bg=bgcolor, width=24, highlightbackground='#3E92CC', bd=0, highlightthickness=1, font=('Helvetica', 12))
        self.usernameEntry.grid(row=1, column=0, pady=(0,40))
        

        self.passwordLabel = tk.Label(self.frame, fg='#1E1B18', bg=bgcolor, text='Password', font=('Helvetica', 14)).grid(row=2,column=0, padx=10,)
        self.passwordEntry = tk.Entry(self.frame, bg=bgcolor, width=24, highlightbackground='#3E92CC', bd=0, highlightthickness=1, font=('Helvetica', 12))
        self.passwordEntry.grid(row=3,column=0, padx=10, pady=(0,40))
        
        self.cnfmpasswordLabel = tk.Label(self.frame, fg='#1E1B18', bg=bgcolor, text='Confirm Password', font=('Helvetica', 14)).grid(row=4,column=0, padx=10, )
        self.cnfmpasswordEntry = tk.Entry(self.frame, bg=bgcolor, width=24, highlightbackground='#3E92CC', bd=0, highlightthickness=1, font=('Helvetica',12 ))
        self.cnfmpasswordEntry.grid(row=5,column=0, padx=10, pady=(0,40)) 

        self.emailLabel = tk.Label(self.frame, fg='#1E1B18', bg=bgcolor, text='Email', font=('Helvetica', 14)).grid(row=6,column=0, padx=10,)
        self.emailEntry = tk.Entry(self.frame, width=24, highlightbackground='#3E92CC', bd=0, highlightthickness=1, font=('Helvetica', 12))
        self.emailEntry.grid(row=7,column=0, padx=10, pady=(0,40))

        self.addressLabel = tk.Label(self.frame, fg='#1E1B18', bg=bgcolor, text='Address', font=('Helvetica', 14)).grid(row=0,column=1, padx=10,)
        self.addressEntry = tk.Entry(self.frame, bg=bgcolor, width=24, highlightbackground='#3E92CC', bd=0, highlightthickness=1, font=('Helvetica', 12))
        self.addressEntry.grid(row=1,column=1, padx=10, pady=(0,40))

        self.genderLabel = tk.Label(self.frame, fg='#1E1B18', bg=bgcolor, text='Gender', font=('Helvetica', 14)).grid(row=4,column=1, padx=10,)
        self.gender = tk.StringVar()
        self.male = tk.Radiobutton(self.frame, text='Male', background=bgcolor, activebackground=bgcolor, variable=self.gender, value='Male', font=('Helvetica', 10))
        self.male.place(x=305,y=220)
        self.male.select()
        self.female = tk.Radiobutton(self.frame, text='Female', background=bgcolor, activebackground=bgcolor, variable=self.gender, value='Female',font=('Helvetica', 10))
        self.female.place(x=370,y=220)
        self.female.deselect()
        # self.genderEntry = tk.Entry(self.frame, bg=bgcolor, width=24, highlightbackground='#3E92CC', bd=0, highlightthickness=1, font=('Helvetica', 12))
        # self.genderEntry.grid(row=5,column=1, padx=10, pady=(0,40))

        self.telephoneLabel = tk.Label(self.frame, fg='#1E1B18', bg=bgcolor, text='Telephone No.', font=('Helvetica', 14)).grid(row=2,column=1, padx=10,)
        self.telephoneEntry = tk.Entry(self.frame, bg=bgcolor, width=24, highlightbackground='#3E92CC', bd=0, highlightthickness=1, font=('Helvetica', 12))
        self.telephoneEntry.grid(row=3,column=1, padx=10, pady=(0,40))

        # self.paymentLabel = tk.Label(self.frame, fg='#1E1B18', bg=bgcolor, text='Payment Method', font=('Helvetica', 14)).grid(row=6,column=1, padx=10,)
        # self.paymentEntry = tk.Entry(self.frame, bg=bgcolor, width=24, highlightbackground='#3E92CC', bd=0, highlightthickness=1, font=('Helvetica', 12))
        # self.paymentEntry.grid(row=7,column=1, padx=10, pady=(0,40))
        self.combo = ttk.Combobox(self.frame, values=['Cash', 'Online'], font=('Helvetica', 12))
        self.combo.grid(row=6, column=1)
        self.combo.bind('<<ComboboxSelected>>', self.comboFunction)
        self.combo.set("Payment Method")
        self.combo['state'] ='readonly'

        # self.emailLabel = tk.Label(self.frame, fg='#1E1B18', bg=bgcolor, text='Email', font=('Helvetica', 14)).grid(row=1,column=1, padx=10, pady=(0,40), pady=(1240))
        # self.emailEntry = tk.Entry(self.frame, width=24, highlightbackground='#3E92CC', bd=0, highlightthickness=1, font=('Helvetica', 12))
        # self.emailEntry.grid(row=2,column=1, padx=10, pady=(0,40))
        
        self.check = tk.IntVar()
        self.checkbtn = tk.Checkbutton(self.root, fg='#1E1B18', bg=bgcolor, text='I agree to the Terms & Conditions', variable=self.check, cursor='hand2', activebackground=bgcolor, activeforeground='#1E1B18', font=('Helvetica', 10, 'bold')).place(x=220, y=460)
        self.signupbtn = tk.Button(self.root, fg='#1E1B18', bd=0, bg='#7EB5DD', text='Signup', cursor='hand2', activebackground='#7EB5DD', width=20, activeforeground='#1E1B18', command=self.connect_database, font=('Open Sans', 14, 'bold')).place(x=310, y=495)

        self.dontHaveacnt = tk.Label(self.root, fg='#1E1B18', bg=bgcolor, text="Already have an acoount?", cursor='hand2', activebackground=bgcolor, activeforeground='#1E1B18', font=('Helvetica', 11, 'bold')).place(x=250, y=550)
        # self.registerWindow.mainloop()
        self.loginBtn = tk.Button(self.root, fg='blue', bg=bgcolor, text='Login', activebackground=bgcolor, activeforeground='blue', font=('Open Sans',14, 'underline', 'bold'), bd=0, cursor='hand2', command=self.login_page).place(x=445, y=545)
        self.root.mainloop()
    
        # self.center_frame(self.leftWindow)
        # self.center_frame(self.registerWindow)

    # def center_frame(self, frame):
    #     frame.grid_rowconfigure(0, weight=1)
    #     frame.grid_columnconfigure(0, weight=1)
        
    def login_page(self):
        self.root.destroy()
        from login import LoginPage
        LoginPage()
    def clear(self):
        self.emailEntry.delete(0,tk.END)
        self.usernameEntry.delete(0,tk.END)
        self.passwordEntry.delete(0,tk.END)
        self.cnfmpasswordEntry.delete(0,tk.END)
        self.addressEntry.delete(0,tk.END)
        self.male.select()
        self.combo.set("Payment Method")
        self.female.deselect()
        self.telephoneEntry.delete(0,tk.END)
        self.check.set(0)

    def connect_database(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        cnfmpassword = self.cnfmpasswordEntry.get()
        email = self.emailEntry.get()
        address = self.addressEntry.get()
        gender = self.gender.get()
        telephone = self.telephoneEntry.get()
        payment = self.combo.get()

        if username == '' or password == '' or cnfmpassword == '' or email == '' or address =='' or gender == '' or telephone == '' or payment == '':
            messagebox.showerror("Error", "All fields are required")
            return
        elif password != cnfmpassword:
            messagebox.showerror("Error", "Password Mismatch")
        elif self.check.get() == 0:
            messagebox.showerror("Error", "Please accept Terms & onditions")
        else:
            db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registration"
        )

        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()
        # Check if the username already exists in the database
        check_username_query = "SELECT * FROM register_info WHERE username = %s"
        cursor.execute(check_username_query, (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Error", "Username already exists. Choose a different username.")
        else:
            # Inserting data into a 'users' table
            query = "INSERT INTO register_info (username, password, email, address, telephone, gender, payment_method) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (username, password, email, address, telephone, gender, payment)

            try:
                cursor.execute(query, values)
                db_connection.commit()
                messagebox.showinfo("Success", "User registered successfully")
                self.clear()
                self.root.destroy()
                import login
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                messagebox.showerror("Error", f"Failed to register user: {err}")
            finally:
                cursor.close()
                db_connection.close()

    def comboFunction(self, e):
        print("Selected")
            
if __name__ == "__main__":
    SignUpPage()
