
from models import Category, Point, Question, Player
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import numpy as np
import random
from prettytable import PrettyTable

if __name__ == '__main__':
    pass

engine = create_engine('sqlite:///Jeopardy.db')

Session = sessionmaker(bind=engine)
session = Session()

print("\n WELCOME TO JEOPARDY \n")

# table = PrettyTable()
all_categories = session.query(Category).all()
# all_points = session.query(Point).all()
# table.field_names = [category.category for category in all_categories]
# table.add_column(, [point.points for point in all_points])

all_points = 0

def username():
    global p1
    global p2
    global turn
    turn = 1
    with open("seed.py") as f:
        exec(f.read())

    session.query(Player).delete()
    
    player1 = input("Player 1, Please input a username \n")
    p1 = Player(player1, 0)
    player2 = input("Player 2, Please input a username \n")
    p2 = Player(player2, 0)
    session.add_all([p1,p2])
    session.commit()
    pick_category()

def pick_category():
    global chosen_cat
    # global questions
    cat_list = [category.category for category in all_categories]
    print(cat_list)

    if turn % 2 != 0:
        category = input(f"{p1.player_name} Please choose a category: \n")
    else: 
        category = input(f"{p2.player_name} Please choose a category: \n")

    if category.lower() == "science":
        chosen_cat = session.query(Question).filter(Question.category == "Science")
        pick_point()
    elif category.lower() == "anime":
        chosen_cat = session.query(Question).filter(Question.category == "Anime")
        pick_point()
    elif category.lower() == "bizarre history":
        chosen_cat = session.query(Question).filter(Question.category == "Bizarre History")
        pick_point()
    elif category.lower() == "finance":
        chosen_cat = session.query(Question).filter(Question.category == "Finance")
        pick_point()
    elif category.lower() == "movie quotes":
        chosen_cat = session.query(Question).filter(Question.category == "Movie Quotes")
        pick_point()
    else:
        print("Choose a valid category \n")
        pick_category()

def pick_point():
    global chosen_question
    global points
    global available_points
    point_in_cat = chosen_cat.filter(Question.selected == 0)
    available_points = [point.point for point in point_in_cat]
    if len(available_points) == 0:
        print("No more questions available \nChoose another category")
        pick_category()
    print(available_points)
    points = input("For how many points? \n")
    if points == '100':
        chosen_question = chosen_cat.filter(Question.point == 100).first()
        print(chosen_question.question)
        chosen_question.selected = 1
        session.commit()
        answer()
    elif points == '200':
        chosen_question = chosen_cat.filter(Question.point == 200).first()
        print(chosen_question.question)
        chosen_question.selected = 1
        session.commit()
        answer()
    elif points == '300':
        chosen_question = chosen_cat.filter(Question.point == 300).first()
        print(chosen_question.question)
        chosen_question.selected = 1
        session.commit()
        answer()
    elif points == '400':
        chosen_question = chosen_cat.filter(Question.point == 400).first()
        print(chosen_question.question)
        chosen_question.selected = 1
        session.commit()
        answer()
    elif points == '500':
        chosen_question = chosen_cat.filter(Question.point == 500).first()
        print(chosen_question.question)
        chosen_question.selected = 1
        session.commit()
        answer()
    else:
        print("Choose a valid point value \n")
        pick_point()

def answer():
    global turn
    global all_points
    input_answer = input("Answer below: \n")
    if all_points < 7500:
        if chosen_question.answer.lower() == input_answer.lower():
            print("Correct!")
            if turn % 2 == 0:
                p2.score += int(points)
                all_points += int(points)
            else:
                p1.score += int(points)
                all_points += int(points)
            turn += 1
            session.commit()
            pick_category()
        else:
            print("Incorrect...")
            turn += 1
            all_points += int(points)
            pick_category()
    else: 
        print("Thanks for playing ya goof")

# pick_category()
username()
