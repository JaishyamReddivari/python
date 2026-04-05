import random

words = [
    "apple", "bicycle", "cloud", "dragon", "eclipse",
    "forest", "guitar", "hammer", "island", "jungle",
    "kettle", "lantern", "marble", "needle", "ocean",
    "puzzle", "quartz", "rocket", "sunset", "tiger",
    "umbrella", "volcano", "whistle", "xylophone", "yogurt",
    "zipper", "candle", "breeze", "pillow", "thunder"
]

print("Welcome to Hangman Game. Get ready to guess words!")
start = input("Type 'Start' to start the game!\n")

if start.lower() == "start":
    word = random.choice(words)
    guessed_letters = []
    guesses = 6

    while guesses > 0:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print(display)

        if "_" not in display:
            print("You guessed the word! You Win!")
            break

        guess = input("Type your guess and ENTER!\n")
        guessed_letters.append(guess)

        if guess in word:
            print(f"Correct! You have {guesses} guesses left!")
        else:
            guesses -= 1
            print(f"Incorrect! You have {guesses} guesses left!")

    if guesses == 0:
        print(f"Game Over! The word was: {word}")
