def findPos():
    str_input = input("Enter String : ").lower()
    target_char = input("Enter Character : ")

    for index, char in enumerate(str_input):
        if char == target_char:
            print(f"Character found at position : {index + 1}")

def findPosNew():
    # .lower() on both inputs ensures a perfect, case-insensitive match
    str_input = input("Enter String : ").lower()
    target_char = input("Enter Character : ").lower()
    
    found = False  # Track if we found at least one match

    for index, char in enumerate(str_input):
        if char == target_char:
            print(f"Character found at position : {index + 1}")
            found = True

    if not found:
        print("Character not found in the string.")

if __name__ == "__main__":
    findPosNew()
