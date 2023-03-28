from models import Category, Point, Question
import numpy as np
import random

if __name__ == '__main__':
    pass

def pick_category():
    category = input(
        '\n Choose a category')
    if category.lower() == "science":
        pass
    elif category.lower() == "anime":
        pass
    elif category.lower() == "bizarre history":
        pass
    elif category.lower() == "movie quotes":
        pass
    elif category.lower() == "finance":
        pass
    else:
        print("Choose a valid category")
