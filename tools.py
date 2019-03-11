import nltk

tools = ['apple corer',
         'apple cutter',
         'aluminum foil',
         'aluminium foil',
         'baster',
         'beanpot',
         'biscuit cutter',
         'blender',
         'bottle opener',
         'bowl',
         'bread knife',
         'browning tray',
         'butter curler',
         'cheese cutter',
         'cheese knife',
         'cheese slicer',
         'cheesecloth',
         'chef\'s knife',
         'cherry pitter',
         'chinois',
         'clay pot',
         'cleaver',
         'colander'
         'corkscrew',
         'crab cracker',
         'cutting board',
         'dough scraper',
         'egg poacher'
         'egg timer',
         'fillet knife',
         'flour sifter',
         'food mill',
         'mill',
         'funnel',
         'garlic press',
         'grater',
         'herb chopper',
         'ladle',
         'lame',
         'lemon reamer',
         'lemon squeezer',
         'squeezer',
         'lobster pick',
         'mandoline',
         'measuring cup',
         'measuring spoon',
         'meat grinder',
         'mincer',
         'meat tenderizer',
         'meat thermometer',
         'thermometer',
         'melon baller',
         'mezzaluna',
         'milk frother',
         'mortar and pestle',
         'nutcracker',
         'oven glove',
         'oven mitt',
         'pastry bag',
         'dish',
         'dishes',
         'pastry blender',
         'pastry brush',
         'brush',
         'peeler',
         'pepper mill',
         'pizza cutter',
         'masher',
         'potato masher',
         'knife',
         'spoon',
         'rolling pin',
         'salt shaker',
         'scale',
         'scissors',
         # maybe not scoop
         'scoop',
         'sieve',
         'skimmer',
         'spatula',
         'tongs',
         'trussing needle',
         'twine',
         'whisk',
         'wooden spoon',
         'wood spoon',
         'fork',
         'pan',
         'pans',
         'cast iron skillet',
         'wok',
         'pot',
         'frying pan',
         'container',
         'sheet pan',
         'baking pan',
         'baking sheet',
         'mixing bowl',
         'zester'
         ]


tool_relations = {'saute': 'pan',
                  'fry': 'pan',
                  'boil': 'pot',
                  'chopped': 'knife',
                  'sliced': 'knife',
                  'diced': 'knife',
                  'minced': 'knife',
                  'chop': 'knife',
                  'slice': 'knife',
                  'dice': 'knife',
                  'mince': 'knife',
                  'mix': 'spoon',
                  'stir': 'spoon',
                  'beat': 'fork',
                  'whisk': "whisk",
                  'scrape': 'knife',
                  'tablespoon': 'measuring spoon',
                  'teaspoon': 'measuring spoon',
                  'tablespoons': 'measuring spoon',
                  'teaspoons': 'measuring spoon',
                  'cup': 'measuring cup',
                  'cups': 'measuring cup'}


def find_tools(directions_lst, ingredients_lst):
    directions = []
    for dir in directions_lst:
        dir = dir.replace("\n", " ")
        dir = dir.replace(".", " ")
        tokens = dir.split(' ')
        directions.append(tokens)

    ingredients = []
    for ing in ingredients_lst:
        tokens = ing.split(' ')
        ingredients.append(tokens)
    #print("LOOK HERE")
    # print(ingredients)

    curr_tools = []
    # direction parsing
    dir_bigrams = []
    dir_trigrams = []
    ing_bigrams = []
    ing_trigrams = []
    for dir in directions:
        dir_bigrams.extend(nltk.bigrams(dir))
        dir_trigrams.extend(nltk.trigrams(dir))
        for word in dir:
            if word in tools and word not in curr_tools:
                curr_tools.append(word)
            if word in tool_relations:
                if tool_relations[word] in tools and tool_relations[word] not in curr_tools:
                    curr_tools.append(tool_relations[word])
    # ingredient parsing
    for ing in ingredients:
        ing_bigrams.extend(nltk.bigrams(ing))
        ing_trigrams.extend(nltk.trigrams(ing))
        for word in ing:
            if word in tool_relations:
                if tool_relations[word] in tools and tool_relations[word] not in curr_tools:
                    curr_tools.append(tool_relations[word])

    # Looking for 2/3 word tools
    bitris = []
    bitris.extend(dir_bigrams)
    bitris.extend(dir_trigrams)
    bitris.extend(ing_bigrams)
    bitris.extend(ing_trigrams)

    joined_grams = []
    for gram in bitris:
        # print("Gram")
        # print(gram)
        new_word = ' '.join(gram)
        joined_grams.append(new_word)
    #print("Now JOINED")
    # print(joined_grams)

    for gram in joined_grams:
        if gram in tools and gram not in curr_tools:
            curr_tools.append(gram)

    # special cases
    if "knife" in curr_tools and "cutting board" not in curr_tools:
        curr_tools.append("cutting board")

    return curr_tools


def step_tools(direction):
    curr_tools = []

    dir = direction.replace("\n", " ")
    dir = dir.replace(".", " ")
    tokens = dir.split(' ')

    bitris = []
    joined_grams = []
    bitris.extend(nltk.bigrams(tokens))
    bitris.extend(nltk.trigrams(tokens))

    for gram in bitris:
        new_word = ' '.join(gram)
        joined_grams.append(new_word)

    for word in tokens:
        if word in tools and word not in curr_tools:
            curr_tools.append(word)
        if word in tool_relations:
            if tool_relations[word] in tools and tool_relations[word] not in curr_tools:
                curr_tools.append(tool_relations[word])

    for gram in joined_grams:
        if gram in tools and gram not in curr_tools:
            curr_tools.append(gram)

    print("tools for this step:")
    print(curr_tools)
    return curr_tools
