import random


text = "Le Lorem Ipsum est simplement du du faux texte."
def generator(text, sep = " ", option=None):

    new_text = text.split(sep)
    if option == "shuffle":
        random.shuffle(new_text)
    elif option == "ordered":
        new_text.sort()
    elif option == "unique":
        new_text = set(new_text)
    elif option != None:
        raise TypeError("Check option")

    for i in new_text:
        yield i


for value in generator(text,sep= " ",option="2"):
    print(value)






