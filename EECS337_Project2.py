# EECS 337 Project 2 Group 18
# Written by Andrew Bosset, Lukas J. Gladic, Julie Kim and Joshua Koo

import requests

while True:
    requested_recipe_webpage = ''
    user_response = input('Do you have a recipe number? (y/n): ')
    if user_response == 'y':
        recipe_number = input('Please enter the recipe number: ')
        requested_recipe_webpage = 'https://www.allrecipes.com/recipe/'
        requested_recipe_webpage += recipe_number
        break
    elif user_response == 'n':
        requested_recipe_webpage = input('Please enter any allrecipes.com recipe URL: ')
        break
    else:
        print('Input not valid, please try again.')

requested_recipe = requests.get(requested_recipe_webpage)
