from datetime import datetime
from recipe import Recipe

class Book:

    def __init__(self, name):

        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        for r_type in self.recipes_list:
            for r_recipe in self.recipes_list[r_type]:
                if name == r_recipe.name:
                    print(name, ":", r_recipe.ingredients)
                    return r_recipe
        raise TypeError("Recipe_name is not in the list")

    def get_recipes_by_types(self, recipe_type):
        if recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                print(recipe.name)
        else:
            raise TypeError("Recipe_type is not in the list")

    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe) and recipe not in self.recipes_list[recipe.recipe_type]:
            self.recipes_list[recipe.recipe_type].append(recipe)
        else:
            raise TypeError("Recipe is not in class Recipe or already is in the list")

