"""Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you 
help him to find out, how many cakes he could bake considering his recipes? 

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns 
the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of 
flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0. 

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
"""


def counter(dict1, dict2):
    list_reps = []
    for i in dict1.keys():
        for l in dict2.keys():
            if i == l:
                coun = 0
                k = dict1.get(i)
                n = dict2.get(l)
                while n >= k:
                    n -= k
                    coun += 1
                list_reps.append(coun)
    return list_reps


def cakes(recipe, available):
    list_keys_res = list(recipe.keys())
    list_keys_aval = list(available.keys())
    if len(list_keys_res) > len(list_keys_aval):
        return 0
    reps = counter(recipe, available)
    cake = min(reps)
    return cake


if __name__ == '__main__':
    print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000,
                                                                                     'milk': 2000}))
'''def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)'''  # лучшее
