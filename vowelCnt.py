def vowelCount():
    vowels = ["a","e","i","o","u"]

    str_input = input("Enter String : ")
    cnt = 0

    for i in str_input.lower():
        if i in vowels:
            cnt = cnt + 1

    print(f"The no of vowels found are : {cnt}")

def newCount():
    str_input = input("Enter String : ")
    cnt = 0

    for i in str_input.lower():
        if i in "aeiou":
            cnt += 1

    print(f"The no of vowels found are : {cnt}")

def vowelCountNew():
    str_input = input("Enter String : ")
    
    # 1. Filters and creates a 1 for every vowel found
    # 2. sum() adds all those 1s together instantly
    cnt = sum(1 for i in str_input.lower() if i in "aeiou")

    print(f"The no of vowels found are : {cnt}")


if __name__ == "__main__":
    newCount()