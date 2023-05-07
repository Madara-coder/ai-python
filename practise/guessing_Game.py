guess_number = 5
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess the number:-\t"))
    guess_count += 1
    if guess == guess_number:
        print("Hurray! You have won :)")
        break
else:
    print("Sorry! You lost :(")
