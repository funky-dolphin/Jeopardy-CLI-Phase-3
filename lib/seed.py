from models import Base, Categories
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



engine = create_engine("sqlite:///Jeopardy.db")
Base.metadata.create_all(bind = engine)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

session.query(Categories).delete()

cat1 = Categories(" ")
cat2 = Categories(" ")
cat3 = Categories(" ")
cat4 = Categories(" ")
cat5 = Categories(" ")

session.add_all([cat1, cat2, cat3, cat4, cat5])

session.commit()
