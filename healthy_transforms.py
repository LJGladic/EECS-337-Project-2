# Contains lists of healthy and unhealthy options, and dictionaries
# for the transforms

# Particularly healthy protein options
healthy_proteins = ['chicken', 'turkey', 'tofu', 'tuna', 'salmon']
# Particularly unhealthy protein options
unhealthy_proteins = ['beef', 'pork', 'sausage', 'veal', 'duck', 'goose', 'bacon', 'foie gras']

# List of healthy cooking oils from: https://www.healthline.com/nutrition/healthy-cooking-oils
healthy_fats = ['olive oil', 'avocado oil', 'canola oil', 'flax oil']
unhealthy_fats = ['butter', 'margarine', 'coconut oil', 'shortening']

# Healthy and unhealthy dairy options
healthy_dairy = ['fat free milk', 'low fat milk', 'yogurt',  'low fat cheese']
unhealthy_dairy = ['cheese', 'whipped cream', 'reduced-fat milk', 'cream cheese', 'whole milk', 'sour cream']

# Healthy and unhealthy carbohydrates
healthy_carbs = ['wild rice', 'whole wheat bread', 'brown rice', 'whole wheat pasta']
unhealthy_carbs = ['pasta', 'noodles', 'white rice', 'rice', 'bread', 'white bread']

to_healthy_protein = {
    'bacon': 'turkey',
    'pork': 'chicken',
    'sausage': 'tuna',
    'beef': 'salmon',
    'duck': 'tofu',
    'goose': 'tofu',
    'foie gras': 'tofu',
    'veal': 'chicken'
}

from_healthy_protein = {
    'turkey': 'bacon',
    'chicken': 'pork',
    'tuna': 'sausage',
    'salmon': 'beef',
    'tofu': 'foie gras'
}

to_healthy_fats = {
    'butter': 'olive oil',
    'margarine': 'avocado oil',
    'coconut oil': 'flax oil',
    'shortening': 'canola oil'
}

from_healthy_fats = {
    'olive oil': 'butter',
    'avocado oil': 'margarine',
    'flax oil': 'coconut oil',
    'canola oil': 'shortening'
}

to_healthy_dairy = {
    'reduced-fat milk': 'fat free milk',
    'cream cheese': 'low fat cream cheese',
    'whole milk': 'fat free milk',
    'milk': 'fat free milk',
    'cheese': 'low fat cheese',
    'whipped cream': 'fat free yogurt',
    'sour cream': 'fat free yogurt',
    'heavy cream': 'fat free yogurt'
}

from_healthy_dairy = {
    'fat free milk': 'whole milk',
    'low fat cream cheese': 'cream cheese',
    'low fat cheese': 'cheese',
    'fat free yogurt': 'heavy cream'
}

to_healthy_carbs = {
    'pasta': 'whole wheat pasta',
    'noodles': 'whole wheat pasta',
    'rice': 'wild rice',
    'white rice': 'brown rice',
    'white bread': 'whole wheat bread',
    'bread': 'whole wheat bread'
}

from_healthy_carbs = {
    'whole wheat pasta': 'pasta',
    'wild rice': 'rice',
    'brown rice': 'white rice',
    'whole wheat bread': 'white bread'
}
