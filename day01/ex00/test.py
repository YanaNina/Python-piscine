from book import Book
from recipe import Recipe

if __name__ == '__main__':
    pasta_pomodoro = Recipe(name='Spaghetti Pomodoro',
                            cooking_lvl=3,
                            cooking_time=15,
                            ingredients=['spaghetti', 'garlic', 'tomatoes',
                                         'basil', 'parmesan'],
                            description='Pasta with tomato sauce and parmesan',
                            recipe_type='lunch',
                            )
    big_book = Book('Big Recipe Book')
    big_book.add_recipe(pasta_pomodoro)
    big_book.get_recipe_by_name(pasta_pomodoro.name)
    big_book.get_recipes_by_types(pasta_pomodoro.recipe_type)



