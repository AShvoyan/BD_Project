from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Date
from sqlalchemy.orm import declarative_base
import subprocess

Base = declarative_base()

class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, nullable=False)
    Name_Surname = Column(String(50), nullable=False, index=True) # to find faster, EATING RAM
    gpa = Column(Integer(20), nullable=True)
    age = Column(Integer, nullable=False)
    entry_year = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=True)


class Study(Base):
    __tablename__ = "study"
    
    id = Column(Integer, ForeignKey("Student.id"), primary_key=True, nullable=False)
    group_number = Column(Integer, nullable=False)
    scholarship = Column(Integer, nullable=True)
    speciality = Column(String(50), nullable=False)
    course = Column(Date)
    
    
class Faculcy(Base):
    __tablename__ = "faculcy"
    
    id = Column(Integer, ForeignKey("Student.id"), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    decan = Column(String(20), nullable=True)
    capacity = Column(Integer, nullable=True)
    
    