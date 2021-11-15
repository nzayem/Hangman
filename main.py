import random

print("H A N G M A N")

while True:

    choice = input("Type \"play\" to play the game, \"exit\" to quit: ")

    if choice == "exit":
        break

    elif choice == "play":

        print()

        languages = ['python', 'java', 'kotlin', 'javascript']
        rand = random.randint(0, len(languages) - 1)

        word = languages[rand]

        hidden = ""

        # Hiding the word with '-':

        for item in word:
            hidden += "-"

        print(hidden)

        list_hidden = list(hidden)
        list_indexes = []

        tries = 8
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        guesses = []

        while tries != 0:

            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("You should input a single letter")

            elif letter not in alphabet:
                print("Please enter a lowercase English letter")

            elif letter in guesses or letter in ''.join(list_hidden):
                print("You've already guessed this letter")

            elif letter not in word:
                print("That letter doesn't appear in the word")
                guesses.append(letter)
                tries -= 1

            if letter in word:

                for i in range(len(word)):
                    if word[i] == letter:
                        list_indexes.append(i)
                        list_hidden[i] = letter

            if tries == 0 and ''.join(list_hidden) != word:
                print("You lost!")
                break

            if ''.join(list_hidden) == word:
                print("You guessed the word!\nYou survived!")
                break

            print()

            print(''.join(list_hidden))
