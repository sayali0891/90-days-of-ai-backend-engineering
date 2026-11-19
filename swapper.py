#Program 1: The SwapperTask: Take two numbers, A = 5 and B = 10. Swap their values so A becomes 10 and B becomes 5.Constraint: Try doing it first using a third temporary variable, and then try doing it without a third variable.

def swapVar3() :
    a = int(input("Enter 1st no : "))
    b = int(input("Enter 2nd no : "))

    c = a
    a = b
    b = c

    print(f"Swapped : No1 = {a} and No2 = {b}")


def swapVar():
    a = int(input("Enter 1st no : "))
    b = int(input("Enter 2nd no : "))

    a = a + b
    b = a - b
    a = a - b

    print(f"Swapped : No1 = {a} and No2 = {b}")

def swapNew():
    a = int(input("Enter 1st no : "))
    b = int(input("Enter 2nd no : "))

    a, b = b, a

    print(f"Swapped : No1 = {a} and No2 = {b}")


if __name__ == "__main__" :
    swapVar3()
    swapVar()
    swapNew()