def factorial():
    N = int(input("Enter no : "))
    mul = 1

    for i in range(1,N + 1):
        mul *= i

    print(f"mul of nos is : {mul}")

if __name__ == "__main__":
    factorial()