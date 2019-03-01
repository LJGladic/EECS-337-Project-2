# EECS 337 Project 2 Group 18
# Written by Andrew Bosset, Lukas J. Gladic, Julie Kim and Joshua Koo

import requests
from bs4 import BeautifulSoup
while True:
    requested_recipe_webpage = ''
    requested_recipe = ''
    user_response = input('Do you have a recipe number? (y/n): ')
    if user_response == 'y':
        while True:
            recipe_number = input('Please enter the recipe number: ')
            requested_recipe_webpage = 'https://www.allrecipes.com/recipe/'
            requested_recipe_webpage += recipe_number
            requested_recipe = requests.get(requested_recipe_webpage)
            if requested_recipe.status_code == 200:
                break
            else:
                print("There was an error fetching that recipe number, please make sure it is correct")
        break
    elif user_response == 'n':
        while True:
            requested_recipe_webpage = input('Please enter any allrecipes.com recipe URL: ')
            requested_recipe = requests.get(requested_recipe_webpage)
            if requested_recipe.status_code == 200:
                break
            else:
                print('There was an error fetching the recipe, please make sure the URL was correct')
        break
    else:
        print('Input not valid, please try again.')

soup = BeautifulSoup(requested_recipe.text, 'html.parser')
#print (soup)
# print(soup.title)

# gets title
recipe_tital = soup.find("h1", {"id": "recipe-main-content"}).text
print(recipe_tital)
#soup.find_all("div", class_="stylelistrow")
recipe_time = soup.find("span", class_="ready-in-time").text
# requested_recipe has the content from the website
print(recipe_time)

prep_times = soup.find_all("li", class_="prepTime__item")
# for p in prep_times:
#     print(p)

ingredients = soup.find_all("span", class_="recipe-ingred_txt added")
ingredients_lst = []
for i in ingredients:
    ingredients_lst.append(i.text)
    print(i.text)

directions = soup.find_all("span", class_="recipe-directions__list--item")
directions_lst = []
for d in directions:
    directions_lst.append(d.text)
    print (d.text)
# div summary background  for title and short description


# dictionary of ingredient names as key, value = [quantity, measurement, descriptor, prep]
# ingredients_dict = {}
# ingredients_dict["ingredient"] = []


cooking_terms = ["bake", "sautee", "grill", "fry", ]


# weird terms,  "to taste", "pinch"
