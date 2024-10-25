import tkinter as tk
from tkinter import ttk
from database import Database  # Importing the Database class from the database module

# ========== FUNCTION DEFINITIONS ========== #
class LaundryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")  
        self.root.title("Laundry Management System")

        # Title label
        title_label = tk.Label(self.root, text="Laundry Management System", font=("Arial", 30, "bold"), border=12, relief=tk.GROOVE, bg="lightblue")
        title_label.pack(side=tk.TOP, fill=tk.X)

        # Detail frame for entering details
        detail_frame = tk.LabelFrame(self.root, text="Enter Details", font=("Arial", 20), bd=12, relief=tk.GROOVE, bg="lightblue")
        detail_frame.place(x=20, y=90, width=420, height=575)

        # Data frame to display laundry data
        data_frame = tk.Frame(self.root, bd=12, bg="lightblue", relief=tk.GROOVE)
        data_frame.place(x=450, y=90, width=820, height=575)

        # ========== VARIABLES ========== #
        self.laundry_id = tk.StringVar()
        self.customer_name = tk.StringVar()
        self.service_type = tk.StringVar()
        self.contact = tk.StringVar()
        self.address = tk.StringVar()
        self.status = tk.StringVar()
        
        self.search_by = tk.StringVar(value="Laundry ID")  # Default value
        self.search_ent = tk.StringVar()

        # ====== ENTRY FIELDS ====== #
        self.create_entry_fields(detail_frame)

        # ========== BUTTONS ========== #
        self.create_buttons(detail_frame)

        # ========== SEARCH FRAME ========== #
        self.create_search_frame(data_frame)

        # ========== TREEVIEW (TABLE) ========== #
        self.create_table(data_frame)

        # Initial display of all laundry entries
        self.display_laundry_entries()

    def create_entry_fields(self, frame):
        # Entry labels and fields
        tk.Label(frame, text="Laundry ID", font=('Arial', 17), bg="lightblue").grid(row=0, column=0, padx=2, pady=2)
        tk.Entry(frame, bd=7, font=("Arial", 17), textvariable=self.laundry_id).grid(row=0, column=1, padx=2, pady=2)

        tk.Label(frame, text="Customer Name", font=('Arial', 17), bg="lightblue").grid(row=1, column=0, padx=2, pady=2)
        tk.Entry(frame, bd=7, font=("Arial", 17), textvariable=self.customer_name).grid(row=1, column=1, padx=2, pady=2)

        tk.Label(frame, text="Service Type", font=('Arial', 17), bg="lightblue").grid(row=2, column=0, padx=2, pady=2)
        tk.Entry(frame, bd=7, font=("Arial", 17), textvariable=self.service_type).grid(row=2, column=1, padx=2, pady=2)

        tk.Label(frame, text="Contact", font=('Arial', 17), bg="lightblue").grid(row=3, column=0, padx=2, pady=2)
        tk.Entry(frame, bd=7, font=("Arial", 17), textvariable=self.contact).grid(row=3, column=1, padx=2, pady=2)

        tk.Label(frame, text="Address", font=('Arial', 17), bg="lightblue").grid(row=4, column=0, padx=2, pady=2)
        tk.Entry(frame, bd=7, font=("Arial", 17), textvariable=self.address).grid(row=4, column=1, padx=2, pady=2)

        tk.Label(frame, text="Status", font=('Arial', 17), bg="lightblue").grid(row=5, column=0, padx=2, pady=2)
        ttk.Combobox(frame, font=("Arial", 17), state="readonly", textvariable=self.status, values=("Pending", "Completed", "Cancelled")).grid(row=5, column=1, padx=2, pady=2)

    def create_buttons(self, frame):
        btn_frame = tk.Frame(frame, bg="lightblue", bd=10, relief=tk.GROOVE)
        btn_frame.place(x=18, y=400, width=340, height=120)

        tk.Button(btn_frame, bg="lightblue", text="Add", bd=7, font=("Arial", 13), width=15, command=self.add_laundry_entry).grid(row=0, column=0, padx=2, pady=2)
        tk.Button(btn_frame, bg="lightblue", text="Update", bd=7, font=("Arial", 13), width=15, command=self.update_laundry_entry).grid(row=0, column=1, padx=3, pady=2)
        tk.Button(btn_frame, bg="lightblue", text="Delete", bd=7, font=("Arial", 13), width=15, command=self.delete_laundry_entry).grid(row=1, column=0, padx=2, pady=2)
        tk.Button(btn_frame, bg="lightblue", text="Clear", bd=7, font=("Arial", 13), width=15, command=self.clear_fields).grid(row=1, column=1, padx=3, pady=2)

    def create_search_frame(self, frame):
        search_frame = tk.Frame(frame, bg="lightblue", bd=10, relief=tk.GROOVE)
        search_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(search_frame, text="Search", font=("Arial", 17), bg="lightblue").grid(row=0, column=0, padx=2, pady=2)
        ttk.Combobox(search_frame, font=("Arial", 15), width=15, state="readonly", textvariable=self.search_by, values=("Laundry ID", "Customer Name")).grid(row=0, column=1, padx=2, pady=2)
        tk.Entry(search_frame, bd=7, font=("Arial", 15), textvariable=self.search_ent).grid(row=0, column=2, padx=2, pady=2)
        tk.Button(search_frame, bg="lightblue", text="Search", bd=7, font=("Arial", 13), width=12, command=self.search_laundry_entry).grid(row=0, column=3, padx=3, pady=2)
        tk.Button(search_frame, bg="lightblue", text="Show All", bd=7, font=("Arial", 13), width=12, command=self.display_laundry_entries).grid(row=0, column=4, padx=3, pady=2)

    def create_table(self, frame):
        table_frame = tk.Frame(frame, bg="lightblue", bd=10, relief=tk.GROOVE)
        table_frame.pack(fill=tk.BOTH, expand=True)

        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)

        self.laundry_table = ttk.Treeview(table_frame, columns=("laundry_id", "customer_name", "service_type", "contact", "address", "status"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x.config(command=self.laundry_table.xview)
        scroll_y.config(command=self.laundry_table.yview)

        self.laundry_table.heading("laundry_id", text="Laundry ID")
        self.laundry_table.heading("customer_name", text="Customer Name")
        self.laundry_table.heading("service_type", text="Service Type")
        self.laundry_table.heading("contact", text="Contact")
        self.laundry_table.heading("address", text="Address")
        self.laundry_table.heading("status", text="Status")
        self.laundry_table['show'] = 'headings'

        self.laundry_table.column("laundry_id", width=100)
        self.laundry_table.column("customer_name", width=150)
        self.laundry_table.column("service_type", width=120)
        self.laundry_table.column("contact", width=120)
        self.laundry_table.column("address", width=150)
        self.laundry_table.column("status", width=100)

        self.laundry_table.pack(fill=tk.BOTH, expand=True)

        # Bind selection event
        self.laundry_table.bind("<<TreeviewSelect>>", self.on_select)

    def add_laundry_entry(self):
        if not self.laundry_id.get() or not self.customer_name.get():
            print("Laundry ID and Customer Name are required!")
            return
        
        db = Database()
        try:
            db.add_laundry_entry(
                self.laundry_id.get(),
                self.customer_name.get(),
                self.service_type.get(),
                self.contact.get(),
                self.address.get(),
                self.status.get()
            )
            self.display_laundry_entries()  # Refresh the table after adding
            self.clear_fields()
        except Exception as e:
            print(f"Error adding laundry entry: {e}")

    def update_laundry_entry(self):
        if not self.laundry_id.get() or not self.customer_name.get():
            print("Laundry ID and Customer Name are required for update!")
            return
        
        db = Database()
        try:
            db.update_laundry_entry(
                self.laundry_id.get(),
                self.customer_name.get(),
                self.service_type.get(),
                self.contact.get(),
                self.address.get(),
                self.status.get()
            )
            self.display_laundry_entries()  # Refresh the table after updating
            self.clear_fields()
        except Exception as e:
            print(f"Error updating laundry entry: {e}")

    def delete_laundry_entry(self):
        if not self.laundry_id.get():
            print("Laundry ID is required for deletion!")
            return
        
        db = Database()
        try:
            db.delete_laundry_entry(self.laundry_id.get())
            self.display_laundry_entries()  # Refresh the table after deleting
            self.clear_fields()
        except Exception as e:
            print(f"Error deleting laundry entry: {e}")

    def search_laundry_entry(self):
        db = Database()
        search_key = self.search_ent.get()
        search_by = self.search_by.get().lower().replace(" ", "_")  # Normalize for DB search
        rows = db.search_laundry_entry(search_by, search_key)
        
        self.laundry_table.delete(*self.laundry_table.get_children())  # Clear current data
        for row in rows:
            self.laundry_table.insert('', 'end', values=row)

    def display_laundry_entries(self):
        db = Database()
        rows = db.fetch_all_laundry_entries()
        self.laundry_table.delete(*self.laundry_table.get_children())  # Clear current data
        for row in rows:
            self.laundry_table.insert('', 'end', values=row)

    def clear_fields(self):
        self.laundry_id.set("")
        self.customer_name.set("")
        self.service_type.set("")
        self.contact.set("")
        self.address.set("")
        self.status.set("")

    def on_select(self, event):
        selected_item = self.laundry_table.selection()[0]  # Get selected item
        item_values = self.laundry_table.item(selected_item, 'values')
        # Populate the entry fields with selected values
        self.laundry_id.set(item_values[0])
        self.customer_name.set(item_values[1])
        self.service_type.set(item_values[2])
        self.contact.set(item_values[3])
        self.address.set(item_values[4])
        self.status.set(item_values[5])

# Start Tkinter main loop
if __name__ == "__main__":
    from database import connect_db  # Ensure the database and table are created at startup
    connect_db()
    root = tk.Tk()
    app = LaundryManagementApp(root)
    root.mainloop()
