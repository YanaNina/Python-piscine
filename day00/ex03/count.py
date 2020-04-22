#text = input()

def text_analyzer(text=None):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if text == None:
        print("What is the text to analyse?")
        text = input()
    my_count = 0
    my_upper = 0
    my_lower = 0
    my_punct = 0
    my_spaces = 0
    punctuation = ",.?!-'"
    for char in text:
        my_count += 1
        if char.isupper():
            my_upper += 1
        if char.islower():
            my_lower += 1
        if char.isspace():
            my_spaces += 1
        if char in punctuation:
            my_punct += 1

    print("The text contains", my_count, "characters:")
    print("-", my_upper,"upper letters")
    print("-", my_lower, "lower letters")
    print("-", my_punct, "punctuation marks")
    print("-", my_spaces, "spaces")

#text_analyzer()
