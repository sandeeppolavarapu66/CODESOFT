import random
import string
def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Define the possible characters for the password
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Generate the password
    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
    else:
        raise ValueError("No character sets selected. Please enable at least one character set.")

    return password
def main():
    print("Welcome to the Password Generator!")

    # Get the desired password length from the user
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Get the complexity options from the user
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Generate and display the password
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
