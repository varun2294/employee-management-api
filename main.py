from employee_service import EmployeeService
##from models import Employee
from database_model import EmployeeDB
from database import engine,Base,sessionLocal
from employeeServices_repo import EmployeeRepository
 
def main():

    employees =      [{
        "employee_id": 101,
         "name": "Amit",
         "department": "Engineering",
         "salary": 95000,
         "experience_years": 4
     }
    ]


    ## Input for add Employee Function
    newEmp =      {
            "employee_id": 105,
             "name": "Varun",
             "department": "AI",
             "salary": 96000,
             "experience_years": 8
         }


    


    ## create Employee Oject from model.py Employee class
    ##employee = Employee(employees)

    ## create empServices Object from EmployeeService Class
    # empServices = EmployeeService(employees)


    ## Invoke add Employee Function
    # addEmployee = empServices.add_Employee(newEmp)

    addEmployeeInDB = EmployeeService(employees)

    ## Input for Search Employee Function
    field = "name"
    value = "Amit"

    # ## Invoke Search employee Function
    # searchEmployee = empServices.search_Employee(field,value)


    # ## Invoke Get Employee Function
    # getEmployee = empServices.get_Employee(employee_id=101)

    # ##Invoke Update Employees Function
    # updateEmployee =empServices.update_Employee(101,
    #                                             {
    #                                                 "salary":96000

    #                                             })

    

    ## Invoke Databse_model.py
    
    ## NEVER EVER ENABLE BELOW Until you want to reset the Table from DB.
    ##Base.metadata.drop_all(bind=engine)


    Base.metadata.create_all(bind=engine)

    ## Map Dictionary Input of Employee Service before sending to DB Model Layer 
    db_Employee = {
        "empID":newEmp["employee_id"],
        "empName":  newEmp["name"],
        "empDepartment": newEmp["department"],
        "empSalary": newEmp["salary"],
        "empExp": newEmp["experience_years"]
    }

    

    # Invoke Repository Module
    db_Session = sessionLocal() 
    empRepo = EmployeeRepository(db=db_Session)

    Services = EmployeeService(empRepo)

    # addEmployeeInDB = Services.add_Employee(db_Employee)
    updateEmpInDB = Services.update_Employee(db_Employee,105)
    getEmpFromDB = Services.get_Employee(empID=105)


    # ## createEmpDB = empRepo.create(db_Employee)
    # getEmpFromDB = empRepo.get(empID=102)

    # updateEmpDB = empRepo.update(db_Employee,105)

    # ## Print Result for each Function
    print(getEmpFromDB)

if __name__ == "__main__":
    main()    