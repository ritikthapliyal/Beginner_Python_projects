import random

difficulty = input("Enter 'hard' for Hard-Mode and 'easy' for Easy-Mode:  ")
difficulty = difficulty.lower()

if difficulty == "hard":
    times = 5
else:
    times = 10

print(f"You have {times} lifes/guesses")

selected_number = random.randint(1,100)
end_of_game = False
won = False

while not end_of_game:
    times -= 1
    guess = int(input("Guess the number: "))

    if guess > selected_number:
        print("Too High")
    elif guess < selected_number:
        print("Too Low")

    if guess == selected_number or times == 0:
        end_of_game = True
        if guess == selected_number:
            won = True

if won:
    print("You Won")
else:
    print(f"You Lost. NUMBER was {selected_number}")