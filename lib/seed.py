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

cat1 = Category("Science")
cat2 = Category("Anime")
cat3 = Category("Bizarre History")
cat4 = Category("Finance")
cat5 = Category("Movie Quotes")

pt1 = Point(100)
pt2 = Point(200)
pt3 = Point(300)
pt4 = Point(400)
pt5 = Point(500)

sciq1 = Question("What is the bioling point of water in Feirhent?", "212", cat1.category, pt1.points )
sciq2 = Question("What gas comprises about 70 percent of the air we breathe?", "Nitrogen", cat1.category, pt2.points )
sciq3 = Question("What type of bond involves the sharing of electron pairs?", "Covalent", cat1.category, pt3.points )
sciq4 = Question("What binds oxygen to red blood cells?", "Hemaglobin", cat1.category, pt4.points )
sciq5 = Question("ATP is the molecular unit of energy. What does ATP stand for?", "Adenosine Triphosphate", cat1.category, pt5.points )

aniq1 = Question("", "", cat2.category, pt1.points)
aniq2 = Question("", "", cat2.category, pt2.points)
aniq3 = Question("", "", cat2.category, pt3.points)
aniq4 = Question("", "", cat2.category, pt4.points)
aniq5 = Question("", "", cat2.category, pt5.points)

bhq1 = Question("", "", cat3.category, pt1.points)
bhq2 = Question("", "", cat3.category, pt2.points)
bhq3 = Question("", "", cat3.category, pt3.points)
bhq4 = Question("", "", cat3.category, pt4.points)
bhq5 = Question("", "", cat3.category, pt5.points)

fiq1 = Question("", "", cat4.category, pt1.points)
fiq2 = Question("", "", cat4.category, pt2.points)
fiq3 = Question("", "", cat4.category, pt3.points)
fiq4 = Question("", "", cat4.category, pt4.points)
fiq5 = Question("", "", cat4.category, pt5.points)

mqq1 = Question("Leave the gun, take the cannoli's...", "The Godfather", cat5.category, pt1.points)
mqq2 = Question("But you merely adopted the dark; I was born in it, moulded by it... ", "The Dark Knight Rises", cat5.category, pt2.points)
mqq3 = Question("I ate his liver with some fava beans and a nice Chianti", "The Slience of the Lambs", cat5.category, pt3.points)
mqq4 = Question("It was Johnny Hopkins and Sloan Ketting. And they were blazing that sh*t up every day...", "Step Brothers", cat5.category, pt4.points)
mqq5 = Question("I like to move it, move it!", "Madagascar", cat5.category, pt5.points)


session.add_all([cat1, cat2, cat3, cat4, cat5])
session.add_all([pt1, pt2, pt3, pt4, pt5])
session.add_all([sciq1,sciq2,sciq3,sciq4,sciq5])

session.commit()
