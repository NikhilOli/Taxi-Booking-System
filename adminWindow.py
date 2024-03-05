import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector



class CustomCanvas(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        tk.Canvas.__init__(self, master, **kwargs)

    def set_image(self, image_path, foreground, background):
        original_image = Image.open(image_path)
        resized_image = original_image.resize((100, 70))
        self.image = ImageTk.PhotoImage(resized_image)
        self.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.configure(bg=background)

class AddDriverWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Add Driver")
        self.parent.geometry('800x600+360+100')
        self.parent.config(background='#dcdcdc')

        self.drivername_label = ttk.Label(parent, text='Driver Name:')
        self.drivername_label.pack(pady=10)
        self.drivername_entry = ttk.Entry(parent)
        self.drivername_entry.pack(pady=10)

        self.password_label = ttk.Label(parent, text='Password:')
        self.password_label.pack(pady=10)
        self.password_entry = ttk.Entry(parent, show='*')
        self.password_entry.pack(pady=10)

        self.email_label = ttk.Label(parent, text='Email:')
        self.email_label.pack(pady=10)
        self.email_entry = ttk.Entry(parent)
        self.email_entry.pack(pady=10)

        self.phone_label = ttk.Label(parent, text='Phone Number:')
        self.phone_label.pack(pady=10)
        self.phone_entry = ttk.Entry(parent)
        self.phone_entry.pack(pady=10)

        self.license_label = ttk.Label(parent, text='License Plate:')
        self.license_label.pack(pady=10)
        self.license_entry = ttk.Entry(parent)
        self.license_entry.pack(pady=10)

        self.register_button = ttk.Button(parent, text='Register', command=self.register_driver)
        self.register_button.pack(pady=20)

    def register_driver(self):
        drivername = self.drivername_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        license_plate = self.license_entry.get()

        # Perform validation if needed

        # Add driver to the database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxibookingsystem"
        )
        cursor = db_connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'driverinfo'")
        if not cursor.fetchone():
            cursor = db_connection.cursor()
            cursor.execute('''CREATE TABLE driverinfo (
                            BookingID INT AUTO_INCREMENT PRIMARY KEY,
                            drivername VARCHAR(255),
                            password VARCHAR(255),
                            email VARCHAR(255),
                            phone VARCHAR(255),
                            license_plate VARCHAR(255))''')
        try:
            query = "INSERT INTO driverinfo (drivername, password, email, phone, license_plate) VALUES (%s, %s, %s, %s, %s)"
            values = (drivername, password, email, phone, license_plate)
            cursor.execute(query, values)
            db_connection.commit()

            messagebox.showinfo("Success", "Driver added/registered successfully")
            self.parent.destroy()  # Close the add driver window after successful registration

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Error", f"Failed to add driver: {err}")

        finally:
            cursor.close()
            db_connection.close()

