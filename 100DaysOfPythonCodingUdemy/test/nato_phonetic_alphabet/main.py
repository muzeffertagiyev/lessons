import pandas

# getting data from our file 
data = pandas.read_csv('nato_phonetic_alphabet.csv')

# creating dictionary from our file's content
nato_alphabet_dict = {value.letter: value.code for (index, value) in data.iterrows()}

def nato_alphabet():
    try:
        user_input = input('Enter a word: ').upper()
         # creating a list from entered word's letters
        word_list = [nato_alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        nato_alphabet()
    else:
        print(word_list)

nato_alphabet()