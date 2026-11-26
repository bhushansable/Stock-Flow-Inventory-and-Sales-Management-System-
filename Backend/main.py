
# import sqlite3

# DB = "inventory_sales_data.db"

# with sqlite3.connect(DB) as conn:
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM purchase_item")

#     re = cursor.fetchall()

#     print(re)



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

          return cursor.fetchall()

         


def delete_supplier(supplier_id):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                         DELETE  FROM supplier
                         WHERE id = ?
                          ''',(supplier_id,)
                          )
     

     

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

          return cursor.fetchall()

               

def delete_customer(customer_id):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                         DELETE  FROM customer
                         WHERE id = ?
                          ''',(customer_id,)
                          )


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

        return cursor.fetchall()


def delete_product(product_id):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                         DELETE  FROM product
                         WHERE id = ?
                          ''',(product_id,)
                          )
     
     

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

               return cursor.fetchall()



def delete_categories(categories_id):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                         DELETE  FROM categories  
                         WHERE id = ?
                          ''',(categories_id,)
                          )


#purchase_item


# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS purchase_item(
#         id INTEGER PRIMARY KEY,
#         supplier_id INTEGER NOT NULL,
#         product_id INTEGER NOT NULL,
#         purchase_date TEXT DEFAULT (DATE('now')),
#         qty INTEGER NOT NULL CHECK(qty > 0),
#         unit_cost INTEGER NOT NULL CHECK(unit_cost >= 0),
#         sub_total INTEGER NOT NULL,
        

#         FOREIGN KEY (supplier_id) REFERENCES supplier(id),
#         FOREIGN KEY (product_id) REFERENCES product(id)
# )
# """)



cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchase_item(
        id INTEGER PRIMARY KEY,
        supplier_id INTEGER,
        product_id INTEGER ,
        purchase_date TEXT DEFAULT (DATE('now')),
        qty INTEGER NOT NULL CHECK(qty > 0),
        unit_cost INTEGER NOT NULL CHECK(unit_cost >= 0),
        sub_total INTEGER NOT NULL,
        

        FOREIGN KEY (supplier_id) REFERENCES supplier(id),
        FOREIGN KEY (product_id) REFERENCES product(id)
)
""")


def purchase_item(name,email,address,phone_no,categories_name,product_name,price ,purchase_date,qty,unit_cost):

     sub_total = qty * unit_cost

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                          INSERT INTO supplier (name,email,address,phone_no)
                          VALUES (?,?,?,?)
                          ''',(name,email,address,phone_no)
                            )

          cursor.execute("""
                          SELECT id FROM supplier
                           WHERE name = ?
                         """, (name,))

          supplier_id = cursor.fetchone()
          supplier_id = supplier_id[0]

          cursor.execute('''
                         INSERT INTO categories (categories_name)
                          VALUES (?)
                            ''',(categories_name,))
          

          cursor.execute("""
                          SELECT id FROM categories
                           WHERE categories_name = ?
                         """, (categories_name,))

          categories_id = cursor.fetchone()
          categories_id = categories_id[0]

          cursor.execute('''
                      INSERT INTO product(product_name,price,categories_id )
                      VALUES (?,?,?)''', (product_name,price,categories_id)
                      )
          

          cursor.execute("""
                          SELECT id FROM product
                           WHERE product_name = ?
                         """, (product_name,))

          product_id = cursor.fetchone()
          product_id = product_id[0]

          cursor.execute(''' 
                         INSERT INTO purchase_item(supplier_id ,product_id,purchase_date,qty,unit_cost,sub_total)
                          VALUES (?,?,?,?,?,?)
                         ''',(supplier_id ,product_id,purchase_date,qty,unit_cost,sub_total)
                         )

          cursor.execute(''' 
                        UPDATE product
                        SET qty = ?
                        WHERE id = ?
                          ''',(qty,product_id))
          

          cursor.execute(''' 
                          UPDATE product
                          SET buying_price = ?
                          WHERE id = ?
                            ''',(sub_total,product_id))

          cursor.execute(''' 
                        UPDATE product
                        SET  selling_price = 5 + ?
                        WHERE id = ?
                          ''',(unit_cost,product_id)
                          )

          conn.commit()
         



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


def delete_purchase_item(purchase_item_id):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                         DELETE  FROM purchase_item  
                         WHERE id = ?
                          ''',(purchase_item_id,)
                          )
          

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_item(
        id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        sale_date TEXT DEFAULT (DATE('now')),
        qty INTEGER NOT NULL CHECK(qty > 0),
        unit_cost INTEGER NOT NULL CHECK(unit_cost >= 0),
        sub_total INTEGER NOT NULL,
        

        FOREIGN KEY (customer_id) REFERENCES customer(id),
        FOREIGN KEY (product_id) REFERENCES product(id)
)
""")




def sales_item(customer_id ,product_id,sale_date,qty,unit_cost):

     sub_total = qty * unit_cost

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()



          cursor.execute(''' 
                          UPDATE product
                          SET qty = qty - ?
                          WHERE id = ?
                          AND qty >= ?
                            ''',(qty,product_id,qty))

          

          if cursor.rowcount == 0:
               raise ValueError("stock is over")
          

          cursor.execute(''' 
                         INSERT INTO sales_item(customer_id ,product_id,sale_date,qty,unit_cost,sub_total)
                          VALUES (?,?,?,?,?,?)
                         ''',(customer_id ,product_id,sale_date,qty,unit_cost,sub_total)
                         )




def view_sales_item():

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()
          cursor.execute('''
                    SELECT
                          sales_item.id,
                          customer.name,
                          customer.address,
                          customer.phone_no,
                          product.product_name,
                          sales_item.sale_date,
                          sales_item.qty,
                          sales_item.unit_cost,
                          sales_item.sub_total

                    FROM sales_item
                    JOIN customer
                    ON sales_item.customer_id = customer.id

                    JOIN product
                    ON sales_item.product_id= product.id


                          ''')

          return cursor.fetchall()


def delete_sales_item(sales_item_id):

     with sqlite3.connect(DB) as conn:
          cursor = conn.cursor()

          cursor.execute('''
                         DELETE  FROM sales_item  
                         WHERE id = ?
                          ''',(sales_item_id,)
                          )




     






 