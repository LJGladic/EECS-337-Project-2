from cooking_method import get_methods
from tools import find_tools, step_tools
from fractions import Fraction
import re
from nltk.corpus import stopwords
# search for "for" then search for number and hour, minutes, seconds

# 219763


def parse_directions(directions_lst, ingredients, tools):
    print(tools)
    # print(ingredients)
    methods_list = []
    directions = ""
    for dir in directions_lst:
        dir = dir.strip()
        #tokens = dir.split(' ')
        directions += dir

    directions = directions.strip().split('.')
    #print (repr(directions))
    steps = []
    i = 1
    pan_names = ["pan", "skillet"]
    for dir in directions:
        if dir != '':
            step = {}
            # walnut issue
            steps_ingredients = find_ingredients(dir, ingredients)
            # print(steps_ingredients)
            steps_tools = step_tools(dir)
            steps_methods = get_methods(dir)
            for x in steps_methods:
                if x not in methods_list:
                    methods_list.append(x)
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
    return steps, methods_list


# 6969 does not find nuts
def find_ingredients(direction, ingredients):
    ingredients_used = []
    for i in ingredients:
        ingredient = i['name']
        tokens = ingredient.split()
        #print (ingredient)
        stop_words = set(stopwords.words('english'))
        for t in tokens:
            if t in direction and t not in stop_words and ingredient not in ingredients_used:
                ingredients_used.append(ingredient)

    return ingredients_used


# use this to fix fraction error re.search("(-?(\d+)\s?((.\d+)?))+", i) 7000
def find_time(direction):
    # search for number
    time_units = ["hour", 'min', 'minutes', 'minute', 'hours', 'h',
                  'hr', 'hrs', 'mins', "second", 'seconds', 's', 'secs', 'sec']
    time = None
    direction = direction.replace(",", '').replace("-", " to ").replace("(", '').replace(")", '')
    double = False
    fraction = False
    # quantity = re.search("(-?(\d+)\s?((.\d+)?))+", i)
    # if quantity != None:
    #     quantity = str(quantity.group().strip())
    #     i = i.replace(quantity, '')
    if "per side" in direction:
        double = True
    # print(direction)
    tokens = direction.split(' ')
    print(tokens)
    for t in tokens:
        if t.isdigit() or re.search("(-?(\d+)\s?((.\d+)?))+", t):
            if re.search("(-?(\d+)\s?((.\d+)?))+", t):
                fraction = True
            i = tokens.index(t)
            if i + 1 < len(tokens):
                next_word = tokens[i + 1]
                # handles if next word is a fraction i.e 1 1/2
                if re.search("(-?(\d+)\s?((.\d+)?))+", next_word):
                    fraction = True
                    i += 1
                    print(next_word)
                    t = t + " " + next_word
                    next_word = tokens[i + 1]
                print(next_word)
                if tokens[i + 1] in time_units:
                    if double:
                        if fraction:
                            t = float(sum(Fraction(s) for s in t.split()))
                        t = str(int(t) * 2)

                    return t + " " + next_word
                elif next_word == "to" and tokens[i + 2].isdigit():
                    #time = t + next_word + tokens[i + 2]
                    if tokens[i + 3] in time_units:
                        t2 = tokens[i + 2]
                        if double:
                            if fraction:
                                t = float(sum(Fraction(s) for s in t.split()))
                                t2 = float(sum(Fraction(s) for s in t.split()))
                            t = str(int(t) * 2)
                            t2 = str(int(t2) * 2)
                        return t + " " + next_word + " " + t2 + " " + tokens[i + 3]
    return time


def print_parsed(parsed_dir):

    for dict in parsed_dir:
        step = str(dict['step_num'])
        tools = ', '.join(dict['tools'])
        if tools == "":
            tools = "None"
        ingredients = ', '.join(dict['ingredients'])
        if ingredients == "":
            ingredients = "None"
        method = dict['methods']
        if method == "":
            method = "N/A"
        print("Step: " + step)
        print(dict['direction'])
        print("Time: " + str(dict['time']))
        print("Necessary tools: " + tools)
        if len(method) > 1:
            methods = ", ".join(method)
        else:
            methods = "".join(method)
        print("Other cooking methods: " + methods)

        print("Necessary ingredients: " + ingredients)
        print("\n")
