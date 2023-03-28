
from models import Category, Point, Question
import numpy as np
import random

if __name__ == '__main__':
    pass

print("\n WELCOME TO JEOPARDY \n")

def pick_category():
    global chosen_cat
    category = input('Please choose a category: \n')
    if category.lower() == "science":
        pick_point()
    elif category.lower() == "anime":
        pick_point()
    elif category.lower() == "bizarre history":
        pass
    elif category.lower() == "finance":
        pass
    elif category.lower() == "movie quotes":
        pass
    else:
        print("Choose a valid category \n")
        pick_category()

def pick_point():
    points = input("For how many points? \n")
    if points == '100':
        pass
    elif points == '200':
        pass
    elif points == '300':
        pass
    elif points == '400':
        pass
    elif points == '500':
        pass
    else:
        print("Choose a valid point value \n")
        pick_point()

pick_category()
