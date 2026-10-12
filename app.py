
from typing import Annotated
from fastapi import FastAPI,Depends
from database import engine,Base,get_db
from database_model import EmployeeDB
from sqlalchemy.orm import Session
from employee_service import EmployeeService
from employeeServices_repo import EmployeeRepository

app = FastAPI()



# @app.get("/")
# def greet():
#     return "wlecome to Employee management Dashboard"

## Below Lines of Code directly talking to Db Layer

# @app.get("/Employees")
# def get_all_Employees(db: Annotated[Session,Depends(get_db)]):
#     db_Employees = db.query(EmployeeDB).all()
#     return db_Employees

## Below Function will talk to Emp Service Layer (more Correct Architecture wise)
 
### Build a repository dependency Function :
def get_employee_repo(db:Annotated[Session,Depends(get_db)]):
    return EmployeeRepository(db=db)



@app.get("/Employees/{emp_id}")
def get_all_Employees(emp_id:int,repo: Annotated[EmployeeRepository,Depends(get_employee_repo)]):
    
    Services = EmployeeService(repository=repo)
    return Services.get_Employee(empID=emp_id)
    



