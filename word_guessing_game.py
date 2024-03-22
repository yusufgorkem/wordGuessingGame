import random

countries = ["UNITED STATES", "CHINA", "RUSSIA", "GERMANY", "UNITED KINGDOM", "SOUTH KOREA", "FRANCE", "JAPAN",
             "SAUDI ARABIA", "UNITED ARAB EMIRATES", "ISRAEL", "INDIA", "CANADA", "UKRAINE"]
animals = ["DOG", "CAT", "HORSE", "CHICKEN", "FISH", "BEAR", "BIRD", "SHARK", "SNAKE", "PIG", "LION", "TURKEY",
           "GRAY WOLF", "SPIDER"]
things_you_take_on_holiday = ["PASSPORT", "VISA", "PHONE", "CHARGER", "PLUG ADAPTOR", "PURSE", "MONEY", "KEYS",
                              "LAPTOP", "TABLET", "CAMERA", "PEN", "NOTEBOOK", "BOOK"]

words = countries + animals + things_you_take_on_holiday

while True:
    random_word = random.choice(words)
    print("WORD GUESSING GAME")
    if random_word in countries:
        print("Hint: It is a country")
    elif random_word in animals:
        print("Hint: It is an animal")
    else:
        print("Hint: It is a thing you take on holiday")

    user_guesses = ""
    chances = 5
    while chances > 0:
        wrong_guess = 0
        for ch in random_word:
            if ch in user_guesses:
                print(ch, end=" ")
            else:
                if ch == " ":
                    print(" ", end="")
                else:
                    wrong_guess += 1
                    print("_", end=" ")
        if wrong_guess == 0:
            print("\nYou won! The word is {}".format(random_word))
            again = input("Do you want to play again? (Y/N): ")
            if again.upper() == "Y":
                break
            else:
                quit()

        while True:
            guess = input("\nMake a guess: ").upper()
            if guess.isalpha() and len(guess) == 1:
                user_guesses += guess
                break
            else:
                print("Please enter a valid guess!")

        if guess not in random_word:
            chances -= 1
            print("Wrong! You have {} chance left".format(chances))
            if chances == 0:
                print("\nGame over! The word is {}".format(random_word))
                again = input("Do you want to play again? (Y/N): ")
                if again.upper() == "Y":
                    break
                else:
                    quit()
