#!/usr/bin/env python3

from rich import print
from rich.console import Console
from rich.theme import Theme
from datetime import datetime

custom_theme = Theme({
    "correct": "bold green3",
    "almost": "bold gold1",
    "wrong": "bold grey100"
})
console = Console(theme=custom_theme)

def update_data(score):
    with open("data.txt", "r+") as data:
        lines = data.readlines()
        if score is True:
            lines[0] += 1
        else:
            lines[1] += 1
        lines[2] = datetime.now()
        lines[3] += 1
        data.write()


def word_processing(word_list,guess_list):
    pass


def run(daily_word):
    word = daily_word.upper()
    word_list = list(word)

    letters = ("\n"
    "Q W E R T Y U I O P\n"
    " A S D F G H J K L\n"
    "  Z X C V B N M"
    )
    spaces = ("""    [][][][][]""")
    
    print(letters)
    print()
    print(spaces)

    guess_num = 0
    while guess_num < 7:
        guess = input("\n% ")

        if guess.isalpha() and len(guess) == 5:
            guess = guess.upper()

            if guess == word:
                console.print(f"\n  [correct]{word}[/correct]")
                print("\nCongrats, you got it!")
                #update_data(True)
                print("The word will change after midnight. bye!")
                quit()
            else:
                guess_list = list(guess)
                word_processing(word_list,guess_list)
        else:
            print("Your guess must be a five letter word.")
        
