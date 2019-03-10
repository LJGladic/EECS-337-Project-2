import random
import vegetarian

def transform(code, parsed, directions):
    # vegetarian substitution
    if code == '1':
        for i in parsed:
            if 'broth' in i['name']:
                sub = random.choice(vegetarian.broth_subs)
                for d in directions:
                    d.replace(i['name'], sub)
                i['name'] = sub
            for key in vegetarian.meat.keys():
                if key in i['name']:
                    sub = random.choice(vegetarian.meat[key])
                    for d in directions:
                        d.replace(i['name'], sub)
                    i['name'] = sub
            for key in vegetarian.seafood.keys():
                if key in i['name']:
                    sub = random.choice(vegetarian.meat[key])
                    for d in directions:
                        d.replace(i['name'], sub)
                    i['name'] = sub
            for word in vegetarian.fish:
                if word in i['name']:
                    sub = random.choice(vegetarian.fish_subs)
                    for d in directions:
                        d.replace(i['name'], sub)
                    i['name'] = sub

    # healthy substitution
    elif code == '2':
        pass


    return parsed, directions