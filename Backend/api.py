
from Backend.main import register_user , verify_user , add_categories ,get_categories , add_customer ,get_customer ,add_product ,get_product ,add_purchases ,get_purchases ,add_purchases_item,get_purchases_item ,add_sales, get_sales ,add_sales_item ,get_sales_item ,add_stock_movement ,get_stock_movement ,add_supplier ,get_supplier
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

   return{
       "detiles" : detiles
   }


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

    return{
        "deitells":{
            deitells[0]
         
        }
      
    }
    