from random import randint as number
from os import system as clear
import hangman_art as art
import hangman_word as word

chosen_word = word.word_list[number(0, len(word.word_list))-1]
blanks = ""
correct = False
incorrect = 0
used_words = []

print("Welcome to")
print(art.logo)

for i in range(len(chosen_word)):
    blanks += "_ "

blanksList = list(blanks)
for i in range(int(len(blanksList)/2)):
    blanksList.remove(" ")
print(f"\nThe word is: {blanks}")

def game():
    global chosen_word
    global blanks
    global correct
    global incorrect
    global used_words
    global blanksList
    if '_' in blanksList and incorrect < 6:
        guess = input("Guess a letter of the word!").lower()
        if guess in used_words or len(guess) != 1:
            print("You can not use that letter!\n")
            return game()
        else:
            used_words.append(guess)
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                blanksList = list(blanks)
                blanksList[i*2] = guess
                blanks = ""
                correct = True
                for j in range(len(blanksList)):
                    blanks += blanksList[j]
                for i in range(int(len(blanksList)/2)):
                    blanksList.remove(" ")
        else:
            clear("clear")
            if not correct:
                correct = False
                incorrect += 1
                print(f"That Letter is not in the Word\n You have {6-incorrect} guesses left!")
                print(art.stages[6-incorrect])
            else:
                correct = False
                print(f"That is correct!\n You have {6-incorrect} guesses left!")
                print(art.stages[6-incorrect])
            print(blanks)
            return game()
    elif incorrect >= 6:
        print("You Lose")
        print(f"The word was {chosen_word}!")
        return game
    elif '_' not in blanksList:
        print("You Win!")   
        return game
    else:
        print("Failed to Calculate..")
        return game
game()