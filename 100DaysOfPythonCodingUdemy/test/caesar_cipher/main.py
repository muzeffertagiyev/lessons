from turtle import position
from alphabet import alphabet
from art import logo


def caesar(start_text,shift_amount,start_direction):
    end_text=""

    if start_direction=='decode':
        shift_amount*=-1
    for letter in start_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=letter
    
    print(f"Here's {start_direction} the encodedd result: {end_text}")


print(logo)

end_of_game=False


while not end_of_game:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").replace(' ','').lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caesar(start_text=text,shift_amount=shift,start_direction=direction)

    confirm_direction=input("Type 'yes' if you want to Continue, or type 'no' to End the app:\n").lower().replace(' ','')

    if confirm_direction=='no':
        end_of_game=True
        print('App ended')
        





