# EECS 337 Project 2 Group 18
# Written by Andrew Bosset, Lukas J. Gladic, Julie Kim and Joshua Koo
import requests
from ingredients import parse_ingredients
from cooking_method import parse_cook
from tools import find_tools
from tools import step_tools
from bs4 import BeautifulSoup
from transform import transform
from directions import parse_directions
from directions import print_parsed

cooking_terms = ["bake", "sautee", "grill", "fry", ]
measurement_terms = ['cup', 'cups', 'gram', 'grams', 'kilogram', 'kilograms', 'liter', 'liters', 'pound', 'pounds', 'clove', 'cloves', 'milliliter', 'milliliters', 'ounce', 'ounces',
                     'pint', 'pints', 'teaspoon', 'teaspoons', 'tablespoon', 'tablespoons', 'pinch', 'pinches']


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


# gets title
recipe_tital = soup.find("h1", {"id": "recipe-main-content"}).text


prep_times = soup.find_all("li", class_="prepTime__item")

total_time_block = str(prep_times[3])
first_quote = total_time_block.find("\"")
second_quote = total_time_block.find("\"", first_quote + 1)

total_time = total_time_block[first_quote + 10:second_quote]



ingredients = soup.find_all("span", class_="recipe-ingred_txt added")
ingredients_lst = []
for i in ingredients:
    ingredients_lst.append(i.text)

directions = soup.find_all("span", class_="recipe-directions__list--item")
directions_lst = []
for d in directions:
    directions_lst.append(d.text)
    # print (d.text)
# div summary background  for title and short description

parsed_ingredients = parse_ingredients(ingredients_lst)
#print("INGREDIENTS")
#print(ingredients_lst)


# weird terms,  "to taste", "pinch"


all_tools = find_tools(directions_lst, ingredients_lst)
# print(all_tools)


# finding tools for each step
num = 1
for dir in directions_lst:
    print(num)
    str = step_tools(dir)
    num += 1

# main cooking method
main_method = parse_cook(directions_lst)

# directions_lst
parsed_directions, all_methods = parse_directions(directions_lst, parsed_ingredients, all_tools)


# Actual printing for directions starts here:
print("Dish: " + recipe_tital)
print("Total time: " + total_time)
print("All ingredients: ")
for x in ingredients_lst:
    print(x)
print(" ")
print("Necessary tools: ")
for x in all_tools:
    print(x)
print(" ")
print("Main cooking method: " + main_method)
print("all cooking methods: ")
for m in all_methods:
    if m != main_method and m.strip() != '':
        print(m)
print(" ")
print("Step by step directions:")
print_parsed(parsed_directions)
#end of print


#stepbystep = []
#print("DIRECTIONS LIST:")
# print(directions_lst)
#print("STEP BY STEP")
# for dir in directions_lst:
#    dir = dir.replace("\n", " ")
#    tokens = dir.split('. ')
#    stepbystep.extend(tokens)
# print(stepbystep)


#keyingredients = []
# for dir in stepbystep:
#    for i in parsed_ingredients:
#        token = i.split(" ")
#        temp = []
#        for t in token:
#            if t in dir:
#                temp.append(t)
#        keyingredients.extend(temp)
# print(keyingredients)

# dictionary of ingredient names as key, value = [quantity, measurement, descriptor, prep]
# ingredients_dict = {}
# ingredients_dict["ingredient"] = []

# weird terms,  "to taste", "pinch"

while True:
    code = input("Enter a transformation code if desired: (0 - original, 1 - vegetarian, 2 - healthy, 3 - unhealthy, 4 - Indian, 5 - Italian, 6 - Exit) ")
    if code == '0':
        print_parsed(parsed_directions)
    elif code in ['1', '2', '3', '4', '5']:
        recipe = ""
        if code == '1':
            recipe = "Vegetarian"
        elif code == "2":
            recipe = "Healthy"
        elif code == "3":
            recipe = "Unhealthy"
        elif code == "4":
            recipe = "Indian"
        elif code == "5":
            recipe = "Italian"

        print("Recipe transformation to: " + recipe)
        print("")

        t_ingredient, t_direction = transform(code, parsed_ingredients, parsed_directions)
        print("New Ingredients:")
        for x in t_ingredient:
            print(x)
        print("")
        print("New step-by-step directions:")
        print_parsed(t_direction)
        print("Transformation complete!")
    elif code == "6":
        break;
    else:
        print("Invalid transformation code")
# returns ingredient list, directions
