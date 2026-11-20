
import sqlite3

DB = 'inventory_sales_data.db'

conn = sqlite3.connect(DB)

cursor = conn.cursor()


# user table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY,
                name VANCHAR(50) NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
                )
                 ''')
# supplier table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS supplier(
                id INTEGER PRIMARY KEY,
                name VANCHAR(50) NOT NULL,
                email TEXT NOT NULL,
                address VANCHAR(100),
                phone_no TEXT NOT NULL
                )
                 ''')

# customer table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS customer(
                id INTEGER PRIMARY KEY,
                sales_item_id INTEGER,
                name VANCHAR(50) NOT NULL,
                address VANCHAR(100),
                phone_no TEXT NOT NULL,
                FOREIGN KEY ( sales_item_id) REFERENCES sales_item(id)
                )
                 ''')

# product table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS product(
                id INTEGER PRIMARY KEY,
                product_name VANCHAR(50),
                price INTEGER NOT NULL,
                qty INTEGER ,
                selling_price INTEGER,
                buying_price INTEGER,
                categories_id INTEGER,
                FOREIGN KEY ( categories_id ) REFERENCES categories(id)
                )
                 ''')

# categories table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY,
                categories_name VANCHAR(50)
                )
                 ''')


# purchases table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS purchases(
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                supplier_id INTEGER,
                total_amount INTEGER,
                FOREIGN KEY ( user_id ) REFERENCES user(id) ,
                FOREIGN KEY (  supplier_id ) REFERENCES supplier(id)
                )
                 ''')

# purchases_item table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS purchases_item(
                id INTEGER PRIMARY KEY,
                purchases_id INTEGER,
                product_id INTEGER,
                qty INTEGER,
                unit_cost INTEGER,
                sub_total INTEGER,
                FOREIGN KEY (purchases_id) REFERENCES purchases(id), 
                FOREIGN KEY (product_id) REFERENCES product(id)
                )
                 ''')

# sales table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS sales(
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                customer_id INTEGER,
                payment_method TEXT NOT NULL,
                total_amount INTEGER,
                FOREIGN KEY (user_id) REFERENCES user(id) ,
                FOREIGN KEY (customer_id) REFERENCES customer(id)
                )
                 ''')

# sales_item
cursor.execute('''
                CREATE TABLE IF NOT EXISTS sales_item(
                id INTEGER PRIMARY KEY,
                sales_id INTEGER,
                product_id INTEGER,
                qty INTEGER,
                unit_cost INTEGER,
                sub_total INTEGER,
                FOREIGN KEY (sales_id) REFERENCES sales(id),
                FOREIGN KEY (product_id) REFERENCES product(id)
                )
                 ''')

# stock momvent
cursor.execute('''
                CREATE TABLE IF NOT EXISTS stock_moment(
                id INTEGER PRIMARY KEY,
                purchases_id INTEGER,
                sales_id INTEGER,
                product_id INTEGER,
                movement_type TEXT ,
                FOREIGN KEY  (purchases_id) REFERENCES purchases(id),
                FOREIGN KEY (sales_id) REFERENCES sales(id),         
                FOREIGN KEY  (product_id) REFERENCES product(id)
                
                )
                 ''')


conn.commit()


