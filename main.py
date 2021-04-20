import random


# Normalize the text
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


# Generate the words
def words():
    number_word = random.randint(0, 170) # Generate a random number between 0 and 170
    with open('./archivos/data.txt', 'r', encoding='utf-8') as data:
        # The method str.rstrip() removes the line breaks (\n)
        words = {str.rstrip(word) for word in data} # Generate a dictionary with the words in data 
        words = dict(enumerate(words)) # Add a key to the dictionary
    word = [letter for letter in normalize(words.get(number_word))] # Select a word at random and separate its letters into a list.
    return word


def interface(word, clue, oportunities):
    pass


def game():
    word = words()
    oportunities = 10
    clue = ['_' for i in word]
    print("".join(word))
    while clue != word:
        print("".join(clue))
        letter = input('Enter a letter: ')
        for i, l in enumerate(word):
            if l.lower() == letter.lower():
                clue[i] = l


def main():
    game()


if __name__ == '__main__':
    game()
