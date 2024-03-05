import tkinter as tk
from tkinter import ttk
from register import SignUpPage
from customerWindow import CustomerWindow
from driverWindow import DriverWindow
from tkinter import messagebox
from PIL import Image, ImageTk 
import mysql.connector


bgcolor = '#E4FDE1'
redColor = '#ff5349'
class LoginPage():
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry('1000x500+300+150')
        # root.geometry('990x660')
        # ChangePassWIndow.geometry('600x440')
        self.root.title("Login Page")
        self.root.config(background=bgcolor)
        # root.eval("tk::PlaceWindow . center")
        # ChangePassWIndow.place(relx=0.5, rely=0.5, ANCHOR=CENTER)
        # bgImage = ImageTk.PhotoImage(file='red2.png')
        # root.wm_attributes('-transparentcolor','black')
        self.ChangePassWIndow = tk.Frame(self.root, width=700, height=460, bg=bgcolor)
        # ChangePassWIndow.pack_propagate(False)
        self.ChangePassWIndow.place(x=200, y=0)


        def user_enter(e):
            if self.username.get() == 'Username':
                self.username.delete(0,tk.END)

        def pass_enter(e):
            if self.password.get() == 'Password':   
                self.password.delete(0,tk.END)
                self.password.config(show='*')
        
        # Gui Widgets

        self.imageframe =tk.Frame(self.ChangePassWIndow, width=10, height=20, background='red').place(x=0, y=100)
        self.image_taxi = Image.open('Images/taxiimage.png')
        self.imageTk = ImageTk.PhotoImage(self.image_taxi)
        self.label = tk.Label(self.imageframe, text='Taxi', background=bgcolor, image=self.imageTk).place(y=100, x=0)
        
        #Option Bar
        self.combo = ttk.Combobox(self.ChangePassWIndow, values=['Customer', 'Driver', 'Admin'])
        self.combo.place(x=370, y=125)
        self.combo.bind('<<ComboboxSelected>>', self.comboFunction)
        self.combo.set("Select User Type")
        self.combo['state'] ='readonly'
        


        self.heading = tk.Label(self.ChangePassWIndow, text='Login your account', font=('bold', 30), bg=bgcolor, fg='#575761').place(x=370,y=50)
        # .grid(row=0, column=0, pady=40, columnspan=2)
        self.username = tk.Entry(self.ChangePassWIndow, width=22, bg=bgcolor, font=('bold', 15), bd=0, fg='#575761')
        self.username.place(x=370,y=165)
        self.username.insert(0,'Username')
        self.username.bind('<FocusIn>', user_enter)

        tk.Frame(self.ChangePassWIndow, width=250, height=2, background='#648381').place(x=368,y=190)
        # .place(x=300,y=158)a

        self.password = tk.Entry(self.ChangePassWIndow, width=22, bg=bgcolor, font=('bold', 15), bd=0, fg='#575761',)
        self.password.place(x=370,y=220)
        self.password.insert(0,'Password')
        self.password.bind('<FocusIn>', pass_enter)

        tk.Frame(self.ChangePassWIndow, width=250, height=2, background='#648381').place(x=370,y=245)

        self.forgetButton = tk.Button(self.ChangePassWIndow, text='Forgot Password?', fg='#575761', command=self.forget_pass, background=bgcolor, bd=0, activebackground=bgcolor, cursor='hand2', font=('bold',9) ).place(x=519,y=255)

        self.loginButton = tk.Button(self.ChangePassWIndow, text='Login', fg='#575761', width=19, command=self.login_user, background='#FFBF46', bd=0, activebackground='#575761', activeforeground=bgcolor, cursor='hand2', font=('bold',) ).place(x=380,y=290)

        self.noAccountBtn = tk.Button(self.ChangePassWIndow, text="Don't have an account?", fg='#575761', background=bgcolor, bd=0, activebackground=bgcolor, cursor='hand2', font=('bold',9) ).place(x=365,y=351)
        self.createAccountBtn = tk.Button(self.ChangePassWIndow, text="Create account", fg='blue', background=bgcolor, bd=0, activebackground=bgcolor, cursor='hand2', command=self.signup_page, font=('bold',11, 'underline') ).place(x=515,y=349)
        self.root.mainloop()

        #Functions 
    def comboFunction(self, e):
        print("Selected")

    def login_user(self):
        username = self.username.get()    
        password = self.password.get()
        if username == '' or password == '':
            messagebox.showerror("Error", "All fields are required")  
        else:
            try:
                db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxibookingsystem"
            )
                cursor = db_connection.cursor()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                messagebox.showerror("Error", f"Failed to register user: {err}")
                return
            query = 'use taxibookingsystem'
            cursor.execute(query)
            query = "SELECT * FROM register_info WHERE username = %s and password = %s"
            cursor.execute(query,(username,password))
            row = cursor.fetchone()

            if row is not None:
                messagebox.showinfo("Success", "Login is successful")
                self.root.destroy()
                customerWindow = tk.Tk()
                CustomerWindow(customerWindow, username)
                customerWindow.mainloop()
            else:
                # Check in driverinfo table
                query = "SELECT * FROM driverinfo WHERE drivername = %s AND password = %s"
                cursor.execute(query, (username, password))
                row = cursor.fetchone()

                if row is not None:
                    messagebox.showinfo("Success", "Login is successful")
                    self.root.destroy()
                    # Replace the following line with the appropriate class for the driver window
                    # For example, if you have a DriverWindow class, use DriverWindow(driver_window, username)
                    driverWindow = tk.Tk()
                    DriverWindow(driverWindow, username)
                    driverWindow.mainloop()
                else:
                    messagebox.showerror("Error", "Invalid username or password")

            db_connection.close()


    def forget_pass(self):
        class ForgotPasswordPage:
            def __init__(self):
                self.ChangePassWIndow = tk.Tk()
                self.ChangePassWIndow.geometry('690x460+450+150')
                self.ChangePassWIndow.title("Forgot Password")
                self.ChangePassWIndow.config(background='#BEA7E5')

                # Create a frame to hold the form elements
                frame = tk.Frame(self.ChangePassWIndow, bg='#BEA7E5')

                # Add labels and entry widgets
                self.heading = tk.Label(frame, text='Reset your password', font=('bold', 30), bg='#BEA7E5', fg='#271B16')
                self.heading.grid(row=0, column=0, pady=20, columnspan=2)

                username_label = tk.Label(frame, text="Username", width=18, bg='#BEA7E5', font=('bold', 15), fg='#271B16')
                username_label.grid(row=1, column=0, padx=20, sticky="e")

                self.username = tk.Entry(frame, width=22, bg='#BEA7E5', font=('bold', 15), bd=0, fg='#271B16')
                self.username.grid(row=2, column=0, columnspan=2,)

                tk.Frame(frame, width=250, height=2, background='black').grid(row=3, column=0, columnspan=2, pady=(0,15))

                password_label = tk.Label(frame, text="New Password", width=18, bg='#BEA7E5', font=('bold', 15), fg='#271B16')
                password_label.grid(row=4, column=0, padx=20, sticky="e")

                self.password = tk.Entry(frame, width=22, bg='#BEA7E5', font=('bold', 15), bd=0, fg='#271B16')
                self.password.grid(row=5, column=0, columnspan=2,)

                tk.Frame(frame, width=250, height=2, background='black').grid(row=6, column=0, columnspan=2, pady=(0,15))

                new_password_label = tk.Label(frame, text="Confirm Password", width=18, bg='#BEA7E5', font=('bold', 15), fg='#271B16')
                new_password_label.grid(row=7, column=0, padx=20, sticky="e")

                self.new_password = tk.Entry(frame, width=22, bg='#BEA7E5', font=('bold', 15), bd=0, fg='#271B16')
                self.new_password.grid(row=8, column=0, columnspan=2,)

                tk.Frame(frame, width=250, height=2, background='black').grid(row=9, column=0, columnspan=2, pady=(0,15))

                submit_button = tk.Button(frame, text="Submit", command=self.forget_password, fg='#271B16', width=19, background='#FFD6AF', bd=0, activebackground='#575761', activeforeground=bgcolor, cursor='hand2', font=('bold',))
                submit_button.grid(row=10, column=0, columnspan=2, pady=20)

                # Center the frame within the main window
                frame.pack(padx=20, pady=20)

            def forget_password(self):
                # Add your logic to handle the submission of the form
                if self.username.get() == '' or self.password.get() == '' or self.new_password.get() == '':
                    messagebox.showerror("Error", "All fields are required", parent =self.ChangePassWIndow)
                elif self.password.get() != self.new_password.get():
                    messagebox.showerror("Error","Password and Confirm Password not does not match",parent=self.ChangePassWIndow)
                else:
                    try:
                        db_connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="taxibookingsystem"
                    )
                    except mysql.connector.Error as err:
                        print(f"Error: {err}")
                        messagebox.showerror("Error", f"Failed to register user: {err}")
                        return
                    cursor =db_connection.cursor()
                    query=("SELECT * FROM register_info WHERE username = %s")
                    cursor.execute(query,(self.username.get(),))
                    row = cursor.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Incorrect Username", parent=self.ChangePassWIndow)
                    else:
                        query="update register_info set password=%s where username = %s"
                        cursor.execute(query, (self.password.get(), self.username.get()))
                        db_connection.commit()
                        db_connection.close()
                        messagebox.showinfo('Success', 'Password reset successfully, Please login with new password', parent=self.ChangePassWIndow)
                        self.ChangePassWIndow.destroy()
                            

            def run(self):
                # Run the Tkinter event loop
                self.ChangePassWIndow.mainloop()

        # Instantiate the ForgotPasswordPage class and run the GUI
        forgot_password_page = ForgotPasswordPage()
        forgot_password_page.run()

    def signup_page(self):
        self.root.destroy()
        SignUpPage()
        
LoginPage()