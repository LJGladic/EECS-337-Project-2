# EECS 337 Project 2 Group 18
# Written by Andrew Bosset, Lukas J. Gladic, Julie Kim and Joshua Koo

import requests

requested_recipe = requests.get('https://www.allrecipes.com/')
print(requested_recipe)

