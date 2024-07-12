import csv
import random
import sys
from tabulate import tabulate
## used to help the tabulate not break with emojis
tabulate.WIDE_CHARS_MODE = True


def main ():
    try:
        ## opens csv
        with open("wordles.csv", "r") as csvfile:
            file = csv.reader(csvfile)
            table = []
            for row in file:
                table.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    tracker = []
    headers = ["Round", "Guessed", "Guess Check"]
    tracker.append(headers)
    n = get_random()
    wordle = get_word(table, n)
    tries = 1
    ## creates a loop for 6 guesses
    while tries <= 6:
        try:
            word = guess(tries).lower()
            length_alpha = check_length_alpha(word)
            if length_alpha == True:
                for line in table:
                    line = ''.join(line)
                    ## checks for if the guess is a word
                    if line in word:
                        ## checks for if the guess is correct
                        if word == wordle:
                            tracker.append([tries, word, "🟢🟢🟢🟢🟢"])
                            print(tabulate(tracker, headers="firstrow", tablefmt="fancy_grid"))
                            print("Correct you have won!")
                            print(f"It took you {tries} tries")
                            ## used to exit the while loop
                            tries = 8
                        ## checks to see what letters are correct
                        else:
                            track = validate(word, wordle)
                            tracker.append([tries, word, track])
                            print(tabulate(tracker, headers="firstrow", tablefmt="fancy_grid"))
                            tries = round_attempts(tries)
            else:
                print("Please re-enter a 5 letter word")
        except:
            pass
    if tries == 7:
        print("You lost")
        print(f"The word was {wordle}")


## gets a random number within the range of the csv
def get_random():
    n = random.randrange(1, 5757)
    return n


## gets the word using the csv and random number
def get_word(table, n):
    wordle_list = table[n]
    wordle = ''.join(wordle_list)
    return wordle


## gets the guess input
def guess(tries):
    word = input(f"Guess {tries} ")
    return word


## checks length of word and if all are letters
def check_length_alpha(word):
    if len(word) == 5 and word.isalpha() == True:
        return True
    else:
        return False


## updates round attempts
def round_attempts(tries):
    tries += 1
    return tries


##checks for if letters are in words
def validate(word, wordle):
    track = ""
    for i in range(5):
        if word[i] == wordle[i]:
            track += "🟢"
        elif word[i] in wordle:
            track += "🟡"
        else:
            track += "🔴"
    return track


if __name__  == "__main__":
    main()
