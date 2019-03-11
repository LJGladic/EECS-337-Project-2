import cooking_method
from tools import find_tools


# search for "for" then search for number and hour, minutes, seconds

# 219763
def parse_directions(directions_lst, ingredients, tools):
    print(tools)
    # print(ingredients)
    directions = ""
    for dir in directions_lst:
        dir = dir.strip()
        #tokens = dir.split(' ')
        directions += dir

    directions = directions.strip().split('.')
    #print (repr(directions))
    steps = []
    i = 1
    for dir in directions:
        if dir != '':
            step = {}
            steps_ingredients = find_ingredients(dir, ingredients)
            steps_tools = find_tools([dir], steps_ingredients)

            step["step_num"] = str(i)
            step["direction"] = dir
            step["time"] = " "
            step["tools"] = steps_tools
            step["methods"] = ""
            step["ingredients"] = steps_ingredients
            steps.append(step)
            print(step)
            print("\r")


# 6969 does not find nuts
def find_ingredients(direction, ingredients):
    ingredients_used = []
    for i in ingredients:
        ingredient = i['name']
        #print (ingredient)
        if ingredient in direction:
            ingredients_used.append(ingredient)

    return ingredients_used
