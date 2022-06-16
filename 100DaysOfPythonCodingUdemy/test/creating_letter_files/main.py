with open('./Input/Names/invited_names.txt') as invited_names:
    names = invited_names.readlines()


with open('./Input/Letters/starting_letter.txt') as starting_letter:
    letter = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letters = letter.replace('[name]', stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}', mode='w') as created_letters:
            created_letters.write(new_letters)