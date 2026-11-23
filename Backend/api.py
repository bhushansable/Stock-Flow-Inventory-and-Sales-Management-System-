
from Backend.main import register_user , verify_user , add_categories ,get_categories , add_customer ,get_customer ,add_product ,get_product ,add_supplier ,get_supplier
from fastapi import FastAPI,HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return{
        "Welcome stock-Flow"
    }


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

    return deitells


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

   
    return deitells
     



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

    return deitels
                
