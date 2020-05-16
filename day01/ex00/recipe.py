class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = None):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

        self.input_error_chk()

    def input_error_chk(self):

        types = ["starter", "lunch", "dessert"]
        if not isinstance(self.name, str):
            raise TypeError("Should be a string.")
        if not isinstance(self.cooking_lvl, int) or self.cooking_lvl not in range(1, 5):
            raise TypeError("Should be an integer in range 1 to 5.")
        if not isinstance(self.cooking_time, int) or self.cooking_time < 0:
            raise TypeError("Should be an integer and no negative.")
        if not isinstance(self.ingredients, list):
            raise TypeError("Should be a list.")
        for i in range(len(self.ingredients)):
            if not isinstance(self.ingredients[i], str):
                raise TypeError("Should be a starter, lunch or dessert.")
        if not isinstance(self.recipe_type, str) or self.recipe_type not in types:
            raise TypeError("Should be a string.")


    def __str__(self):
        return f'Description is: {self.description}.'

#
# pasta = Recipe("pomodoro",2,30,["spaghetti","pepper","tomatoes"],"lunch", "Vlad's favorite dish")
# print(pasta)
# print(pasta.name)
# print()