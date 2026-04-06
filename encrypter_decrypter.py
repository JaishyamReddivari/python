import string
letters = string.ascii_letters

def secret_message():
    start = input("Type 'encode' to encrypt. Type 'decode' to decrypt.\n")
    if start == "encode":
        message = input("Type your message.\n")
        shift = int(input("Type the shift number.\n"))
        encrypted_message = ""
        for letter in message:
            if letter in letters:
                index = letters.index(letter)
                letter = letters[index + shift]
                encrypted_message += letter + ""
            else:
                encrypted_message += letter + ""

        print(f"Here's the encoded result: {encrypted_message}")

    elif start == "decode":
        message = input("Type your message.\n")
        shift = int(input("Type the shift number.\n"))
        decrypted_message = ""
        for letter in message:
            if letter in letters:
                index = letters.index(letter)
                letter = letters[index - shift]
                decrypted_message += letter + ""
            else:
                decrypted_message += letter + ""

        print(f"Here's the encoded result: {decrypted_message}")
    else:
        print("Invalid Input!")

while True:
    secret_message()
    cont = input("Type 'Yes' if you want to go again. 'No' if you want to quit.\n")
    if cont != "yes":
        print("END")
        break
