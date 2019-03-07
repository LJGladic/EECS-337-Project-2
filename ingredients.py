import numpy as np
import re
import nltk

# good testers 7000
# problems temp of water and decimals
# remove anything with parentheses around it

my_unit_list = [
    "teaspoon",
    "teaspoons",
    "t",
    "tsp",
    "tablespoon",
    "tablespoons",
    "tbsp",
    "tbl",
    "tbs",
    "fluid ounce",
    "fluid ounces",
    "gill",
    "gills",
    "cup",
    "cups",
    "c",
    "pint",
    "pints",
    "p",
    "pt",
    "pts",
    "fl pt",
    "fl pts",
    "quart",
    "quarts",
    "qt",
    "qts",
    "fl qt",
    "fl qts",
    "gallon",
    "gallons",
    "g",
    "gal",
    "ml",
    "milliliter",
    "millilitre",
    "litre",
    "liter",
    "liters",
    "l",
    "pounds",
    "pound",
    "gram",
    "grams",
    "lb",
    "lbs",
    "needed",
    "taste",
    "pinch",
    "dash",
    "pkg.",
    "package",
    "can",
    "cans"
    'c.',
    'fl oz',
    'ounce'
    'ounces'
    'oz'
    'tbsps'
    'tsps'
    'inch'
    'in'
    '\"'
    'cm'
    'mm'
]

preparations_list = [
    'drained',
    'chopped',
    'softened'
]

# get from text file
descriptors_list = [
    "room",
    "temperature",
    "chopped",
    "diced",
    "sliced"
]

stop_words = [
    'junk',
    "(optional)"
]


# print(stop_words)


# potentially remove anything after or
def parse_ingredients(ingredients):
    ingredients_list = []

    for i in ingredients:
        quantity = ''
        measurement = ''
        name = ''
        descriptors = []
        preperations = []

        # adds parentheses to descriptors
        desc = re.findall("\(.*?\)", i)
        for d in desc:
            if d != None:
                descriptors.append(d)
                i = i.replace(d, '')
        tokens = [t.lower() for t in i.split() if i.lower().replace('\(', '') not in stop_words]
        # find quantity
        print(tokens)
        quantity = re.search("(-?(\d+)\s?((.\d+)?))", i)
        if quantity != None:
            quantity = str(quantity.group().strip())
            tokens.remove(quantity)
            # print (quantity)

        for t in tokens:
            # finding measurement
            if t in my_unit_list:
                measurement = t
                tokens.remove(t)
                # print(t)
            elif t in descriptors_list:
                descriptors.append(t)
                tokens.remove(t)
                # print(t)
            elif t in preparations_list:
                preparation = t
                tokens.remove(t)
                # print(t)
            elif t in stop_words:
                tokens.remove(t)
        name = " ".join(tokens).strip()
        print(name)
        # print(tokens)

        ingredient = {}
        ingredient['name'] = name
        ingredient['quantity'] = quantity
        ingredient['measurement'] = measurement
        ingredient['descriptor'] = " ".join(descriptors).strip()
        ingredient['preperations'] = " ".join(preperations).strip()
        ingredients_list.append(ingredient)
        print(ingredient)
# ingredient['prep'] = ''
    return ingredients_list
