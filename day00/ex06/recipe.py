
recipes = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad":{
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}
def add_recipe():
    print("Please enter a recipe name:")
    new_recipe_name = input()
    print("Please enter ingredients comma separated:")
    ingredients = input()
    lst = []
    lst.append(ingredients)
    print("Please enter the type of meal:")
    meal_type = input()
    print("Please enter preparation time in minutes:")
    time = int(input())
    recipes[new_recipe_name] = {"ingredients": lst,
                   "meal": meal_type,
                   "prep_time" : time}
    print("\nYour receipt was successfully added!")

def delete_recipe():
    print("Please enter which recipe to delete: ")
    to_delete = input()
    del recipes[to_delete]
    print("\nYour receipt was successfully deleted!")

while True:
    print("\n")
    print("Please select an option by typing the corresponding number:\n1: "
           "Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")
    number = input()
    if number == "1":
        add_recipe()
    elif number == "2":
        delete_recipe()
    elif number == "3":
        print("Please enter the recipe's name to get its details:")
        recipe_name = input()
        print("Recipe for cake:\n\nIngredients list:{}\nTo be eaten for {}."
              "\nTakes {} minutes of cooking.".format(*recipes[recipe_name].values()))
    elif number == "4":
        print("Our recipes:")
        for key in recipes:
            print("-",key)
    elif number == "5":
        print("Cookbook closed")
        exit()
    else:
        print("This option does not exist, please type the corresponding number. To exit, enter 5.")


