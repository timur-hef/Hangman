import random

list = "python", "java", "kotlin", "javascript"

alphabet = "qwertyuiopasdfghjklzxcvbnm"

print("H A N G M A N")
choice = input('Type "play" to play the game, "exit" to quit:')
while (choice != "play") and (choice != "exit"):
    choice = input('Type "play" to play the game, "exit" to quit:')

while choice == "play":
    word = random.choice(list)
    mistake = 0
    result = "-" * len(word)
    all_letters = set()
    right_letters = set()
    while mistake < 8:
        print("\n" + result)
        letter = input("Input a letter:")

        if (letter in word) and (letter not in result):
            right_letters.add(letter)
            result = word
            for i in word:
                if (i not in right_letters):
                    result = result.replace(i, "-")
        elif letter in all_letters:
            print("You've already guessed this letter")
        elif len(letter) != 1:
            print("You should input a single letter")
        elif letter not in alphabet:
            print("Please enter a lowercase English letter")
        else:
            print("That letter doesn't appear in the word")
            mistake += 1

        if "-" not in result:
            print(f'You guessed the word {result}!')
            print("You survived!")
            break

        if letter in alphabet:
            all_letters.add(letter)

    if mistake == 8:
        print("You lost!")

    choice = input('\nType "play" to play the game, "exit" to quit:')
    while (choice != "play") and (choice != "exit"):
        choice = input('Type "play" to play the game, "exit" to quit:')

