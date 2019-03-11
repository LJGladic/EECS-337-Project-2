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
                 "sear",
                 "cook"
                 ]


def parse_cook(directions_lst):
    # print("COOKING")
    # print(directions_lst)
    last_step_parse = directions_lst[-2:]
    last_step = last_step_parse[0]
    last_step = last_step.replace("\n", "")
    # print("LAST")
    # print(last_step)
    cook_bigrams = []
    tokens = last_step.split(' ')
    cook_bigrams.extend(nltk.bigrams(last_step))
    combined_list = tokens + cook_bigrams

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
    print(method_mode)
    return method_mode
