from sqlalchemy.orm import Session
from database_model import EmployeeDB


class EmployeeRepository:
    def __init__(self,db:Session):
        self.db = db


    def create(self,dictEmployeeInput:dict) -> EmployeeDB |None:
        new_Emp = EmployeeDB(**dictEmployeeInput)
        self.db.add(new_Emp)
        self.db.commit()
        self.db.refresh(new_Emp)
        return new_Emp


    def get(self,empID:int) -> EmployeeDB |None:
        empDict = self.db.query(EmployeeDB).filter_by(empID=empID).first()
        return empDict


    def update(self,dictEmployeeInput:dict,empID:int) -> EmployeeDB | None:

        db_Emp = self.db.query(EmployeeDB).filter_by(empID=empID).first()

        if not db_Emp:
            return None

        for key,value in dictEmployeeInput.items():
            if hasattr(db_Emp,key):
                setattr(db_Emp,key,value)

        self.db.commit()
        self.db.refresh(db_Emp)
        return db_Emp
