import random
import vegetarian
import indian
import copy

def transform(code, input_ingredients, input_directions):
    parsed_ingredients = copy.deepcopy(input_ingredients)
    directions = copy.deepcopy(input_directions)
    # vegetarian
    if code == '1':
        used = set()
        for i in parsed_ingredients:
            sub = None
            if 'broth' in i['name']:
                sub = random.choice(vegetarian.broth_subs)
                while sub in used:
                    sub = random.choice(vegetarian.broth_subs)
            for key in vegetarian.meat.keys():
                if key in i['name']:
                    if not sub:
                        sub = random.choice(vegetarian.meat[key])
                        while sub in used:
                            sub = random.choice(vegetarian.meat[key])
            for key in vegetarian.seafood.keys():
                if key in i['name']:
                    if not sub:
                        sub = random.choice(vegetarian.seafood[key])
                        while sub in used:
                            sub = random.choice(vegetarian.seafood[key])
            for word in vegetarian.fish:
                if word in i['name']:
                    if not sub:
                        sub = random.choice(vegetarian.fish_subs)
                        while sub in used:
                            sub = random.choice(vegetarian.fish_subs)
            if sub:
                tokens = i['name'].split(" ")
                for d in directions:
                    mapped = []
                    for t in tokens:
                        if t in d['direction']:
                            mapped.append(t)
                    word = " ".join(mapped)
                    if word != "":
                        d['direction'] = d['direction'].replace(word, sub)
                    ingredients = []
                    for ingredient in d['ingredients']:
                        ingredient = ingredient.replace(word, sub)
                        ingredients.append(ingredient)
                    d['ingredients'] = ingredients
                i['name'] = sub
                i['descriptor'] = ''
                used.add(sub)
            sub = None
    # healthy
    elif code == '2':
        pass
    # unhealthy
    elif code == '3':
        pass
    # Indian
    elif code == '4':
        for i in parsed_ingredients:
            for key in indian.indian.keys():
                if key in i['name']:
                    sub = indian.indian[key]
                    tokens = i['name'].split(" ")
                    for d in directions:
                        mapped = []
                        for t in tokens:
                            if t in d['direction']:
                                mapped.append(t)
                        word = " ".join(mapped)
                        if word != "":
                            d['direction'] = d['direction'].replace(word, sub)
                        ingredients = []
                        for ingredient in d['ingredients']:
                            ingredient = ingredient.replace(word, sub)
                            ingredients.append(ingredient)
                        d['ingredients'] = ingredients
                    i['name'] = sub
                    i['descriptor'] = ''
        step = {}
        step["step_num"] = str(len(directions)+1)
        step["direction"] = indian.directions
        step["time"] = 'None'
        step["tools"] = []
        step["methods"] = []
        step["ingredients"] = indian.spices
        directions.append(step)
    # Italian
    elif code == '5':
        pass


    return parsed_ingredients, directions