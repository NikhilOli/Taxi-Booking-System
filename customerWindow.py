import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
class BookingWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x500+300+150')
        self.root.title("Booking Page")
        self.root.config(background='#dcdcdc')

        # Create Treeview
        columns = ("SN", "Driver Name", "Vehicle Type", "Status", "Fare")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)  # Adjust the width as needed

        # Insert sample data
        self.insert_data()

        # Pack Treeview to the window
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Start the Tkinter event loop
        self.root.mainloop()

    def insert_data(self):
        # Sample data
        data = [
            ("1", "John Doe", "Sedan", "Available", "$20"),
            ("2", "Jane Smith", "SUV", "Busy", "$30"),
            ("3", "Bob Johnson", "Hatchback", "Offline", "$25"),
            # Add more rows as needed
        ]

        # Insert data into Treeview
        for row in data:
            self.tree.insert("", tk.END, values=row)



class CustomCanvas(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        tk.Canvas.__init__(self, master, **kwargs)

    def set_image(self, image_path, foreground, background):
        original_image = Image.open(image_path)
        resized_image = original_image.resize((100, 70))
        self.image = ImageTk.PhotoImage(resized_image)
        self.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.configure(bg=background)

class CustomerWindow:
    # Create the main window
    def __init__(self,customerWindow,username):
        self.customerWindow = customerWindow
        self.customerWindow.title("Customer Dashboard")
        self.customerWindow.geometry('1366x768')
        self.customerWindow.state('zoomed')
        self.customerWindow.config(background='#dcdcdc')


    #========Header=========================  
        self.header = tk.Frame(self.customerWindow, bg='#fff')
        self.header.place(x=0,y=0, width=1535, height=70, )

        self.heading = ttk.Label(self.customerWindow,background='#fff', text=f'Welcome Back, {username}', font=("Trebuchet MS", 20),)
        self.heading.place(x=200,y=15)
        
        # Create a custom canvas
        self.custom_canvas = CustomCanvas(self.header, width=100, height=70, bg='#fff', )
        self.custom_canvas.place(x=70, y=0)

        # Set image on the canvas with custom colors
        self.custom_canvas.set_image("Images/logo.png", foreground='#e45200', background='#fff')
        
        self.image_path = "Images/logout.png"
        original_image = Image.open(self.image_path)
        resized_image = original_image.resize((30, 25))
        self.image = ImageTk.PhotoImage(resized_image)

        # Create and display a label with the image
        self.image_label = tk.Button(self.header, image=self.image, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, command=self.logout, cursor='hand2')
        self.image_label.place(x=1390, y=25)

        self.logout_label = tk.Label(self.header, text='Logout', bg='#fff',fg='#e45200', font=('Tahoma',14), cursor='hand2')
        self.logout_label.place(x=1420, y=25)

        #====================SideBar===========================================================
        #===================================-----------------------------------------------------------------------------
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#fff', relief='ridge', padding=(60, 20, 20, 20))
        self.sidebar = ttk.Frame(self.customerWindow, style='TFrame')
        self.sidebar.place(x=0, y=72, width=320, height=750)

        #Dashboard   
        self.menu = ttk.Label(self.sidebar, text='MENU', background='#fff', foreground='#797979', font=('Trebuchet MS', 11, 'bold'))
        self.menu.place(x=35, y=10)
        self.image_path1 = "Images/layout.png"
        original_image1 = Image.open(self.image_path1)
        resized_image1 = original_image1.resize((35, 30))
        self.image1 = ImageTk.PhotoImage(resized_image1)
        self.image_1 = tk.Button(self.sidebar, image=self.image1, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_1.place(x=35, y=44)
        self.dashboardBtn = tk.Button(self.sidebar, text='Dashboard', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14, 'bold'))
        self.dashboardBtn.place(x=75, y=42)

        self.image_path2 = "Images/bookings.png"
        original_image2 = Image.open(self.image_path2)
        resized_image2 = original_image2.resize((35, 30))
        self.image2 = ImageTk.PhotoImage(resized_image2)
        self.image_2 = tk.Button(self.sidebar, image=self.image2, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_2.place(x=35, y=94)
        self.bookingsBtn = tk.Button(self.sidebar, fg='#797979', text='Bookings', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,), command=self.BookingWindow)
        self.bookingsBtn.place(x=75, y=92)

        self.image_path3 = "Images/trips.png"
        original_image3 = Image.open(self.image_path3)
        resized_image3 = original_image3.resize((35, 30))
        self.image3 = ImageTk.PhotoImage(resized_image3)
        self.image_3 = tk.Button(self.sidebar, image=self.image3, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_3.place(x=35, y=144)
        self.tripsBtn = tk.Button(self.sidebar, fg='#797979', text='Your Trips', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.tripsBtn.place(x=75, y=142)

        self.image_path4 = "Images/completedtrip.png"
        original_image4 = Image.open(self.image_path4)
        resized_image4 = original_image4.resize((35, 30))
        self.image4 = ImageTk.PhotoImage(resized_image4)
        self.image_4 = tk.Button(self.sidebar, image=self.image4, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_4.place(x=35, y=194)
        self.completedtripsBtn = tk.Button(self.sidebar, fg='#797979', text='Completed Trips', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.completedtripsBtn.place(x=75, y=192)

        self.image_path5 = "Images/cancelledtrip.png"
        original_image5 = Image.open(self.image_path5)
        resized_image5 = original_image5.resize((35, 30))
        self.image5 = ImageTk.PhotoImage(resized_image5)
        self.image_5 = tk.Button(self.sidebar, image=self.image5, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_5.place(x=35, y=244)
        self.completedtripsBtn = tk.Button(self.sidebar, fg='#797979', text='Cancelled Trips', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.completedtripsBtn.place(x=75, y=242)

        self.image_path6= "Images/profile.png"
        original_image6 = Image.open(self.image_path6)
        resized_image6 = original_image6.resize((35, 30))
        self.image6 = ImageTk.PhotoImage(resized_image6)
        self.image_6 = tk.Button(self.sidebar, image=self.image6, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_6.place(x=35, y=294)
        self.profileBtn = tk.Button(self.sidebar, fg='#797979', text='Profile', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.profileBtn.place(x=75, y=292)
        
        self.image_path7= "Images/help.png"
        original_image7 = Image.open(self.image_path7)
        resized_image7 = original_image7.resize((35, 30))
        self.image7 = ImageTk.PhotoImage(resized_image7)
        self.image_7 = tk.Button(self.sidebar, image=self.image7, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_7.place(x=35, y=344)
        self.helpBtn = tk.Button(self.sidebar, fg='#797979', text='Help And Support', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.helpBtn.place(x=75, y=342)

        self.image_path8= "Images/resetpass.png"
        original_image8 = Image.open(self.image_path8)
        resized_image8 = original_image8.resize((35, 30))
        self.image8 = ImageTk.PhotoImage(resized_image8)
        self.image_8 = tk.Button(self.sidebar, image=self.image8, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_8.place(x=35, y=394)
        self.resetpassBtn = tk.Button(self.sidebar, fg='#797979', text='Reset Password', activebackground='#fff', background='#fff', bd=0, font=('Trebuchet MS', 14,))
        self.resetpassBtn.place(x=75, y=392)

        #TOP head Frames 
        self.topframe1 = tk.Frame(self.customerWindow, bg='#fff')
        self.topframe1.place(x=355, y=80, width=250, height=150)
        self.image_path9= "Images/totalride.png"
        original_image9 = Image.open(self.image_path9)
        resized_image9 = original_image9.resize((25, 25))
        self.image9 = ImageTk.PhotoImage(resized_image9)
        self.image_9 = tk.Button(self.topframe1, image=self.image9, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_9.place(x=30, y=20)
        self.ridelabel = tk.Label(self.topframe1, fg='#797979', text='Rides Completed', activebackground='#fff', background='#fff', font=('Tahoma', 14,))
        self.ridelabel.place(x=30, y=50)
        self.ridelabelamnt = tk.Label(self.topframe1, fg='#242424', text='2034', activebackground='#fff', background='#fff', font=('Tahoma', 18,))
        self.ridelabelamnt.place(x=30, y=80)

        self.topframe2 = tk.Frame(self.customerWindow, bg='#fff')
        self.topframe2.place(x=640, y=80, width=250, height=150)
        self.image_path10= "Images/cancelride.png"
        original_image10 = Image.open(self.image_path10)
        resized_image10 = original_image10.resize((25, 25))
        self.image10 = ImageTk.PhotoImage(resized_image10)
        self.image_10 = tk.Button(self.topframe2, image=self.image10, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_10.place(x=30, y=20)
        self.ridelabel = tk.Label(self.topframe2, fg='#797979', text='Rides Cancelled', activebackground='#fff', background='#fff', font=('Tahoma', 14,))
        self.ridelabel.place(x=30, y=50)
        self.ridelabelamnt = tk.Label(self.topframe2, fg='#242424', text='104', activebackground='#fff', background='#fff', font=('Tahoma', 18,))
        self.ridelabelamnt.place(x=30, y=80)

        self.topframe3 = tk.Frame(self.customerWindow, bg='#fff')
        self.topframe3.place(x=920, y=80, width=250, height=150)
        self.image_path11= "Images/ttldriver.png"
        original_image11 = Image.open(self.image_path11)
        resized_image11 = original_image11.resize((25, 25))
        self.image11 = ImageTk.PhotoImage(resized_image11)
        self.image_11 = tk.Button(self.topframe3, image=self.image11, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_11.place(x=30, y=20)
        self.ttldriverlabel = tk.Label(self.topframe3, fg='#797979', text='Total Drivers', activebackground='#fff', background='#fff', font=('Tahoma', 14,))
        self.ttldriverlabel.place(x=30, y=50)
        self.ttldriverlabelamt = tk.Label(self.topframe3, fg='#242424', text='10', activebackground='#fff', background='#fff', font=('Tahoma', 18,))
        self.ttldriverlabelamt.place(x=30, y=80)


        self.topframe4 = tk.Frame(self.customerWindow, bg='#fff')
        self.topframe4.place(x=1200, y=80, width=250, height=150)
        self.image_path12= "Images/avlbldriver.png"
        original_image12 = Image.open(self.image_path12)
        resized_image12 = original_image12.resize((25, 25))
        self.image12 = ImageTk.PhotoImage(resized_image12)
        self.image_12 = tk.Button(self.topframe4, image=self.image12, bg='#fff',fg='#e45200', activebackground='#fff', bd=0, cursor='hand2')
        self.image_12.place(x=30, y=20)
        self.availbldriverlabel = tk.Label(self.topframe4, fg='#797979', text='Available Drivers', activebackground='#fff', background='#fff', font=('Tahoma', 14,))
        self.availbldriverlabel.place(x=30, y=50)
        self.availbldriverlabelamt = tk.Label(self.topframe4, fg='#242424', text='7', activebackground='#fff', background='#fff', font=('Tahoma', 18,))
        self.availbldriverlabelamt.place(x=30, y=80)

        #Customer ENtry and Buttons Frame
        self.inputFrame = tk.Frame(self.customerWindow, bg='#fff')
        self.inputFrame.place(x=355, y=245, width=1100, height=220)

        self.inputframe1 = tk.Frame(self.inputFrame, highlightbackground='#e45200', highlightthickness=2, bg='#fff')
        self.inputframe1.place(x=0, y=0, width=550, height=220,)

        self.pickupLabel = tk.Label(self.inputframe1, fg='#1E1B18', bg='#fff', text='Pickup Address', font=('Helvetica', 14)).grid(row=0,column=0, padx=10, pady=15)
        self.pickupEntry = tk.Entry(self.inputframe1, bg='#fff', width=24, highlightbackground='#e45200', bd=0, highlightthickness=1, font=('Helvetica', 12))
        self.pickupEntry.grid(row=1,column=0, padx=10, pady=(0,40))

        self.dropLabel = tk.Label(self.inputframe1, fg='#1E1B18', bg='#fff', text='Drop Address', font=('Helvetica', 14)).grid(row=0,column=1, padx=10, pady=15)
        self.dropEntry = tk.Entry(self.inputframe1, bg='#fff', width=24, highlightbackground='#e45200', bd=0, highlightthickness=1, font=('Helvetica', 12))
        self.dropEntry.grid(row=1,column=1, padx=10, pady=(0,40))

        self.timeLabel = tk.Label(self.inputframe1, fg='#1E1B18', bg='#fff', text='Pickup Time', font=('Helvetica', 14)).grid(row=3,column=0, padx=10, pady=15)
        self.timeEntry = tk.Entry(self.inputframe1, bg='#fff', width=24, highlightbackground='#e45200', bd=0, highlightthickness=1, font=('Helvetica', 12))
        self.timeEntry.grid(row=4,column=0, padx=10, pady=(0,40))

        self.dateLabel = tk.Label(self.inputframe1, fg='#1E1B18', bg='#fff', text='Pickup Date', font=('Helvetica', 14)).grid(row=3,column=1, padx=10, pady=15)
        self.dateEntry = tk.Entry(self.inputframe1, bg='#fff', width=24, highlightbackground='#e45200', bd=0, highlightthickness=1, font=('Helvetica', 12))
        self.dateEntry.grid(row=4,column=1, padx=10, pady=(0,40))
        
        #Button Frame and Buttons
        self.btnframe = tk.Frame(self.inputFrame, highlightbackground='#e45200', highlightthickness=2, bg='#fff')
        self.btnframe.place(x=550, y=0, width=550, height=220,)

        requestRide = tk.Button(self.btnframe, bd=1, text='Request Ride', background='#dcdcdc', highlightcolor="red", highlightthickness=2, activebackground='#e45200', fg='#e45200', font=('Tahoma', 14,), command=self.reqRide)
        requestRide.place(x=10, y=30)

        updateInfo = tk.Button(self.btnframe, bd=1, text='Update Info', background='#dcdcdc', highlightcolor="red", highlightbackground='pink', highlightthickness=2, activebackground='#e45200', fg='#e45200', font=('Tahoma', 14,),command=self.update_info)
        updateInfo.place(x=200, y=30)
        
        cancelBooking= tk.Button(self.btnframe, bd=1, text='Cancel Booking', background='#dcdcdc', highlightcolor="red", highlightthickness=2, activebackground='#e45200', fg='#e45200', font=('Tahoma', 14,), command=self.cancel_booking)
        cancelBooking.place(x=10, y=100)

        deleteBooking= tk.Button(self.btnframe, bd=1, text='Delete Booking', background='#dcdcdc', highlightcolor="red", highlightthickness=2, activebackground='#e45200', fg='#e45200', font=('Tahoma', 14,), command=self.delete_items)
        deleteBooking.place(x=200, y=100)

        editInfo= tk.Button(self.btnframe, bd=1, text='Edit Info', background='#dcdcdc', highlightcolor="red", highlightthickness=2, activebackground='#e45200', fg='#e45200', font=('Tahoma', 14,), command=self.edit_items)
        editInfo.place(x=370, y=100)
            
        #CReating Treeview-------------------

        self.treeviewframe = tk.Frame(self.customerWindow, highlightbackground='#e45200', highlightthickness=2, bg='#fff')
        self.treeviewframe.place(x=355, y=480, width=1100, height=300)
        self.table = ttk.Treeview(self.treeviewframe, columns= ('Booking ID', 'Pickup Address', 'Drop Address', 'Pickup Time', 'Pickup Date', 'status'), show='headings')
        self.table.heading('Booking ID', text='BookingID')
        self.table.heading('Pickup Address', text='Pickup Address')
        self.table.heading('Drop Address', text='Drop Address')
        self.table.heading('Pickup Time', text='Pickup Time')
        self.table.heading('Pickup Date', text='Pickup Date')
        self.table.heading('status', text='Status')

        self.table.pack(side='left', fill='y')

        scrollbar = ttk.Scrollbar(self.treeviewframe, orient="vertical", command=self.table.xview)
        scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=scrollbar.set)

        self.update_table()
        self.customerWindow.mainloop()  
        
    def reqRide(self):
        pickupAddress = self.pickupEntry.get()
        dropAddress = self.dropEntry.get()
        pickuptime = self.timeEntry.get()
        pickupdate = self.dateEntry.get()

        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxibookingsystem")
        
        cursor = db_connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'driverdata'")
        if not cursor.fetchone():
            cursor.execute('''CREATE TABLE driverdata (
                            BookingID INT AUTO_INCREMENT PRIMARY KEY,
                            pickupAddress VARCHAR(255),
                            dropAddress VARCHAR(255),
                            pickuptime VARCHAR(255),
                            pickupdate VARCHAR(255),
                            status VARCHAR(255))''')

        query = "INSERT INTO driverdata (pickupAddress, dropAddress, pickupdate, pickuptime, status) VALUES (%s, %s, %s, %s, %s)"
        values = (pickupAddress, dropAddress, pickupdate, pickuptime, 'pending')
        try:
            cursor.execute(query, values)
            db_connection.commit()
            messagebox.showinfo("Success", "Booking made successfully")
            self.update_table()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Error", f"Failed to make Booking: {err}")
        finally:
            cursor.close()
            db_connection.close()
        self.clear()
        

    def delete_items(self):
        selected_items = self.table.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "No item selected for deletion.")
            return

        confirmed = messagebox.askyesno("Confirmation", "Do you want to delete the selected booking(s)?")
        if not confirmed:
            return

        # Delete selected items from the database and update the table
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxibookingsystem")

        cursor = db_connection.cursor()
        for item in selected_items:
            booking_id = self.table.item(item, 'values')[0]
            query = f'DELETE FROM driverdata WHERE BookingID={booking_id}'
            cursor.execute(query)

        db_connection.commit()
        cursor.close()
        db_connection.close()

        # Update the table to reflect the changes
        self.update_table()
        messagebox.showinfo("Success", "Booking(s) deleted successfully.")

    def update_table(self):
        # Clear the existing rows in the table
        for item in self.table.get_children():
            self.table.delete(item)

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
            self.table.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    def update_info(self):
        # Get the selected item from the Treeview
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No item selected for update.")
            return

        # Get the updated data from entry widgets
        updated_pickup_address = self.pickupEntry.get()
        updated_drop_address = self.dropEntry.get()
        updated_pickup_time = self.timeEntry.get()
        updated_pickup_date = self.dateEntry.get()

        # Get the BookingID of the selected row
        booking_id = self.table.item(selected_item, 'values')[0]

        # Update the data in the database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxibookingsystem"
        )

        cursor = db_connection.cursor()
        query = "UPDATE driverdata SET pickupAddress=%s, dropAddress=%s, pickuptime=%s, pickupdate=%s WHERE BookingID=%s"
        values = (updated_pickup_address, updated_drop_address, updated_pickup_time, updated_pickup_date, booking_id)
        
        try:
            cursor.execute(query, values)
            db_connection.commit()
            messagebox.showinfo("Success", "Booking information updated successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Error", f"Failed to update booking information: {err}")
        finally:
            cursor.close()
            db_connection.close()

        # Update the Treeview to reflect the changes
        self.update_table()
        self.clear()

    def edit_items(self):
        # Get the selected item from the Treeview
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No item selected for editing.")
            return

        # Fetch data from the selected row
        selected_row_values = self.table.item(selected_item, 'values')

        # Check if entry widgets are not created, create them
        if not hasattr(self, 'pickupEntry'):
            self.pickupEntry = tk.Entry(self.inputframe1, bg='#fff', width=24, highlightbackground='#e45200', bd=0, highlightthickness=1, font=('Helvetica', 12))
            self.pickupEntry.grid(row=1, column=0, padx=10, pady=(0, 40))

        if not hasattr(self, 'dropEntry'):
            self.dropEntry = tk.Entry(self.inputframe1, bg='#fff', width=24, highlightbackground='#e45200', bd=0, highlightthickness=1, font=('Helvetica', 12))
            self.dropEntry.grid(row=1, column=1, padx=10, pady=(0, 40))

        if not hasattr(self, 'timeEntry'):
            self.timeEntry = tk.Entry(self.inputframe1, bg='#fff', width=24, highlightbackground='#e45200', bd=0, highlightthickness=1, font=('Helvetica', 12))
            self.timeEntry.grid(row=4, column=0, padx=10, pady=(0, 40))

        if not hasattr(self, 'dateEntry'):
            self.dateEntry = tk.Entry(self.inputframe1, bg='#fff', width=24, highlightbackground='#e45200', bd=0, highlightthickness=1, font=('Helvetica', 12))
            self.dateEntry.grid(row=4, column=1, padx=10, pady=(0, 40))

        # Set the fetched data to entry widgets for editing
        self.pickupEntry.delete(0, tk.END)
        self.pickupEntry.insert(0, selected_row_values[1])

        self.dropEntry.delete(0, tk.END)
        self.dropEntry.insert(0, selected_row_values[2])

        self.timeEntry.delete(0, tk.END)
        self.timeEntry.insert(0, selected_row_values[3])

        self.dateEntry.delete(0, tk.END)
        self.dateEntry.insert(0, selected_row_values[4])


    def cancel_booking(self):
        selected_items = self.table.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "No item selected for cancellation.")
            return

        confirmed = messagebox.askyesno("Confirmation", "Do you want to cancel the selected booking(s)?")
        if not confirmed:
            return

        # Cancel selected bookings in the database and update the table
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxibookingsystem")

        cursor = db_connection.cursor()
        for item in selected_items:
            booking_id = self.table.item(item, 'values')[0]
            query = f'UPDATE driverdata SET status="Cancelled" WHERE BookingID={booking_id}'
            cursor.execute(query)

        db_connection.commit()
        cursor.close()
        db_connection.close()

        # Update the table to reflect the changes
        self.update_table()
        messagebox.showinfo("Success", "Booking(s) cancelled successfully.")

        
    def BookingWindow(self):
        booking_window = BookingWindow()



    def clear(self):
        self.pickupEntry.delete(0,tk.END)
        self.dropEntry.delete(0,tk.END)
        self.timeEntry.delete(0,tk.END)
        self.dateEntry.delete(0,tk.END)
    
        
    def button_click(self):
        print("Button clicked!")

    def logout(self,):
        self.customerWindow.destroy()
        import login



    
if __name__ == "__main__":
    customerWindow = tk.Tk()
    app = CustomerWindow(customerWindow)
    customerWindow.mainloop()




