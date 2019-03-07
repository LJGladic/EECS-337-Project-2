import numpy as np

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

descriptors_list = [
    'drained',
    'chopped',


]

my_unit_set = set(my_unit_list)

# add_unit_list = np.setdiff1d(unitslist2, my_unit_list)
# print(add_unit_list)
