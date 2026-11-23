
import sqlite3

DB = 'inventory_sales_data.db'

conn = sqlite3.connect(DB)

cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS purchases_item")
cursor.execute("DROP TABLE IF EXISTS purchases")
cursor.execute("DROP TABLE IF EXISTS sales_item")
cursor.execute("DROP TABLE IF EXISTS sales")
cursor.execute("DROP TABLE IF EXISTS stock_moment")

conn.commit()

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

def add_product(product_name, price, qty, selling_price, buying_price, categories_id):

    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO product (
                product_name,
                price,
                qty,
                selling_price,
                buying_price,
                categories_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            product_name,
            price,
            qty,
            selling_price,
            buying_price,
            categories_id
        ))

        conn.commit()
     



def get_product():
     
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
              product.id,
              product.product_name,
              product.price,
              product.qty,
              product.selling_price,
              product.buying_price,
              categories.categories_name 
          FROM product
          JOIN categories
           ON product.categories_id = categories.id
        """)

        result = cursor.fetchall()
        return result
     

# categories table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY,
                categories_name VARCHAR(50)
                )
                 ''')

def add_categories(categories_name):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                        INSERT INTO categories (categories_name)
                        VALUES (?)
                         ''',(categories_name,))

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

     






 