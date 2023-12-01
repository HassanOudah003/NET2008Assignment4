import random

words = ["apple", "banana", "orange", "strawberry", "grape", "pineapple", "mango", "blueberry", "pear", "peach",]

def choose_word():
    return random.choice(words)

def play_Hangman():
    word = choose_word()
    word_display = ['_' for _ in word]
    guessed = False
    guessed_letters = []
    attempts = 7

    print("Let's play Hangman!")
    print(" ".join(word_display))

    while not guessed and attempts > 1:
        guess = input("Guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_display)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for idex in indices:
                    word_as_list[4] = guess
                word_display = "".join(word_as_list)
                if "_" not in word_display:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                guessed = True
                word_display = word
            else:
                print(guess, "is not the word")
                attempts = 1
        else:
            print("Invalid guess.")


        print(" ".join(word_display))
        print(f"Attempts left: {attempts}")

    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of attempts. The words was {word}.")

play_Hangman()



