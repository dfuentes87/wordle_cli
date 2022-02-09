#!/usr/bin/env python3

from rich import print
from rich.console import Console
from rich.theme import Theme
from datetime import datetime
import game

custom_theme = Theme({
    "correct": "bold green3",
    "almost": "bold gold1",
    "wrong": "bold grey100"
})
console = Console(theme=custom_theme)

# load the game data in following order: wins, losses, epoch date, line # of last word
# lines[2] = 0000 indicates a first run of the game
try:
    with open("data.txt", "r") as data:
        lines = data.readlines()
        wins = lines[0].strip()
        losses = lines[1].strip()
        last_day = int(lines[2])
        daily_word = int(lines[3])
        # if this is a first run or the last word in the list, (re)start from the beginning
        # otherwise continue from the previous word
        if last_day == 0000 or daily_word == 5762:
            daily_word = lines[5].strip()
        else:
            daily_word = lines[3]
            
except FileNotFoundError:
    print("You are missing data.txt. Exiting.")
    quit()

# game introduction
print()
console.print("[correct]W[/correct] [wrong]O[/wrong] [wrong]R[/wrong] [almost]D[/almost] [wrong]L[/wrong] [correct]E[/correct]")
print(f"""
Guess the five letter word in six tries or less. The word changes daily.
The game will save your wins and losses as you progress.

[bold]Statistics:[/bold]
Wins: [green3]{wins}[/green3]
Losses: [red]{losses}[/red]

To begin playing, type 'start'. To reset your score (but not the word), type 'reset'. To exit, type 'exit'.
""")

while True:
    user = input('% ')
    if user == 'exit':
        print("Thanks for playing!")
        break
    elif user == 'start':
        print()
        # check if it's a new game/day
        today = datetime.now()
        if last_day == today:
            print("You've already played today. Wait until tomorrow for a new word.")
            break
        else:
            game.run(daily_word)
    # reset score (does not reset word)
    elif user == 'reset':
        with open("data.txt", "r+") as data:
            lines = data.readlines()
            lines[0] = 0
            lines[1] = 0
            data.write()
        print("Score has been reset.\n")
    else:
        print("You must enter a valid command.\n")
