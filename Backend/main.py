
import sqlite3

DB = 'inventory_sales_data.db'

conn = sqlite3.connect(DB)

cursor = conn.cursor()



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


# purchase_item

cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchase_item(
        id INTEGER PRIMARY KEY,
        supplier_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        purchase_date TEXT DEFAULT (DATE('now')),
        qty INTEGER NOT NULL CHECK(qty > 0),
        unit_cost INTEGER NOT NULL CHECK(unit_cost >= 0),
        sub_total INTEGER NOT NULL,
        

        FOREIGN KEY (supplier_id) REFERENCES supplier(id),
        FOREIGN KEY (product_id) REFERENCES product(id)
)
""")


def purchase_item(supplier_id ,product_id,purchase_date,qty,unit_cost):

     sub_total = qty * unit_cost

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute(''' 
                         INSERT INTO purchase_item(supplier_id ,product_id,purchase_date,qty,unit_cost,sub_total)
                          VALUES (?,?,?,?,?,?)
                         ''',(supplier_id ,product_id,purchase_date,qty,unit_cost,sub_total)
                         )

          cursor.execute(''' 
                        UPDATE product
                        SET qty = qty + ?
                        WHERE id = ?
                          ''',(qty,product_id))
          
          cursor.execute(''' 
                          UPDATE product
                          SET buying_price = ?
                          WHERE id = ?
                            ''',(unit_cost,product_id))



def view_purchase_item():

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()
          cursor.execute('''
                    SELECT
                          purchase_item.id,
                          supplier.name,
                          product.product_name,
                          purchase_item.purchase_date,
                          purchase_item.qty,
                          purchase_item.unit_cost,
                          purchase_item.sub_total

                    FROM purchase_item
                    JOIN supplier
                    ON purchase_item.supplier_id = supplier.id

                    JOIN product
                    ON purchase_item.product_id= product.id


                          ''')

          return cursor.fetchall()





     






 