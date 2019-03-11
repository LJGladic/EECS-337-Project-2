from cooking_method import get_methods
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
            print(steps_ingredients)
            steps_tools = find_tools([dir], steps_ingredients)
            steps_methods = get_methods(dir)
            step["step_num"] = str(i)
            step["direction"] = dir
            step["time"] = find_time(dir)
            step["tools"] = steps_tools
            step["methods"] = steps_methods
            step["ingredients"] = steps_ingredients
            steps.append(step)
            print(step)
            print("\r")
        i += 1
    return steps


# 6969 does not find nuts
def find_ingredients(direction, ingredients):
    ingredients_used = []
    for i in ingredients:
        ingredient = i['name']
        #print (ingredient)
        if ingredient in direction:
            ingredients_used.append(ingredient)

    return ingredients_used


def find_time(direction):
    # search for number
    time_units = ["hour", 'min', 'minutes', 'minute', 'hours', 'h',
                  'hr', 'hrs', 'mins', "second", 'seconds', 's', 'secs', 'sec']
    time = None
    direction = direction.replace(",", '')
    # print(direction)
    tokens = direction.split(' ')
    for t in tokens:
        if t.isdigit():
            i = tokens.index(t)
            if i + 1 < len(tokens):
                next_word = tokens[i + 1]
                print(next_word)
                if tokens[i + 1] in time_units:
                    time = t + " " + next_word
                    print("here")
                    return time
                elif next_word == "to":
                    time = t + next_word + tokens[i + 2]
                    if (tokens[i + 3] in time_units):
                        time = t + " " + next_word + " " + tokens[i + 2] + " " + tokens[i + 3]
                        return time
    return time
