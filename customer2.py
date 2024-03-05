import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar  # For date/time picker

class TaxiBookingDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Taxi Booking Dashboard")

        # Title Label
        ttk.Label(master, text="Taxi Booking System", font=('Helvetica', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

        # Pickup Location
        ttk.Label(master, text="Pickup Location:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.pickup_entry = ttk.Entry(master)
        self.pickup_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Drop-off Location
        ttk.Label(master, text="Drop-off Location:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.dropoff_entry = ttk.Entry(master)
        self.dropoff_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # Date/Time Picker
        ttk.Label(master, text="Pickup Time:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.pickup_time_entry = ttk.Entry(master)
        self.pickup_time_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        # Calendar for date/time picker
        ttk.Button(master, text="Select Pickup Time", command=self.select_pickup_time).grid(row=4, column=0, columnspan=2, pady=10)

        # Book Now Button
        ttk.Button(master, text="Book Now", command=self.book_now).grid(row=5, column=0, columnspan=2, pady=20)

    def select_pickup_time(self):
        # You can customize the date/time picker implementation here
        cal = Calendar(self.master, selectmode='time', year=2023, month=12, day=12)
        cal.pack()
        cal.mainloop()

    def book_now(self):
        pickup_location = self.pickup_entry.get()
        dropoff_location = self.dropoff_entry.get()
        pickup_time = self.pickup_time_entry.get()

        # Perform booking logic here (communicate with a backend, etc.)
        # For this example, we'll just print the details
        print(f"Booking a trip from {pickup_location} to {dropoff_location} at {pickup_time}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaxiBookingDashboard(root)
    root.mainloop()
