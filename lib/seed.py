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

sciq1 = Question("What is the boiling point of water in fahrenheit?", "212", cat1.category, pt1.points )
sciq2 = Question("What gas comprises about 70 percent of earth's atmosphere?", "Nitrogen", cat1.category, pt2.points )
sciq3 = Question("What type of bond involves the sharing of electron pairs?", "Covalent", cat1.category, pt3.points )
sciq4 = Question("Issac Newton had three laws of motion.  What is his second law of motion, commonly expressed in a simple mathmatical expression?" , "F = m*a", cat1.category, pt4.points )
sciq5 = Question("ATP is the molecular unit of energy. What does ATP stand for?", "Adenosine Triphosphate", cat1.category, pt5.points )

aniq1 = Question("What is the name of Goku's Saiyan rival?", "Vegeta", cat2.category, pt1.points)
aniq2 = Question("What is the name of the genius tactician in Naruto's generation?", "Shikamaru", cat2.category, pt2.points)
aniq3 = Question("What is the name of Izuku Midoriya's quirk? ", "One for all", cat2.category, pt3.points)
aniq4 = Question("What is Nico Robin's role in the Straw Hat's Pirate Crew?", "Archaeologist", cat2.category, pt4.points)
aniq5 = Question("What is the name of the first villian to show up in One Punch Man", "Vaccine man", cat2.category, pt5.points)

bhq1 = Question("Around 300 million years ago, earth's land masses existed as a supercontinent.  What was this landmass called?", "Pangea", cat3.category, pt1.points)
bhq2 = Question("The start of World War I is is commonly said to have started of due to the assination of this Austrian Archduke.", "Franz Ferdinand", cat3.category, pt2.points)
bhq3 = Question("What was the name of this Eurasian trade route active from the 2nd Centure BCE to the mid 15th Century responsible for the global distribution of goods?", "The Silk Road", cat3.category, pt3.points)
bhq4 = Question("Civil Rights activist Martin Luther King Jr was assinated in this city.", "Memphis", cat3.category, pt4.points)
bhq5 = Question("The Black Plague is known as of the most devastating global epidemics to date. It spread via a zoonotic bacteria carried by fleas on the the backs of traveling rats.  What is the name of this bacteria?", "Yersinia pestis", cat3.category, pt5.points)

fiq1 = Question("Founded in 1971, the National Association of Securities Dealers Automated Quotations is better known as what stock exchange?", "NASDAQ", cat4.category, pt1.points)
fiq2 = Question("What “S” venture capital firm, founded in 1972 by Donald Valentine in Menlo Park, CA, shares its name with a large tree species that is one of the redwood tree types.", "Sequoia Capital", cat4.category, pt2.points)
fiq3 = Question("Former J.P. Morgan Chase employee Bruno Iksil acquired what large mammalian nickname after losing the company a staggering $6.2 billion with a 2012 trade?", "London Whale", cat4.category, pt3.points)
fiq4 = Question("Also known as an acid test, what 'rapid' two-word term means an indicator of a company’s short-term liquidity position, which measures a company’s ability to meet its short-term obligations with its most liquid assets?", "Quick ratio", cat4.category, pt4.points)
fiq5 = Question("In the wake of the 2008 financial crisis, the federal government instituted TARP, which stood for 'Troubled ___ Relief Program.' What word goes in the blank?", "Asset", cat4.category, pt5.points)

mqq1 = Question("Leave the gun, take the cannoli's...", "The Godfather", cat5.category, pt1.points)
mqq2 = Question("But you merely adopted the dark; I was born in it, moulded by it... ", "The Dark Knight Rises", cat5.category, pt2.points)
mqq3 = Question("I ate his liver with some fava beans and a nice Chianti...", "The Slience of the Lambs", cat5.category, pt3.points)
mqq4 = Question("It was Johnny Hopkins and Sloan Ketting. And they were blazing that sh*t up every day...", "Step Brothers", cat5.category, pt4.points)
mqq5 = Question("I like to move it, move it!...", "Madagascar", cat5.category, pt5.points)


session.add_all([cat1, cat2, cat3, cat4, cat5])
session.add_all([pt1, pt2, pt3, pt4, pt5])
session.add_all([
    sciq1,sciq2,sciq3,sciq4,sciq5,
    aniq1,aniq2,aniq3,aniq4,aniq5,
    fiq1,fiq2,fiq3,fiq4,fiq5,
    mqq1, mqq2, mqq3, mqq4, mqq5, 
    bhq1,bhq2,bhq3,bhq4,bhq5
    ])


session.commit()