class AdminWindow:
    # Create the main window
    def __init__(self,adminWindow):
        self.adminWindow = adminWindow
        self.adminWindow.title("Driver Dashboard")
        self.adminWindow.geometry('1366x768')
        self.adminWindow.state('zoomed')
        self.adminWindow.config(background='#dcdcdc')


    #========Header=========================  
        self.header = tk.Frame(self.adminWindow, bg='#fff')
        self.header.place(x=0,y=0, width=1535, height=70, )
        # self.username = StringVar()
        # db_connection = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="",
        #     database="registration"
        # )
        # cursor = db_connection.cursor()
        # query = 'use registration'
        # cursor.execute(query)
        # query = "SELECT * FROM register_info WHERE username = %s"
        # cursor.execute(query)
        # username_data = cursor.fetchone()

        self.heading = ttk.Label(self.adminWindow,background='#fff', text=f'Welcome Back, Ankit', font=("Trebuchet MS", 20),)
        self.heading.place(x=200,y=15)
        
        # Create a custom canvas
        self.custom_canvas = CustomCanvas(self.header, width=100, height=70, bg='#fff', )
        self.custom_canvas.place(x=70, y=0)

        # Set image on the canvas with custom colors
        self.custom_canvas.set_image("Images/logo.png", foreground='#87CEEB', background='#fff')
        
        self.image_path = "Images/logout.png"
        original_image = Image.open(self.image_path)
        resized_image = original_image.resize((30, 25))
        self.image = ImageTk.PhotoImage(resized_image)

        # Create and display a label with the image
        self.image_label = tk.Button(self.header, image=self.image, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, command=self.logout, cursor='hand2')
        self.image_label.place(x=1390, y=25)

        self.logout_label = tk.Label(self.header, text='Logout', bg='#fff',fg='#87CEEB', font=('Tahoma',14), cursor='hand2')
        self.logout_label.place(x=1420, y=25)

        #====================SideBar===========================================================
        #===================================-----------------------------------------------------------------------------
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#fff', relief='ridge', padding=(60, 20, 20, 20))
        self.sidebar = ttk.Frame(self.adminWindow, style='TFrame')
        self.sidebar.place(x=0, y=72, width=320, height=750)

        #Dashboard   
        self.menu = ttk.Label(self.sidebar, text='MENU', background='#fff', foreground='#797979', font=('Trebuchet MS', 11, 'bold'))
        self.menu.place(x=35, y=10)
        self.image_path1 = "Images/layout.png"
        original_image1 = Image.open(self.image_path1)
        resized_image1 = original_image1.resize((35, 30))
        self.image1 = ImageTk.PhotoImage(resized_image1)
        self.image_1 = tk.Button(self.sidebar, image=self.image1, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_1.place(x=35, y=44)
        self.dashboardBtn = tk.Button(self.sidebar, text='Dashboard', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14, 'bold'))
        self.dashboardBtn.place(x=75, y=42)

        self.image_path2 = "Images/profile.png"
        original_image2 = Image.open(self.image_path2)
        resized_image2 = original_image2.resize((35, 30))
        self.image2 = ImageTk.PhotoImage(resized_image2)
        self.image_2 = tk.Button(self.sidebar, image=self.image2, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_2.place(x=35, y=94)
        self.profileBtn = tk.Button(self.sidebar, fg='#797979', text='Profile Management', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.profileBtn.place(x=75, y=92)

        self.image_path3 = "Images/trips.png"
        original_image3 = Image.open(self.image_path3)
        resized_image3 = original_image3.resize((35, 30))
        self.image3 = ImageTk.PhotoImage(resized_image3)
        self.image_3 = tk.Button(self.sidebar, image=self.image3, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_3.place(x=35, y=144)
        self.tripsBtn = tk.Button(self.sidebar, fg='#797979', text='Ride History', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.tripsBtn.place(x=75, y=142)

        self.image_path4 = "Images/completedtrip.png"
        original_image4 = Image.open(self.image_path4)
        resized_image4 = original_image4.resize((35, 30))
        self.image4 = ImageTk.PhotoImage(resized_image4)
        self.image_4 = tk.Button(self.sidebar, image=self.image4, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_4.place(x=35, y=194)
        self.completedtripsBtn = tk.Button(self.sidebar, fg='#797979', text='Manage Driver', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.completedtripsBtn.place(x=75, y=192)

        self.image_path5 = "Images/cancelledtrip.png"
        original_image5 = Image.open(self.image_path5)
        resized_image5 = original_image5.resize((35, 30))
        self.image5 = ImageTk.PhotoImage(resized_image5)
        self.image_5 = tk.Button(self.sidebar, image=self.image5, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_5.place(x=35, y=244)
        self.addDriverBtn = tk.Button(self.sidebar, fg='#797979', text='Add Driver', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,), command=self.open_add_driver_window,)
        self.addDriverBtn.place(x=75, y=242)

        self.image_path6= "Images/bookings.png"
        original_image6 = Image.open(self.image_path6)
        resized_image6 = original_image6.resize((35, 30))
        self.image6 = ImageTk.PhotoImage(resized_image6)
        self.image_6 = tk.Button(self.sidebar, image=self.image6, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_6.place(x=35, y=294)
        self.bookingsBtn = tk.Button(self.sidebar, fg='#797979', text='Bookings', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.bookingsBtn.place(x=75, y=292)
        
        self.image_path7= "Images/help.png"
        original_image7 = Image.open(self.image_path7)
        resized_image7 = original_image7.resize((35, 30))
        self.image7 = ImageTk.PhotoImage(resized_image7)
        self.image_7 = tk.Button(self.sidebar, image=self.image7, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_7.place(x=35, y=344)
        self.helpBtn = tk.Button(self.sidebar, fg='#797979', text='Help And Support', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.helpBtn.place(x=75, y=342)

        self.image_path8= "Images/resetpass.png"
        original_image8 = Image.open(self.image_path8)
        resized_image8 = original_image8.resize((35, 30))
        self.image8 = ImageTk.PhotoImage(resized_image8)
        self.image_8 = tk.Button(self.sidebar, image=self.image8, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_8.place(x=35, y=394)
        self.resetpassBtn = tk.Button(self.sidebar, fg='#797979', text='Reset Password', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.resetpassBtn.place(x=75, y=392)

        #TOP head Frames 
        self.topframe1 = tk.Frame(self.adminWindow, bg='#fff')
        self.topframe1.place(x=355, y=80, width=250, height=150)
        self.image_path9= "Images/totalride.png"
        original_image9 = Image.open(self.image_path9)
        resized_image9 = original_image9.resize((25, 25))
        self.image9 = ImageTk.PhotoImage(resized_image9)
        self.image_9 = tk.Button(self.topframe1, image=self.image9, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_9.place(x=30, y=20)
        self.ridelabel = tk.Label(self.topframe1, fg='#797979', text='Rides Completed', activebackground='#fff', background='#fff', font=('Tahoma', 14,))
        self.ridelabel.place(x=30, y=50)
        self.ridelabelamnt = tk.Label(self.topframe1, fg='#242424', text='2034', activebackground='#fff', background='#fff', font=('Tahoma', 18,))
        self.ridelabelamnt.place(x=30, y=80)

        self.topframe2 = tk.Frame(self.adminWindow, bg='#fff')
        self.topframe2.place(x=640, y=80, width=250, height=150)
        self.image_path10= "Images/cancelride.png"
        original_image10 = Image.open(self.image_path10)
        resized_image10 = original_image10.resize((25, 25))
        self.image10 = ImageTk.PhotoImage(resized_image10)
        self.image_10 = tk.Button(self.topframe2, image=self.image10, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_10.place(x=30, y=20)
        self.ridelabel = tk.Label(self.topframe2, fg='#797979', text='Rides Cancelled', activebackground='#fff', background='#fff', font=('Tahoma', 14,))
        self.ridelabel.place(x=30, y=50)
        self.ridelabelamnt = tk.Label(self.topframe2, fg='#242424', text='104', activebackground='#fff', background='#fff', font=('Tahoma', 18,))
        self.ridelabelamnt.place(x=30, y=80)

        self.topframe3 = tk.Frame(self.adminWindow, bg='#fff')
        self.topframe3.place(x=920, y=80, width=250, height=150)
        self.image_path11= "Images/ttldriver.png"
        original_image11 = Image.open(self.image_path11)
        resized_image11 = original_image11.resize((25, 25))
        self.image11 = ImageTk.PhotoImage(resized_image11)
        self.image_11 = tk.Button(self.topframe3, image=self.image11, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_11.place(x=30, y=20)
        self.ttldriverlabel = tk.Label(self.topframe3, fg='#797979', text='Total Drivers', activebackground='#fff', background='#fff', font=('Tahoma', 14,))
        self.ttldriverlabel.place(x=30, y=50)
        self.ttldriverlabelamt = tk.Label(self.topframe3, fg='#242424', text='10', activebackground='#fff', background='#fff', font=('Tahoma', 18,))
        self.ttldriverlabelamt.place(x=30, y=80)


        self.topframe4 = tk.Frame(self.adminWindow, bg='#fff')
        self.topframe4.place(x=1200, y=80, width=250, height=150)
        self.image_path12= "Images/avlbldriver.png"
        original_image12 = Image.open(self.image_path12)
        resized_image12 = original_image12.resize((25, 25))
        self.image12 = ImageTk.PhotoImage(resized_image12)
        self.image_12 = tk.Button(self.topframe4, image=self.image12, bg='#fff',fg='#87CEEB', activebackground='#fff', bd=0, cursor='hand2')
        self.image_12.place(x=30, y=20)
        self.availbldriverlabel = tk.Label(self.topframe4, fg='#797979', text='Available Drivers', activebackground='#fff', background='#fff', font=('Tahoma', 14,))
        self.availbldriverlabel.place(x=30, y=50)
        self.availbldriverlabelamt = tk.Label(self.topframe4, fg='#242424', text='7', activebackground='#fff', background='#fff', font=('Tahoma', 18,))
        self.availbldriverlabelamt.place(x=30, y=80)

        #Customer ENtry and Buttons Frame

        self.inputFrame = tk.Frame(self.adminWindow, bg='#fff')
        self.inputFrame.place(x=355, y=245, width=1100, height=220)
        
        #Button Frame and Buttons
        # Left Treeview
        self.left_treeview_frame = tk.Frame(self.inputFrame, highlightbackground='#87CEEB', highlightthickness=2, bg='#fff')
        self.left_treeview_frame.place(x=0, y=0, width=500, height=220)
        self.left_table = ttk.Treeview(self.left_treeview_frame, columns=('Booking ID', 'Pickup Address', 'Drop Address', 'Pickup Time', 'Pickup Date', 'Status'), show='headings')
        self.left_table.heading('Booking ID', text='BookingID')
        self.left_table.heading('Pickup Address', text='Pickup Address')
        self.left_table.heading('Drop Address', text='Drop Address')
        self.left_table.heading('Pickup Time', text='Pickup Time')
        self.left_table.heading('Pickup Date', text='Pickup Date')
        self.left_table.heading('Status', text='Status')
        

        self.left_table.pack(side='left', fill='y')
        self.update_table()

        left_scrollbar = ttk.Scrollbar(self.left_treeview_frame, orient="vertical", command=self.left_table.yview)
        left_scrollbar.pack(side="right", fill="y")
        self.left_table.configure(yscrollcommand=left_scrollbar.set)

        # Right Treeview
        self.right_treeview_frame = tk.Frame(self.inputFrame, highlightbackground='#87CEEB', highlightthickness=2, bg='#fff')
        self.right_treeview_frame.place(x=600, y=0, width=500, height=220)
        self.right_table = ttk.Treeview(self.right_treeview_frame, columns=('Booking ID', 'Pickup Address', 'Drop Address', 'Pickup Time', 'Pickup Date', 'Status'), show='headings')
        self.right_table.heading('Booking ID', text='BookingID')
        self.right_table.heading('Pickup Address', text='Pickup Address')
        self.right_table.heading('Drop Address', text='Drop Address')
        self.right_table.heading('Pickup Time', text='Pickup Time')
        self.right_table.heading('Pickup Date', text='Pickup Date')
        self.right_table.heading('Status', text='Status')

        self.right_table.pack(side='left', fill='y')

        right_scrollbar = ttk.Scrollbar(self.right_treeview_frame, orient="vertical", command=self.right_table.yview)
        right_scrollbar.pack(side="right", fill="y")
        self.right_table.configure(yscrollcommand=right_scrollbar.set)

        # Completed Button
        self.completed_button = tk.Button(self.inputFrame, text='Completed', command=self.complete_booking, font=('Trebuchet MS', 14), bd=0, bg='#87CEEB', fg='#fff', activebackground='#87CEEB', cursor='hand2')
        self.completed_button.place(x=525, y=90)
        db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxibookingsystem")
        cursor = db_connection.cursor()

        cursor.execute("SHOW TABLES LIKE 'driverdata'")
        if not cursor.fetchone():
            cursor = db_connection.cursor()
            cursor.execute('''CREATE TABLE driverdata (
                            BookingID INT AUTO_INCREMENT PRIMARY KEY,
                            pickupAddress VARCHAR(255),
                            dropAddress VARCHAR(255),
                            pickuptime VARCHAR(255),
                            pickupdate VARCHAR(255),
                            status VARCHAR(255))''')
        

        self.adminWindow.mainloop()
    
    def open_add_driver_window(self):
        add_driver_window = tk.Toplevel(self.adminWindow)
        AddDriverWindow(add_driver_window)


    def update_table(self):
        # Clear the existing rows in the table
        for item in self.left_table.get_children():
            self.left_table.delete(item)

        # Fetch and insert the latest data into the table
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxibookingsystem")

        cursor = db_connection.cursor()
        query = 'SELECT * FROM driverdata'
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            self.left_table.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))

    def complete_booking(self):
        selected_items = self.left_table.selection()
        status_index = self.left_table['columns'].index('Status')

        for item in selected_items:
            values = self.left_table.item(item, 'values')
            booking_id = values[0]

            # Update status in the database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxibookingsystem")

            cursor = db_connection.cursor()
            query = 'UPDATE driverdata SET Status = "Completed" WHERE BookingID = %s'
            cursor.execute(query, (booking_id,))
            db_connection.commit()

            # Move the selected row from the left table to the right table
            # self.right_table.insert("", "end", values=values)

            # Update status in the right table immediately
            values_with_completed_status = list(values)
            values_with_completed_status[status_index] = 'Completed'
            self.right_table.insert("", "end", values=values_with_completed_status)

            self.left_table.delete(item)

        # Update the left table after moving all selected rows
        self.update_table()

        cursor.close()
        db_connection.close()








            
        #CReating Treeview-------------------

        # self.treeviewframe = tk.Frame(self.adminWindow, highlightbackground='#87CEEB', highlightthickness=2, bg='#fff')
        # self.treeviewframe.place(x=355, y=480, width=1100, height=300)
        # self.table = ttk.Treeview(self.treeviewframe, columns= ('Booking ID', 'Pickup Address', 'Drop Address', 'Pickup Time', 'Pickup Date'), show='headings')
        # self.table.heading('Booking ID', text='BookingID')
        # self.table.heading('Pickup Address', text='Pickup Address')
        # self.table.heading('Drop Address', text='Drop Address')
        # self.table.heading('Pickup Time', text='Pickup Time')
        # self.table.heading('Pickup Date', text='Pickup Date')

        # self.table.pack(side='left', fill='y')

        # scrollbar = ttk.Scrollbar(self.treeviewframe, orient="vertical", command=self.table.yview)
        # scrollbar.pack(side="right", fill="y")
        # self.table.configure(yscrollcommand=scrollbar.set)


        # self.adminWindow.mainloop()  
    # # Start the Tkinter event loop

    # def reqRide(self):
    #     pickupAddress = self.pickupEntry.get()
    #     dropAddress = self.dropEntry.get()
    #     pickuptime = self.timeEntry.get()
    #     pickupdate = self.dateEntry.get()

    #     db_connection = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="",
    #         database="taxibookingsystem")
        
    #     cursor = db_connection.cursor()
    #     cursor.execute("SHOW TABLES LIKE 'bookingrequest'")
    #     if not cursor.fetchone():
    #         cursor.execute('''CREATE TABLE bookingrequest (
    #                         BookingID INT AUTO_INCREMENT PRIMARY KEY,
    #                         pickupAddress VARCHAR(255),
    #                         dropAddress VARCHAR(255),
    #                         pickuptime VARCHAR(255),
    #                         pickupdate VARCHAR(255))''')

    #     query = "INSERT INTO bookingrequest (pickupAddress, dropAddress, pickupdate, pickuptime) VALUES (%s, %s, %s, %s)"
    #     values = (pickupAddress, dropAddress, pickupdate, pickuptime)
    #     try:
    #         cursor.execute(query, values)
    #         db_connection.commit()
    #         messagebox.showinfo("Success", "Booking made successfully")
    #     except mysql.connector.Error as err:
    #         print(f"Error: {err}")
    #         messagebox.showerror("Error", f"Failed to make Booking: {err}")
    #     finally:
    #         cursor.close()
    #         db_connection.close()
    #     self.clear()
    #     self.update_table()

    # def update_table(self):
    #     # Clear the existing rows in the table
    #     for item in self.table.get_children():
    #         self.table.delete(item)

    #     # Fetch and insert the latest data into the table
    #     db_connection = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="",
    #         database="taxibookingsystem")

    #     cursor = db_connection.cursor()
    #     query = 'SELECT * FROM bookingrequest'
    #     cursor.execute(query)
    #     rows = cursor.fetchall()

    #     for row in rows:
    #         self.table.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))
            
    # def clear(self):
    #     self.pickupEntry.delete(0,tk.END)
    #     self.dropEntry.delete(0,tk.END)
    #     self.timeEntry.delete(0,tk.END)
    #     self.dateEntry.delete(0,tk.END)
    
    # def delete_items(self):
    #     for i in self.table.selection():
    #         self.table.delete(i)
        
    # def button_click(self):
    #     print("Button clicked!")

    def logout(self,):
        self.adminWindow.destroy()
        import login
    # Create  TTk widgets    
    
if __name__ == "__main__":
    adminWindow = tk.Tk()
    app = AdminWindow(adminWindow)
    adminWindow.mainloop()




