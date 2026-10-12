
from sqlalchemy import Column,Integer,String,Float
from database import Base

class EmployeeDB(Base):
    __tablename__ = "empDataTable"

    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    empID = Column(Integer)
    empName = Column(String)
    empDepartment = Column(String)
    empSalary = Column(Integer)
    empExp = Column(Integer)

    

