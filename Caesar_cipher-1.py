alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
# example:
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"
# -----------------------------------
# 1- take the inputs : dicretion - text - shift
direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# 2- define a function called 'encrypt' with two inputs that takes text and shift:
# inside function , shift each letter of the text forwards in alphabet list
def encrypt(plain_text,shift_amount):
    cipher_text =""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

# 3- call the encrypt function
encrypt(plain_text=text, shift_amount=shift)
# or
# encrypt(text,shift)



