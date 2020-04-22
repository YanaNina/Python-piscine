from sys import argv

try:
    a = int(argv[1])
    b = int(argv[2])
except:
    print("InputError: only numbers")
    print("Usage: python operations.py\nExample:\n    python operations.py 10.3")
    exit(1)

if len(argv) == 3:
    try:
        print("Sum:", a + b)
        print("Difference:", a - b)
        print("Product:", a * b)
        print("Quotient:",a / b)
        print("Remainder:",a % b)
    except ZeroDivisionError:
        print("Quotient: ERROR (div by zero)")
        print("Remainder: ERROR (modulo by zero)")
else:
    print("InputError: too many arguments")
    print("Usage: python operations.py\nExample:\n    python operations.py 10.3")


