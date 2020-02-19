#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches_per_ingredient = []
    for ingredient in recipe.keys():
        if ingredient in ingredients:
            batches_per_ingredient.append(
                ingredients[ingredient] // recipe[ingredient])
        else:
            return 0

    max_batch = batches_per_ingredient[0]
    for batch in batches_per_ingredient:
        if batch < max_batch:
            max_batch = batch
    return max_batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
