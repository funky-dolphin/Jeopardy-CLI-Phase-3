from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Categories(Base):
    __tablename__ = "Categories"

    id = Column("Key", Integer, primary_key = True)
    category = Column("category", String)

    def __init__(self, category):
        self.category = category
        
    def __repr__(self):
        return f"({self.id} {self.category})"
    


    
