def caseFlipperASCII():
    str_input = input("Enter String: ")
    flipped_str = ""

    for char in str_input:
        ascii_val = ord(char)

        # Check if the character is an Uppercase letter (A-Z: 65 to 90)
        if 65 <= ascii_val <= 90:
            flipped_str += chr(ascii_val + 32)  # Add 32 to make it lowercase
            
        # Check if the character is a Lowercase letter (a-z: 97 to 122)
        elif 97 <= ascii_val <= 122:
            flipped_str += chr(ascii_val - 32)  # Subtract 32 to make it uppercase
            
        # If it's a number, space, or symbol, keep it exactly as it is
        else:
            flipped_str += char

    print(f"Flipped String: {flipped_str}")

def caseFlipperManual():
    str_input = input("Enter String: ")
    flipped_str = ""  # Start with an empty string

    for char in str_input:
        if char.isupper():
            flipped_str += char.lower()  # Convert to lowercase and append
        else:
            flipped_str += char.upper()  # Convert to uppercase and append

    print(f"Flipped String: {flipped_str}")


if __name__ == "__main__":
    caseFlipperASCII()
    caseFlipperManual()
