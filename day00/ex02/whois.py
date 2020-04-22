from sys import argv

if len(argv) == 2 and argv[1].isdecimal():
    if argv[1] == '0':
        print("I'm Zero.")
    elif (int(argv[1]) % 2 != 0):
        print("I'm Odd.")
    else:
        print("I'm Even.")
else:
    print("ERROR")

