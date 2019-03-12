import numpy as np
import re
import nltk

# to do
# 73634
# good testers 7000, 139236(weird with blue cheese, comma problem and stems),14140(alt and pepper)
# problems temp of water and decimals possibly
# remove anything with parentheses around it maybe
# remove optional in 6969
# set up functionality for bigram and trigram checking for descriptors and prep

my_unit_list = [
    "teaspoon",
    "teaspoons",
    "t",
    "tsp",
    "tablespoon",
    'package',
    'packages',
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

# get preps from prep.txt
preparations_list = []
prep_file = open("prep.txt", "r")
prep_lines = prep_file.readlines()
prep_lines = set(prep_lines)
for l in prep_lines:
    preparations_list.append(str(l).strip())

# get from text file

# get descriptor list from text file
descriptors_list = []
desc_file = open("descriptors.txt", "r")
desc_lines = desc_file.readlines()
# desc_lines = set(desc_lines)
for l in desc_lines:
    descriptors_list.append(str(l).strip())
# print (descriptors_list)

stop_words = [
    "(optional)",
    "or",
    "to taste",
    "for topping"
]


# print(stop_words)


# potentially remove anything after or
# add anything after a comma to descriptors
# figure out what to do about salt and pepper to taste 14140
# add in bigrams feature andd then remove tokens from original tokens list if it matches desc or prep
def parse_ingredients(ingredients):
    ingredients_list = []

    for i in ingredients:
        quantity = ''
        measurement = ''
        name = ''
        descriptors = []
        preperations = []
        paranthesis = []
        # adds parentheses to descriptors
        desc = re.findall("\(.*?\)", i)
        for d in desc:
            if d is not None:
                paranthesis.append(d)
                i = i.replace(d, '')

        quantity = re.search("(-?(\d+)\s?((.\d+)?))+", i)
        if quantity is not None:
            quantity = str(quantity.group().strip())
            i = i.replace(quantity, '')
            # print (quantity)
        # fixes comma problem
        i = i.replace(',', '')
        tokens = [t.lower() for t in i.split() if i.lower().replace(
            '\(', '').replace("-", ' ')]
        bigrams = []
        bigrams.extend(nltk.bigrams(tokens))
        remove_bigrams = []
        for b in bigrams:
            b = ' '.join(b).strip()
            print(b)
            # finding measurement
            if b in my_unit_list:
                measurement = b
                remove_bigrams.append(b)
            elif b in descriptors_list:
                descriptors.append(b)
                remove_bigrams.append(b)

            elif b in preparations_list:
                preperations.append(b)
                remove_bigrams.append(b)
            elif b in stop_words:
                remove_bigrams.append(b)

        for r in remove_bigrams:
            i = i.replace(r, '')

        remove_tokens = []
        # redo for singles
        tokens = [t.lower() for t in i.split() if i.lower().replace(
            '\(', '').replace("-", ' ')]
        for t in tokens:
            t = t.strip()
            # finding measurement
            if t in my_unit_list:
                measurement = t
                remove_tokens.append(t)
            elif t in descriptors_list:
                descriptors.append(t)
                remove_tokens.append(t)

            elif t in preparations_list:
                preperations.append(t)
                remove_tokens.append(t)

            elif t in stop_words:
                remove_tokens.append(t)

        for r in remove_tokens:
            if r in tokens:
                tokens.remove(r)

        name = " ".join(tokens).replace('-', '')
        name = name.strip()
        if name[0:3] == 'and' or 'and' == name[-3:]:
            name = name.replace("and", '').strip()
        # print descriptors

        for p in paranthesis:
            descriptors.append(p)
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
