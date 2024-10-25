import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",  
        user="your_username",  
        password="your_password",  
        database="laundry_management_db"  
    )
    cur = conn.cursor()
    # Create table if it doesn't exist
    cur.execute('''CREATE TABLE IF NOT EXISTS laundry (
                    laundry_id VARCHAR(255) PRIMARY KEY,
                    customer_name VARCHAR(255),
                    service_type VARCHAR(255),
                    contact VARCHAR(255),
                    address TEXT,
                    status VARCHAR(255))''')
    conn.commit()
    conn.close()

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="kanishk",  
            password="kanishk123",  
            database="laundry_management_db"
        )
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def add_laundry_entry(self, laundry_id, customer_name, service_type, contact, address, status):
        self.cur.execute('INSERT INTO laundry VALUES (%s, %s, %s, %s, %s, %s)',
                         (laundry_id, customer_name, service_type, contact, address, status))
        self.conn.commit()

    def update_laundry_entry(self, laundry_id, customer_name, service_type, contact, address, status):
        self.cur.execute('''UPDATE laundry SET customer_name=%s, service_type=%s, contact=%s, address=%s, status=%s
                           WHERE laundry_id=%s''',
                         (customer_name, service_type, contact, address, status, laundry_id))
        self.conn.commit()

    def delete_laundry_entry(self, laundry_id):
        self.cur.execute('DELETE FROM laundry WHERE laundry_id=%s', (laundry_id,))
        self.conn.commit()

    def search_laundry_entry(self, search_by, search_value):
        self.cur.execute(f'SELECT * FROM laundry WHERE {search_by} LIKE %s', ('%' + search_value + '%',))
        return self.cur.fetchall()

    def fetch_all_laundry_entries(self):
        self.cur.execute('SELECT * FROM laundry')
        return self.cur.fetchall()
