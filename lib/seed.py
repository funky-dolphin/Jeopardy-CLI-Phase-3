from models import Base, Category, Point, Question
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



engine = create_engine("sqlite:///Jeopardy.db")
Base.metadata.create_all(bind = engine)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

session.query(Category).delete()
session.query(Point).delete()
session.query(Question).delete()

cat1 = Category(" ")
cat2 = Category(" ")
cat3 = Category(" ")
cat4 = Category(" ")
cat5 = Category(" ")

pt1 = Point(100)
pt2 = Point(200)
pt3 = Point(300)
pt4 = Point(400)
pt5 = Point(500)


q1 = Question("Where am I?", "IDK", cat1.category, pt1.points )
q2 = Question("Where am you?", "my house", cat2.category, pt2.points )
q3 = Question("Where am we?", "lost", cat1.category, pt3.points )

session.add_all([cat1, cat2, cat3, cat4, cat5])
session.add_all([pt1, pt2, pt3, pt4, pt5])
session.add_all([q1, q2, q3])

session.commit()
