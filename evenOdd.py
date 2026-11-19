def evenOdd():
    for i in range(1, 21):
        if i % 2 == 0:
            print(f"{i} is even")
        else : 
            print(f"{i} is odd")

def evenOddTernary():
    for i in range(1, 21):
        status = "even" if i % 2 == 0 else "odd"
        print(f"{i} is {status}")

if __name__ == "__main__":
    evenOdd()
    evenOddTernary()