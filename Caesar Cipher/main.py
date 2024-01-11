from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_count, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_count *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_count
            end_text += alphabet[new_position % len(alphabet)]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_count=shift, cipher_direction=direction)
    restart = input(f"Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == 'no':
        should_continue = False
        print("Goodbye")
