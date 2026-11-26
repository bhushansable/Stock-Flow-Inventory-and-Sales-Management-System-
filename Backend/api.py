
from Backend.main import register_user , verify_user , add_categories ,get_categories , add_customer ,get_customer ,add_product ,get_product ,add_supplier ,get_supplier ,sales_item , view_sales_item , delete_supplier , delete_customer , delete_product , delete_categories , delete_sales_item ,purchase_item ,view_purchase_item  ,delete_purchase_item 
from fastapi import FastAPI,HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return{
        "Welcome stock-Flow"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=[ 
    "http://127.0.0.1:5500",
    "http://localhost:5500",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Register(BaseModel):
    name : str 
    email : str
    password : str


@app.post("/register")
def register(user : Register):
    register_user(
        user.name,
        user.email,
        user.password
    )

    return{
        "register successfull"
    }



class Login(BaseModel):
    email : str
    password : str


@app.post("/login")
def login(user : Login):
   detiles =  verify_user(
        user.email,
        user.password
    )

   return detiles


class Supplier(BaseModel):
    name : str
    email : str
    address : str
    phone_no : int


@app.post("/supplier")
def supplider(user:Supplier):
    add_supplier(
        user.name,
        user.email,
        user.address,
        user.phone_no
    )
    return{
        "supplier add successfuly"
    }

@app.get("/view_supplier")
def view_supplier():
    deitells = get_supplier()

    result = []
    if deitells:
            for row in deitells:
                result.append({
                "id": row[0],
                "name" : row[1],
                "email" : row[2],
                "address" : row[3],
                "phone no" : row[4]
            })


            return result

    else:
        return{
            "there is no supplier "
        }
        



@app.delete("/supplier/{supplier_id}")
def delete_supplier_(supplier_id : int):
    delete_supplier(supplier_id)

    return{
        "supplie delete succusefuly"
    }


class  Customer(BaseModel):

    name : str
    address : str
    phone_no : int


@app.post("/customer")
def customer(user:Customer):
    add_customer(
        user.name,
        user.address,
        user.phone_no
    )

    return{
        "customer add successfuly"
    }

@app.get("/view_customer")
def view_customer():
    deitells = get_customer()

    result = []

   
    if deitells:
        for row in deitells:
                    result.append({
                        "id": row[0],
                        "name" : row[1],
                        "address" : row[2],
                        "phone no" : row[3]
                    })
        
        return result

    else:
        return{
            "there is no customer"
        }


@app.delete("/customer/{customer_id}")
def customer_delete(customer_id : int):
    delete_customer(customer_id)

    return{
        "customer delete succesfully"
    }

     



class Product(BaseModel):
    product_name: str
    price: int
    qty: int
    selling_price: int
    buying_price: int
    categories_id: int

@app.post("/product")
def product(user:Product):
     add_product(
         user.product_name,
         user.price,
         user.qty,
         user.selling_price,
         user.buying_price,
         user.categories_id
    )

     return{
         "product add successfuly"
     }

  

@app.get("/get_product")
def view_product():
    result = get_product()

    products = []

    if result:
        for row in result:
                products.append({
                    "id": row[0],
                    "product_name": row[1],
                    "price": row[2],
                    "qty": row[3],
                    "selling_price": row[4],
                    "buying_price": row[5],
                    "category_name": row[6]
                })
        
        return products

    else:
        return{
            "there is no product"
        }

@app.delete("/product/{product_id}")
def delete_product_id( product_id : int):
    delete_product(product_id)

    return{
        "product delete successfuly"
    }


class Categories(BaseModel):
    categories_name : str

@app.post("/categories")
def categories(user : Categories):
    add_categories(
        user.categories_name
    )

    return{
        "add succesfully"
    }


@app.get("/get_categories")
def get__categories():
    deitels =  get_categories()

    result = []

    if deitels:
        for row in deitels:
                result.append({
                    "id": row[0],
                    "categories" : row[1]
                })
        
        return result

    else:
         return{
              "there is no categories"
         }

@app.delete("/categories/{categories_id}")
def delete_categories_id(categories_id : int):
    delete_categories(categories_id)

    return{
        "delete categories  successfuly"
    }


class Purchase_item(BaseModel):
     name : str
     email: str
     address : str
     phone_no : int 
     categories_name : str
     product_name : str
     price : int
     purchase_date : str
     qty : int
     unit_cost : int 

@app.post("/purchase_item")
def add_purchase_item(user : Purchase_item):
    purchase_item(
         user.name,
         user.email,
         user.address,
         user.phone_no,
         user.categories_name,
         user.product_name,
         user.price,
         user.purchase_date,
         user.qty,
         user.unit_cost
    )

    return{
        "add succesfully "
    }


@app.get("/purchase_item")

def get_purchase_item():
    reuslt = view_purchase_item()

    product = []

    if reuslt:
         for row in reuslt:
                 product.append({
                       "purchase_id": row[0],
                       "supplier": row[1],
                       "product": row[2],
                       "purchase_date": row[3],
                       "quantity": row[4],
                       "unit_cost": row[5],
                       "subtotal": row[6]
                 })
         
         return product

    else:
         return{
              "there is purchase no iteam"
         }

@app.delete("/purchase_item/{purchase_item_id}")
def purchase_item_delete(purchase_item_id : int):
     delete_purchase_item(purchase_item_id)

     return{
          "purchase_item delete successfuly"
     }


class Sales_iteam(BaseModel):
    customer_id : int
    product_id : int 
    sale_date : str 
    qty: int 
    unit_cost : int 

@app.post("/sales_item")
def add_sales_item(user : Sales_iteam):
    sales_item(
        user.customer_id,
        user.product_id,
        user.sale_date,
        user.qty,
        user.unit_cost
    )

    return{
        "add succesfully "
    }


@app.get("/sales_item")

def get_sales_item():
    reuslt = view_sales_item()

    product = []

    if reuslt:
         for row in reuslt:
                 product.append({
                       "sales_id": row[0],
                       "customer name ": row[1],
                       "customer address":row[2],
                       "customer phone no ":row[3],
                       "product": row[4],
                       "sale_date": row[5],
                       "quantity": row[6],
                       "unit_cost": row[7],
                       "subtotal": row[8]
                 })
         
         return product

    else:
         return{
              "there is no sales_iteam"
         }

@app.delete("/sales_item/{sales_item_id}")
def sales_item_delete(sales_item_id : int):
     delete_sales_item(sales_item_id)

     return{
          "sales_item delete successfuly"
     }
    

