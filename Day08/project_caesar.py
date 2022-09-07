from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

should_end = False
while not should_end:

    while True:
        try:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            if direction == "encode" or direction == "decode":
                break
        except:
            print("", end="")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 #ensures the shift number is always between 1 and 26


    def encrypt(text, shift):
        cipher_text = ""
        for i in text:
            if i == " " or i not in alphabet:
                cipher_text += i
            else:
                if alphabet.index(i) + shift > (len(alphabet)-1):
                    cipher_text += alphabet[(alphabet.index(i) + shift) - len(alphabet)]
                else:
                    cipher_text += alphabet[alphabet.index(i) + shift]

        print(f"The encoded text is {cipher_text}")

    def decrypt(text, shift):
        cipher_text = ""
        for i in text:
            if i == " " or i not in alphabet:
                cipher_text += i
            else:
                cipher_text += alphabet[alphabet.index(i) - shift] #list out of range error doesn't happen beacause we can use negative integers (-1, -2) as index in python lists.

        print(f"The decoded text is {cipher_text}")

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text,shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
