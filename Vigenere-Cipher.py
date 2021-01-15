###########################################
# Vigenere Cipher using python
# Nishant Tomar
# 2020PMD4210
###########################################


# Importing regex library
import re

# Key and character to integer value
key = "PASCAL"
character_value = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# Checking if the message has whitespace
def check_whitespace(string):
    return True if " " in string else False


# Checks if the input message contains any number
def has_numbers(input):
    return any(character.isdigit() for character in input)


# Check if any illegal characters present in the string
def check_illegal_char(input):
    regex = re.compile("[@_!#$%^&*()<>?/\|}{~:]")                                                                                 # Regex

    return True if regex.search(input) == None else False


# Checking of input string
def check_input(input):
    # Checking all valid conditions if true
    if not has_numbers(input) and not check_whitespace(input) and check_illegal_char(input):
        return True

    return False


# To take plain-text input from the user (Message to be encrypted)
def take_input():
    print("\n\n########################################")
    print("\t\t\tVIGENERE CIPHER")
    print("########################################\n\n")
    input_string = ""

    # Loop till the input is not valid
    while True:
        input_string = input("Enter your message to be encrypted in capital-letters: ").upper()             # Converting input message to upper-case
        flag = check_input(input_string)

        if flag:
            break
        else:
            print("\nPlease try again (Invalid input)!")

    return input_string


# To generate the key stream according to the message length
def generate_key_stream(text):
    key_stream_string = ""

    # Loop till message length
    for index, character in enumerate(text):
        key_stream_string += key[index % len(key)]

    return key_stream_string


# To convert the string to its corresponding value
def convert_string_to_values(string):
    string_value = []

    # Loop till string length and retrieve the index value from character_value array
    for character in string:
        string_value.append(character_value.index(character))

    return string_value


# To convert the integer values to character values
def convert_values_to_string(integer_array):
    string = ""

    # Loop till array length and keep appending each integer value to its character value
    for value in integer_array:
        string += character_value[value]

    return string


# Cipher formula [C(i) = {P(i) + K(i)} mod 26]
def cipher_formula(text, key):
    cipher_value = []

    # Loop till text length and keep applying cipher formula on each iteration
    for index, value in enumerate(text):
        cipher_value.append((value + key[index]) % 26)

    return cipher_value


# Decipher formula [D(i) = {C(i) - K(i)} mod 26]
def decipher_formula(text, key):
    decipher_value = []

    # Loop till text length and keep applying decipher formula on each iteration
    for index, value in enumerate(text):
        decipher_value.append((value - key[index]) % 26)

    return decipher_value


# Function to encrypt the message
def encryption(text, key_stream):
    # Get the integer values corresponding to the characters
    text_value = convert_string_to_values(text)
    key_stream_value = convert_string_to_values(key_stream)

    # To get the cipher integer value
    cipher_value = cipher_formula(text_value, key_stream_value)

    # To get the cipher string
    cipher_string = convert_values_to_string(cipher_value)

    print("\n\nEncrypted Message: " + cipher_string)

    return cipher_value, key_stream_value


# Function to decrypt the encrypted message
def decryption(cipher, key):
    # To get decipher integer value
    decipher_value = decipher_formula(cipher, key)

    # To get the decipher string
    decipher_string = convert_values_to_string(decipher_value)

    print("\n\nDECRYPTED MESSAGE: " + decipher_string + "\n")


# So that this function doesn't run when some other file imports this file
if __name__ == "__main__":
    message = take_input()
    key_stream = generate_key_stream(message)
    cipher_value, key_stream_value = encryption(message, key_stream)
    decryption(cipher_value, key_stream_value)
