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
def word():
    number_word = random.randint(0, 170) # Generate a random number between 0 and 170
    with open('./archivos/data.txt', 'r', encoding='utf-8') as data:
        # The method str.rstrip() removes the line breaks (\n)
        words = {str.rstrip(word) for word in data} # Generate a dictionary with the words in data 
        words = dict(enumerate(words)) # Add a key to the dictionary
    word = [lyrics for lyrics in normalize(words.get(number_word))]
    return word
    
 

def game():
    pass


def main():
    print(word())


if __name__ == '__main__':
    main()
