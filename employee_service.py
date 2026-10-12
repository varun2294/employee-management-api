from sqlalchemy.orm import Session
from employeeServices_repo import EmployeeRepository

class EmployeeService:

    
    ## Initialize 
    # def __init__(self,employees):
    #     self.employees = employees

    def __init__(self,repository):
        self.repository = repository

    # ## Add Employee Business Logic
    # def add_Employee(self,newEmp):
    #      self.employees.append(newEmp)
    #      return self.employees

    ## Add Employee Business Logic - Db Layer
    def add_Employee(self,newEmp):
            return self.repository.create(newEmp)
             


    # ## Search Employee using key &  Value - Business Logic
    # def search_Employee(self,field,value):
    #     result= [
    #             emp 
    #             for emp in self.repository
    #             if emp[field] == value
            
    #             ]    
        
    #     return result if result else None


    ## Get Employee Details  using id or name Business Logic
    # def get_Employee(self,**kwargs):

        
    #     for emp in self.repository:
    #         match = True
    #         for field,value in kwargs.items():
    #             if emp[field] != value:
    #                 match = False
    #                 break
    #         if match:
    #             return emp            
                
    ## Get Employee - post DB Layer implementation

    def get_Employee(self,empID:int):
         return self.repository.get(empID)

    # ## Update Employee Details usin id - Business logic
    # def update_Employee(self,empID,dictUpdateData):

    #     for emp in self.repository:
    #         if emp['employee_id'] == empID:
    #             for key,value in dictUpdateData.items():
    #                 emp[key] = value
    #             return emp
    #     return None
        
    ## Update DB -post DB Layer implementation
    def update_Employee(self,dictupdateData,empID):
         return self.repository.update(dictupdateData,empID)



             