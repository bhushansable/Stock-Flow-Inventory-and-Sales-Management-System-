
import sqlite3

DB = 'inventory_sales_data.db'

conn = sqlite3.connect(DB)

cursor = conn.cursor()


# user table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
                )
                 ''')


def register_user(name,email,password):

    with sqlite3.connect(DB) as conn :
         cursor = conn.cursor()
         
         cursor.execute(''' 
                   INSERT INTO user (name, email, password)
                   VALUES (?,?,?)
                   ''',(name,email,password)
                   )

         conn.commit()


def verify_user(email,password):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute(''' 
                        SELECT email , password FROM user
                        WHERE email = ? AND password = ?
                        ''',(email,password)
                        )

          result = cursor.fetchone()

          if result:
               return result[0]

          else:
               None



# supplier table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS supplier(
                id INTEGER PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                email TEXT NOT NULL,
                address VARCHAR(100),
                phone_no INTEGER NOT NULL
                )
                 ''')


def add_supplier(name,email,address,phone_no):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                        INSERT INTO supplier (name,email,address,phone_no)
                        VALUES (?,?,?,?)
                         ''',(name,email,address,phone_no)
                         )

          conn.commit()      


def get_supplier():

     with sqlite3.connect(DB) as conn :
          cursor = conn.cursor()

          cursor.execute('''
                        SELECT * FROM supplier
                         ''')

          result = cursor.fetchall()

          if result:
               return result

          else:
               None

     

# customer table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS customer(
                id INTEGER PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                address VARCHAR(100),
                phone_no TEXT NOT NULL
                )
                 ''')


def add_customer(name,address,phone_no):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute( ''' 
                        INSERT INTO customer (name,address,phone_no)
                        VALUES (?,?,?)
                        ''',(name,address,phone_no)
                        )

          conn.commit()


def get_customer():

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute(''' 
                        SELECT * FROM customer                      
                         ''')

          result = cursor.fetchall()

          if result:
               return result

          else:
               None


# product table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS product(
                id INTEGER PRIMARY KEY,
                product_name VARCHAR(50),
                price INTEGER NOT NULL,
                qty INTEGER ,
                selling_price INTEGER,
                buying_price INTEGER,
                categories_id INTEGER,
                FOREIGN KEY ( categories_id ) REFERENCES categories(id)
                )
                 ''')

def add_product(name,price,qty,selling_price,buying_price,categoreies_id):
      
      with sqlite3.connect(DB) as conn:
               cursor = conn.cursor()

               cursor.execute('''
                            INSERT INTO product (name,price,qty,selling_price,buying_price,categoreies_id)
                            VALUES (?,?,?,?,?,?)
                                 ''',(name,price,selling_price,buying_price,categoreies_id)
                            )

               conn.commit()
     

def get_product():

      with sqlite3.connect(DB) as conn:
               cursor = conn.cursor()

               cursor.execute('''
                             SELECT * FROM product    
                             ''')

               result = cursor.fetchall()

               if result:
                     return result

               else:
                     None
     

# categories table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY,
                categories_name VARCHAR(50)
                )
                 ''')

def add_categories(name):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                        INSERT INTO categories (name)
                        VALUES (?)
                         ''',(name))

          conn.commit()

def get_categories():

      with sqlite3.connect(DB) as conn:
               cursor = conn.cursor()

               cursor.execute('''
                             SELECT * FROM categories      
                             ''')

               result = cursor.fetchall()

               if result:
                    return result

               else:
                    None

     

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

def add_purchases(user_id,supplier_id,total_amount):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                        INSERT INTO purchases (user_id,supplier_id,total_amount)
                        VALUES (?,?,?)
                         ''',(user_id,supplier_id,total_amount)
                         )

          conn.commit()

def get_purchases():

      with sqlite3.connect(DB) as conn:
               cursor = conn.cursor()

               cursor.execute('''
                             SELECT * FROM purchases      
                             ''')

               return cursor.fetchall()



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

def add_purchases_item(purchases_id,product_id,qty,unit_cost):

     sub_total = qty* unit_cost

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                        INSERT INTO purchases_item (purchases_id,product_id,qty,unit_cost)
                        VALUES (?,?,?,?,?)
                         ''',(purchases_id,product_id,qty,unit_cost,sub_total)
                         )

          conn.commit()

def get_purchases_item():

      with sqlite3.connect(DB) as conn:
               cursor = conn.cursor()

               cursor.execute('''
                             SELECT * FROM purchases_item   
                             ''')

               return cursor.fetchall()

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

def add_sales(user_id,customer_id , payment_method, total_amount):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                        INSERT INTO sales (user_id,customer_id , payment_method, total_amount)
                        VALUES (?,?,?,?)
                         ''',(user_id,customer_id,payment_method,total_amount)
                         )

          conn.commit()

def get_sales():

      with sqlite3.connect(DB) as conn:
               cursor = conn.cursor()

               cursor.execute('''
                             SELECT * FROM sales   
                             ''')
               
               return cursor.fetchall()

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

def add_sales_item(sales_id,product_id,qty,unit_cost,sub_total):

     sub_total = qty* unit_cost

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                        INSERT INTO sales_item (sales_id,product_id,qty,unit_cost,sub_total)
                        VALUES (?,?,?,?,?)
                         ''',(sales_id,product_id,qty,unit_cost,sub_total)
                         )

          conn.commit()

def get_sales_item():

      with sqlite3.connect(DB) as conn:
               cursor = conn.cursor()

               cursor.execute('''
                             SELECT * FROM sales_item   
                             ''')
               
               return cursor.fetchall()

            

# stock momvent
cursor.execute('''
                CREATE TABLE IF NOT EXISTS stock_moment(
                id INTEGER PRIMARY KEY,
                purchases_id INTEGER,
                sales_id INTEGER,
                product_id INTEGER,
                movement_type TEXT ,
                qty INTEGER,
                FOREIGN KEY  (purchases_id) REFERENCES purchases(id),
                FOREIGN KEY (sales_id) REFERENCES sales(id),         
                FOREIGN KEY  (product_id) REFERENCES product(id)
                
                )
                 ''')

def add_stock_movement(purchases_id,sales_id,product_id,movement_type,qty):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                        INSERT INTO stock_moment (purchases_id,sales_id,product_id,movement_type,qty)
                        VALUES (?,?,?,?,?)
                         ''',(purchases_id,sales_id,product_id,movement_type,qty)
                         )

          conn.commit()

def get_stock_movement():

      with sqlite3.connect(DB) as conn:
               cursor = conn.cursor()

               cursor.execute('''
                             SELECT * FROM stock_moment  
                             ''')

               return cursor.fetchall()

           


conn.commit()





 