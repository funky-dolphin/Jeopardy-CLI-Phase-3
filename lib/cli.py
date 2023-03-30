
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

# table = PrettyTable()
# table.field_names = ["Science", "Anime", "Bizzare History", "Finance", "Movie Quotes"]
# table.add_row([100, 100, 100, 100, 100])
# table.add_row([200, 200, 200, 200, 200])
# table.add_row([300, 300, 300, 300, 300])
# table.add_row([400, 400, 400, 400, 400])
# table.add_row([500, 500, 500, 500, 500])

with open("seed.py") as f:
        exec(f.read())

def print_table():

    global table 
    table = PrettyTable()

    table_query_science = session.query(Question.point).filter(Question.category == "Science").all()
    table_list_science = [item for t in table_query_science for item in t]

    table_query_anime = session.query(Question.point).filter(Question.category == "Anime").all()
    table_list_anime = [item for t in table_query_anime for item in t]

    table_query_history = session.query(Question.point).filter(Question.category == "Bizarre History").all()
    table_list_history = [item for t in table_query_history for item in t]

    table_query_finance = session.query(Question.point).filter(Question.category == "Finance").all()
    table_list_finance = [item for t in table_query_finance for item in t]

    table_query_movie = session.query(Question.point).filter(Question.category == "Movie Quotes").all()
    table_list_movie = [item for t in table_query_movie for item in t]

    columns=["Science", "Anime", "Bizzare History", "Finance", "Movie Quotes"]
    table.add_column(columns[0], table_list_science)
    table.add_column(columns[1], table_list_anime)
    table.add_column(columns[2], table_list_history)
    table.add_column(columns[3], table_list_finance)
    table.add_column(columns[4], table_list_movie)



print("""

     ██╗███████╗ ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ██╗   ██╗
     ██║██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
     ██║█████╗  ██║   ██║██████╔╝███████║██████╔╝██║  ██║ ╚████╔╝ 
██   ██║██╔══╝  ██║   ██║██╔═══╝ ██╔══██║██╔══██╗██║  ██║  ╚██╔╝  
╚█████╔╝███████╗╚██████╔╝██║     ██║  ██║██║  ██║██████╔╝   ██║   
 ╚════╝ ╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝    ╚═╝                                                                   
 """)
<<<<<<< HEAD
# print(f'\n{table }')
=======
print_table()
print(f'\n{table}')
>>>>>>> main

all_categories = session.query(Category).all()
# all_points = session.query(Point).all()

all_points = 0

def username():
    global p1
    global p2
    global turn
    turn = 1
    

    session.query(Player).delete()
    
    player1 = input("\nPlayer 1, Please input a username: \n")
    p1 = Player(player1, 0)
    player2 = input("\nPlayer 2, Please input a username: \n")
    p2 = Player(player2, 0)
    session.add_all([p1,p2])
    session.commit()
    pick_category()

def pick_category():
    global chosen_cat
    score = session.query(Player).filter(Player.score == "s")
    # global questions
    cat_list = [category.category for category in all_categories]
    print_table()

    print(f'\n{table}')
    
    if turn % 2 != 0:
        category = input(f"\n{p1.player_name} Please choose a category:\n")
    else: 
        category = input(f"\n{p2.player_name} Please choose a category:\n")

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
    elif category.lower() == "s":
        print(f'\n{p1.player_name} Score: {p1.score}\n{p2.player_name} Score: {p2.score}')
        pick_category()
    elif category.lower() == "t":
        print_table()
        print(f'\n{table }') 
        pick_category()
    else:
        print("\nChoose a valid category \n")
        pick_category()

def pick_point():
    global chosen_question
    global points
    global available_points
    point_in_cat = chosen_cat.filter(Question.selected == 0)
    available_points = [point.point for point in point_in_cat]
    if len(available_points) == 0:
        print("\nNo more questions available \nChoose another category")
        pick_category()
    print(f'\n{available_points}')
    points = input("\nFor how many points? \n")
    if points == '100':
        chosen_question = chosen_cat.filter(Question.point == 100).first()
        print(f'\n{chosen_question.question}')
        chosen_question.selected = 1
        chosen_question.point = 0
        session.commit()
        answer()
    elif points == '200':
        chosen_question = chosen_cat.filter(Question.point == 200).first()
        print(f'\n{chosen_question.question}')
        chosen_question.selected = 1
        chosen_question.point = 0
        session.commit()
        answer()
    elif points == '300':
        chosen_question = chosen_cat.filter(Question.point == 300).first()
        print(f'\n{chosen_question.question}')
        chosen_question.selected = 1
        chosen_question.point = 0
        session.commit()
        answer()
    elif points == '400':
        chosen_question = chosen_cat.filter(Question.point == 400).first()
        print(f'\n{chosen_question.question}')
        chosen_question.selected = 1
        chosen_question.point = 0
        session.commit()
        answer()
    elif points == '500':
        chosen_question = chosen_cat.filter(Question.point == 500).first()
        print(f'\n{chosen_question.question}')
        chosen_question.selected = 1
        chosen_question.point = 0
        session.commit()
        answer()
    else:
        print("\nChoose a valid point value \n")
        pick_point()

def answer():
    global turn
    global all_points
    input_answer = input("\nAnswer below:\n")
    if all_points < 7500:
        if chosen_question.answer.lower() == input_answer.lower():
            print("""
 ██████╗ ██████╗ ██████╗ ██████╗ ███████╗ ██████╗████████╗██╗
██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██║
██║     ██║   ██║██████╔╝██████╔╝█████╗  ██║        ██║   ██║
██║     ██║   ██║██╔══██╗██╔══██╗██╔══╝  ██║        ██║   ╚═╝
╚██████╗╚██████╔╝██║  ██║██║  ██║███████╗╚██████╗   ██║   ██╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝ 
""")
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
            print("""         
██╗    ██╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ██╗
██║    ██║██╔══██╗██╔═══██╗████╗  ██║██╔════╝ ██║
██║ █╗ ██║██████╔╝██║   ██║██╔██╗ ██║██║  ███╗██║
██║███╗██║██╔══██╗██║   ██║██║╚██╗██║██║   ██║╚═╝
╚███╔███╔╝██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝██╗
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝
""")
            turn += 1
            all_points += int(points)
            pick_category()
    else: 
        print("\n Thanks for playing ya goof \n")

# pick_category()
username()
