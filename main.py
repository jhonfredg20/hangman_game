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
    with open('./files/data.txt', 'r', encoding='utf-8') as data:
        # The method str.rstrip() removes the line breaks (\n)
        words = {str.rstrip(word) for word in data} # Generate a dictionary with the words in data 
        words = dict(enumerate(words)) # Add a key to the dictionary
    word = [letter for letter in normalize(words.get(number_word))] # Select a word at random and separate its letters into a list.
    return word


def system_clear(system):
    # Check if the system is equal to Windowns (w)
    if system == 'w':
        os.system('cls')
    else:
        os.system('clear')


def interface(word, clue, attempts):
    interface = f'''
__________________________________________________
{'TRY TO GUESS THE WORD!'.center(50)}
{''.join(clue).center(50)}
{f'Attempts: {attempts}'.center(50)}
--------------------------------------------------'''.center(50)
    if attempts == 1:
        interface = f'''
____________________________________________
             +---+ 
            /    ! 
           o     ! {''.join(clue)}
          /|\    ! 
          /      ! 
                 ! Remaining attempts: {attempts}
--------------------------------------------'''
    elif attempts == 2:
        interface = f'''
____________________________________________
             +---+ 
            /    ! 
           o     ! {''.join(clue)}
          /|\    ! 
                 ! 
                 ! Remaining attempts: {attempts}
--------------------------------------------'''
    elif attempts == 3:
        interface = f'''
____________________________________________
             +---+ 
            /    ! 
           o     ! {''.join(clue)}
          /|     ! 
                 ! 
                 ! Remaining attempts: {attempts}
--------------------------------------------'''
    elif attempts == 4:
        interface = f'''
____________________________________________
             +---+ 
            /    ! 
           o     ! {''.join(clue)}
           |     ! 
                 ! 
                 ! Remaining attempts: {attempts}
--------------------------------------------'''
    elif attempts == 5:
        interface = f'''
____________________________________________
             +---+ 
            /    ! 
           o     ! {''.join(clue)}
                 ! 
                 ! 
                 ! Remaining attempts: {attempts}
--------------------------------------------'''
    elif attempts == 6:
        interface = f'''
____________________________________________
             +---+ 
            /    ! 
                 ! {''.join(clue)}
                 ! 
                 ! 
                 ! Remaining attempts: {attempts}
--------------------------------------------'''
    elif attempts == 7:
        interface = f'''
____________________________________________
             +---+ 
                 ! 
                 ! {''.join(clue)}
                 ! 
                 ! 
                 ! Remaining attempts: {attempts}
--------------------------------------------'''
    elif attempts == 8:
        interface = f'''
____________________________________________
              ---+ 
                 ! 
                 ! {''.join(clue)}
                 ! 
                 ! 
                 ! Remaining attempts: {attempts}
--------------------------------------------'''
    elif attempts == 9:
        interface = f'''
____________________________________________
               --+ 
                 ! 
                 ! {''.join(clue)}
                 ! 
                 ! 
                 ! Remaining attempts: {attempts}
--------------------------------------------'''
    return interface

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
                attempts -= 1 # If no matches are found, subtract one from the attempts
    return clue, attempts # Returns the clue and attempts remaining
         


def main():
    # Variables
    word = words() # Receives the data word as a list
    attempts = 10
    clue = ['_' for i in word] # List of "_" of the same length as the word


    # Check the operating system the scrip is running from
    system = input('If your system is Windowns enter a "w": ')


    # Loop
    while clue != word and attempts > 0:
        # Generation of the Interface
        system_clear(system.lower())
        print(interface(word, clue, attempts))

        # Letter an Exception Management
        letter = input('Enter a letter: ') 
       #  if letter.isnumeric() or int(letter) < 0:
        if letter.isnumeric():
            raise ValueError('Numbers can not be entered. Please, try again.')

        # Function that verifies if there is the letter matches the word
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
            /    ! YOU FAILED, GAME OVER!
           o     ! 
          /|\    ! Word: {"".join(word)}
          / \    ! Puntuation: {attempts * 10}/100
                 ! Remaining attempts: {attempts}
--------------------------------------------'''
        print(defeat)



if __name__ == '__main__':
    main()
