import sys
length = len(sys.argv)


if length == 3 and not sys.argv[1].isdigit() and sys.argv[2].isdigit():
    print(list(i for i in sys.argv[1].replace(",","").split(" ") if len(i) > int(sys.argv[2])))
else:
    print("ERROR")



