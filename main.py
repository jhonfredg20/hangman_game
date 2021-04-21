import os
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


def system_clear(system):
    if system == 'w':
        os.system('cls')
    else:
        os.system('clear')


def interface(word, clue, attempts):
    if attempts == 9:
        interface = f'''

        '''


def game(word, clue, letter, attempts):
    end_loop = 0 # Loop repetitions counter 
    coincidence = 0 # Match indentifier
    for i, l in enumerate(word): 
        end_loop += 1 
        if l.lower() == letter.lower() and attempts > 0: 
            clue[i] = l # Add the letter in the corresponding index
            coincidence += 1 
        else: 
            if end_loop == len(word) and coincidence == 0: 
                attempts -= 1 
    return clue, attempts
         


def main():
    # Variables
    word = words()
    attempts = 10
    clue = ['_' for i in word]
    system = input('If your system is Windowns enter a "w": ')


    # Loop
    while clue != word and attempts > 0:
        system_clear(system)
        print(interface(word, clue, attempts))
        letter = input('Enter a letter: ')
        clue, attempts = game(word, clue, letter, attempts)


    # Victory
    if clue == word and attempts > 0:
        system_clear(system)
        victory = f'''
____________________________________________
  VICTORY!!!                                  
    \o/        Word: {"".join(word)}          
     |         Puntuation: {attempts * 10}/100                
    / \        Remaining attempts: {attempts}       
--------------------------------------------'''
        print(victory)


    # Defeat
    elif clue != word and attempts == 0:
        system_clear(system)
        defeat = f'''
____________________________________________
             +---+
            /    !
           o     ! Word: {"".join(word)}
          /|\    ! Puntuation: {attempts * 10}/100
          / \    ! Remaining attempts: {attempts}
                 !
--------------------------------------------
You Failed, Game Over!
'''
        print(defeat)



if __name__ == '__main__':
    main()
