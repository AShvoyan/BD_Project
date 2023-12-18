from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Date, Float
from sqlalchemy.orm import declarative_base
import subprocess

Base = declarative_base()

class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, nullable=False)
    Name_Surname = Column(String(150), nullable=False, index=True) 
    gpa = Column(Float, nullable=False)
    age = Column(Integer, nullable=False)
    entry_year = Column(Integer, nullable=False)
    gender = Column(String(15), nullable=True)


class Study(Base):
    __tablename__ = "study"
    
    student_id = Column(Integer, ForeignKey("Student.id"), primary_key=True, nullable=False)
    faculty_id = Column(Integer, ForeignKey("Faculty.faculty_id"), nullable=False)
    group_number = Column(Integer, nullable=False)
    scholarship = Column(Integer, nullable=True)
    speciality = Column(String(50), nullable=False)
    course = Column(Date)
    
    
class Faculty(Base):
    __tablename__ = "faculty"
    
    faculty_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    decan = Column(String(20), nullable=True)
    capacity = Column(Integer, nullable=True)
    
    