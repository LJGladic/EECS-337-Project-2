import nltk

cooking_terms = ["bake",
                 "sautee",
                 "grill",
                 "fry",
                 "broil",
                 "deepfry",
                 "poach",
                 "steam",
                 "simmer",
                 "roast",
                 "blanch",
                 "baste",
                 "deep fry",
                 "stir fry",
                 "stirfry",
                 "barbeque",
                 "toast",
                 "saute",
                 "stir-fry",
                 "deep-fry",
                 "smoke",
                 "braise",
                 "boil",
                 "pan-fry",
                 "panfry",
                 "pan fry",
                 "pressure-cook",
                 "pressure cook",
                 "sear"
                 ]
aux_methods = ['mix',
               'stir',
               'toss',
               'whisk',
               'chop', 'knead', 'scrape'
               'grate', 'stir', 'shake', 'mince', 'crush', 'squeeze', 'coat', 'heat'
               'drain', 'spoon', 'beat', 'pour', 'sprinkle', 'garnish', 'spread', 'cover',
               'grease', 'blend'
               ]

# make this return all methods


def get_methods(direction):
    direction = direction.lower()
    tokens = direction.split(' ')
    bigrams = []
    cook_bigrams = []
    bigrams.extend(nltk.bigrams(tokens))
    for x in bigrams:
        cook_bigrams.append(' '.join(x))

    combined_list = tokens + cook_bigrams
    all_cooking_terms = cooking_terms + aux_methods
    freq = {}
    max = 0
    max_key = ""

    for x in combined_list:
        if x in all_cooking_terms:
            if x in freq:
                temp = freq[x]
                temp += 1
                freq[x] = temp
            else:
                freq[x] = 1
            if freq[x] > max:
                max = freq[x]
                max_key = x
    method_mode = max_key
    return method_mode


def parse_cook(directions_lst):
    # print("COOKING")
    # print(directions_lst)
    last_step_parse = directions_lst[-2:]
    last_step = last_step_parse[0]
    last_step = last_step.replace("\n", "")
    last_step = last_step.lower()

    cook_bigrams = []

    tokens = last_step.split(' ')

    bigrams = []
    cook_bigrams = []
    bigrams.extend(nltk.bigrams(tokens))
    for x in bigrams:
        cook_bigrams.append(' '.join(x))

    combined_list = tokens + cook_bigrams
    # print("COMBINED")
    # print(combined_list)
    freq = {}
    max = 0
    max_key = ""

    for x in combined_list:
        if x in cooking_terms:
            if x in freq:
                temp = freq[x]
                temp += 1
                freq[x] = temp
            else:
                freq[x] = 1
            if freq[x] > max:
                max = freq[x]
                max_key = x
    method_mode = max_key
    print("METHOD")
    print(method_mode)
    return method_mode
