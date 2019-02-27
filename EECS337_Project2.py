# EECS 337 Project 2 Group 18
# Written by Andrew Bosset, Lukas J. Gladic, Julie Kim and Joshua Koo

import requests

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

# requested_recipe has the content from the website
