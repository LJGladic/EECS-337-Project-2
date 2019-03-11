import random
import vegetarian

def transform(code, parsed, directions):
    # vegetarian substitution
    if code == '1':
        used = set()
        for i in parsed:
            sub = None
            if 'broth' in i['name']:
                sub = random.choice(vegetarian.broth_subs)
                while sub in used:
                    sub = random.choice(vegetarian.broth_subs)
            for key in vegetarian.meat.keys():
                if key in i['name']:
                    sub = random.choice(vegetarian.meat[key])
                    while sub in used:
                        sub = random.choice(vegetarian.meat[key])
            for key in vegetarian.seafood.keys():
                if key in i['name']:
                    sub = random.choice(vegetarian.seafood[key])
                    while sub in used:
                        sub = random.choice(vegetarian.seafood[key])
            for word in vegetarian.fish:
                if word in i['name']:
                    sub = random.choice(vegetarian.fish_subs)
                    while sub in used:
                        sub = random.choice(vegetarian.fish_subs)
            if sub:
                for d in directions:
                    d.replace(i['name'], sub)
                i['name'] = sub
                i['descriptor'] = ''
                used.add(sub)

    # healthy substitution
    elif code == '2':
        pass


    return parsed, directions