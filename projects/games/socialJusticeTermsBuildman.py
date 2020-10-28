import random
terms = ["equality", "blacklivesmatter", "allyship",
         "equity", "feminism", "tolerance"]

guessedIncorrect = []
chosenWord = random.choice(terms)
print(chosenWord)

guessedCorrect = ["_"] * len(chosenWord)

def print_man(count):
    if count > 0:
        print(" 0")
    if count == 2:
        print(" |")
        print(" |")
    if count == 3:
        print("/|")
        print(" |")
    if count >= 4:
        print("/|\\")
        print(" |")
    if count == 5:
        print("/")
    if count == 6:
        print("/ \\")


while len(guessedIncorrect) < 6 and "_" in guessedCorrect:
    nextLetter = input("Guess a letter: ")
    while not nextLetter.isalpha():
        nextLetter = input("Input was not a letter. Please input a valid letter: ")
    inWord = False
    for i in range(len(chosenWord)):
        if(chosenWord[i] == nextLetter):
            guessedCorrect[i] = nextLetter
            inWord = True
    if inWord == False and nextLetter not in guessedIncorrect:
        guessedIncorrect.append(nextLetter)

    print("Incorrect Guesses:")
    print(guessedIncorrect)
    print()
    print_man(len(guessedIncorrect))
    print()
    print("Word so far:")
    print(''.join(guessedCorrect))

if(len(guessedIncorrect) == 6):
    print("Oh no! You didn't get the word. The word is: " + chosenWord)
else:
    print("You got the word!")
