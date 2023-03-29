from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    id = Column("Key", Integer, primary_key = True)
    category = Column("category", String)

    def __init__(self, category):
        self.category = category
        
    def __repr__(self):
        return f"({self.id} {self.category})"

class Point (Base):
    __tablename__ = "points"
    
    id  = Column("key", Integer, primary_key = True)
    points = Column("points", Integer)

    def __init__(self, points):
        self.points = points

    def __repr__(self):
        return f"({self.id} {self.points})"
    
class Question(Base):
    __tablename__ = "questions"

    id = Column("key", Integer, primary_key = True)
    question = Column("question", String)
    answer = Column("answer", String)
    category = Column(String, ForeignKey("categories.category"))
    point = Column (Integer, ForeignKey("points.points"))

    def __init__(self, question, answer, category, point):
        self.question = question
        self.answer = answer
        self.category = category
        self.point = point
        
    def __repr__(self):
        return f"{self.question} {self.answer} {self.category} {self.point}"
    
class Players(Base):
    __tablename__="players"

    id=Column("key", Integer, primary_key=True)
    player_name = Column("player_name", String)
    score = Column("score", Integer)

    def __init__(self, player_name, score):
        self.player_name = player_name
        self.score = score

    def __repr__(self):
        return f"{self.player_name} {self.score}"
