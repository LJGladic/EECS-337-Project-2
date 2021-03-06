import random
import vegetarian
import indian
import healthy_transforms
import italian
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
                for d in directions:
                    if 'broth' in d['direction']:
                        d['direction'] = d['direction'].replace('broth', sub)
                        ingredients = []
                        for ingredient in d['ingredients']:
                            ingredient = ingredient.replace(i['name'], sub)
                            ingredients.append(ingredient)
                        d['ingredients'] = ingredients
                i['name'] = sub
                i['descriptor'] = ''
                used.add(sub)
                sub = None
                pass
            if 'gravy' in i['name']:
                sub = 'onion gravy'
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
                    if word != "" and sub not in d['direction']:
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
        sub = None
        for i in parsed_ingredients:
            for key in healthy_transforms.to_healthy_carbs.keys():
                if key in i['name']:
                    sub = healthy_transforms.to_healthy_carbs[key]
            for key in healthy_transforms.to_healthy_dairy.keys():
                if key in i['name']:
                    sub = healthy_transforms.to_healthy_dairy[key]
            for key in healthy_transforms.to_healthy_fats.keys():
                if key in i['name']:
                    sub = healthy_transforms.to_healthy_fats[key]
            for key in healthy_transforms.to_healthy_protein.keys():
                if key in i['name']:
                    sub = healthy_transforms.to_healthy_protein[key]
            if sub:
                tokens = i['name'].split(" ")
                for d in directions:
                    mapped = []
                    for t in tokens:
                        if t in d['direction']:
                            mapped.append(t)
                    word = " ".join(mapped)
                    if word != "" and sub not in d['direction']:
                        d['direction'] = d['direction'].replace(word, sub)
                        ingredients = []
                        for ingredient in d['ingredients']:
                            ingredient = ingredient.replace(word, sub)
                            ingredients.append(ingredient)
                        d['ingredients'] = ingredients
                i['name'] = sub
                i['descriptor'] = ''
            sub = None

    # unhealthy
    elif code == '3':
        sub = None
        for i in parsed_ingredients:
            for key in healthy_transforms.from_healthy_carbs.keys():
                if key in i['name']:
                    sub = healthy_transforms.from_healthy_carbs[key]
            for key in healthy_transforms.from_healthy_dairy.keys():
                if key in i['name']:
                    sub = healthy_transforms.from_healthy_dairy[key]
            for key in healthy_transforms.from_healthy_fats.keys():
                if key in i['name']:
                    sub = healthy_transforms.from_healthy_fats[key]
            for key in healthy_transforms.from_healthy_protein.keys():
                if key in i['name']:
                    sub = healthy_transforms.from_healthy_protein[key]
            if sub:
                tokens = i['name'].split(" ")
                for d in directions:
                    mapped = []
                    for t in tokens:
                        if t in d['direction']:
                            mapped.append(t)
                    word = " ".join(mapped)
                    if word != "" and sub not in d['direction']:
                        d['direction'] = d['direction'].replace(word, sub)
                        ingredients = []
                        for ingredient in d['ingredients']:
                            ingredient = ingredient.replace(word, sub)
                            ingredients.append(ingredient)
                        d['ingredients'] = ingredients
                i['name'] = sub
                i['descriptor'] = ''
            sub = None

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
        step["step_num"] = str(len(directions) + 1)
        step["direction"] = indian.directions
        step["time"] = 'None'
        step["tools"] = []
        step["methods"] = []
        step["ingredients"] = indian.spices
        directions.append(step)
    # Italian
    elif code == '5':
        sub = None
        for i in parsed_ingredients:
            if 'cheese' in i['name']:
                sub = random.choice(italian.italian_cheeses)
            for food in italian.other_meats:
                if food in i['name']:
                    sub = random.choice(italian.italian_meats)
            for food in italian.other_fish:
                if food in i['name']:
                    sub = random.choice(italian.italian_fish)
            for food in italian.other_herbs_and_spices:
                if food in i['name']:
                    sub = random.choice(italian.italian_herbs_and_spices)
            if sub:
                tokens = i['name'].split(" ")
                for d in directions:
                    mapped = []
                    for t in tokens:
                        if t in d['direction']:
                            mapped.append(t)
                    word = " ".join(mapped)
                    if word != "" and sub not in d['direction']:
                        d['direction'] = d['direction'].replace(word, sub)
                        ingredients = []
                        for ingredient in d['ingredients']:
                            ingredient = ingredient.replace(word, sub)
                            ingredients.append(ingredient)
                        d['ingredients'] = ingredients
                i['name'] = sub
                i['descriptor'] = ''
            sub = None

    list_ingredients = []
    for dict in parsed_ingredients:
        if dict['name'] not in list_ingredients:
            list_ingredients.append(dict['name'])

    return parsed_ingredients, directions
