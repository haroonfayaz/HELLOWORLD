

secret_number = 13
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("guess:"))
    guess_count += 1
    if guess == secret_number:
        print(f"{guess} was the secret number")
        break
else:
    print("sorry ,you didn't made the right guess")





