import pandas as pd
nato_contents = pd.read_csv("nato_phonetic_alphabet.csv")
nato_contents_dict = {row.letter : row.code for (index, row) in nato_contents.iterrows()}

def generate_phonetic():
    input_word = input("Type in the word you want to find its NATO phonetic: ").upper()
    try:
        print([nato_contents_dict[letter] for letter in input_word])
    except KeyError:
        print("Sorry, only alphabet is allowed. Please try again.")
        generate_phonetic()
        
generate_phonetic()