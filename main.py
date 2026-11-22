#1.fastapi setup
from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
import sqlite3 #no need to install any sql from outside by default fastapi contain any sqls so,we need to import as our requirement
from pydantic import BaseModel,Field
from fastapi.responses import RedirectResponse

templates=Jinja2Templates(directory="templates")

app=FastAPI()

#2.setup of setrver-side-rendering    
@app.get('/')    
def home(req:Request):
    connection=get_connection()
    cursor=connection.cursor()
    q="select *from students"
    cursor.execute(q)
    data=cursor.fetchall()
    print(data)
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"students":data}
    )
#3.creating database,tables    
def get_connection():
    connection=sqlite3.connect(
        "student.db"
    )  
    return connection 
get_connection()  
#4.creating students table  in student database
def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    q = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        marks INTEGER,
        course TEXT,
        image TEXT,
        status INTEGER
    )
    """

    cursor.execute(q)
    connection.commit()
    connection.close()

create_table()
#5.create students form add into 
@app.get('/add-student')
def send_form(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="add-student.html",
        context={}
    )
class student(BaseModel):
    name:str=Field(min_length=4,max_length=20)
    age:int=Field(le=100,ge=18)
    gender:str
    marks:int=Field(le=100,ge=35)
    course:str
    image:str
    status:int    
#fetech the data from database    
@app.get("/student/{std_id}")   
def single_student(req:Request,std_id):
    connection=get_connection()
    cursor=connection.cursor()
    q=""" 
    select *from students where id=?
    """
    cursor.execute(q,(std_id,))
    std=cursor.fetchone()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="single-student.html",
        context={"student":std}
    )
@app.get("/std/delete/{std_id}")    
def delete_std(std_id):
    connection=get_connection()
    cursor=connection.cursor()
    q="delete from students where id=?"
    cursor.execute(q,(std_id,))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/",status_code=303)
#inserting data into database and represent to front-end client part
@app.post('/add-student')    
def add_student(
    name=Form(),
    age=Form(),
    gender=Form(),
    marks=Form(),
    course=Form(),
    image=Form(),
    status=Form()
    ):
    
    print(name,age,gender,marks,course,image,status)
    obj=student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )
    print(obj)
    std={
        "name":obj.name,
        "age":obj.age,
        "gender":obj.gender,
        "marks":obj. marks,
        "course":  obj.course,
        "image":obj.image,
        "status":obj.status,  
    }
    
    connection=get_connection()
    cursor=connection.cursor()
    q = """
    INSERT INTO students
    (name, age, gender, marks, course, image, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    cursor.execute(q, (name, age, gender, marks, course, image, status))
    connection.commit()
    connection.close()
    return RedirectResponse(url='/',status_code=303)

@app.get("/students/add")
def add_student(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="add-student.html",
        context={}
    )
    
    
@app.get("/students/update/{std_id}")
def update_form(req: Request, std_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    q = "SELECT * FROM students WHERE id=?"
    cursor.execute(q, (std_id,))

    student = cursor.fetchone()

    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="update-student.html",
        context={"student": student}
    )    
    


@app.post("/students/update/{std_id}")
def update_student(
    std_id: int,
    name: str = Form(),
    age: int = Form(),
    gender: str = Form(),
    marks: int = Form(),
    course: str = Form(),
    image: str = Form(),
    status: int = Form()
):
    connection = get_connection()
    cursor = connection.cursor()

    q = """
    UPDATE students
    SET name=?, age=?, gender=?, marks=?,
        course=?, image=?, status=?
    WHERE id=?
    """

    cursor.execute(q, (
        name,
        age,
        gender,
        marks,
        course,
        image,
        status,
        std_id
    ))

    connection.commit()
    connection.close()

    return RedirectResponse(
        url="/",
        status_code=303
    )
    
    

        
            
            
        
    