from sys import argv

a = len(argv)
while a > 1:
    result = argv[a - 1][::-1].swapcase()
    if a > 2:
        print(result, end = ' ')
    else:
        print(result)
    a -= 1

# doesn't work with exclamation mark

