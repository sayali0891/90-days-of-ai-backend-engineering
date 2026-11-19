def palindrome():
    str_input = input("Enter string : ")
    pal = True

    # The exact equivalent of your C logic using negative indexing
    for i, char in enumerate(str_input):
        if char != str_input[-1 - i]:
            pal = False
            break

    # We integer divide (//) by 2 so we only loop to the middle
    # for i, char in enumerate(my_string[:len(my_string) // 2]):
    #     if char != my_string[-1 - i]:
    #         pal = False
    #         break

    if pal:
        print("String is palindrome")
    else:
        print("String is not a palindrome")


# Using string slicing 
def palindrome_slicing(): 
    user_input = input("Enter a string: ")

    # Convert to lowercase to ensure case-insensitivity
    cleaned_string = user_input.lower()

    # Check if the string is equal to its reverse
    if cleaned_string == cleaned_string[::-1]:
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")

# Using 2 pointer technique
def is_palindrome(text):
    text = text.lower()
    left = 0
    right = len(text) - 1
    
    # Compare characters from both ends moving inward
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")


