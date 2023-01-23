import pandas as pd
nato_contents = pd.read_csv("nato_phonetic_alphabet.csv")
nato_contents_dict = {row.letter : row.code for (index, row) in nato_contents.iterrows()}

input_word = input("Type in the word you want to find its NATO phonetic: ").upper()
print([nato_contents_dict[letter] for letter in input_word])