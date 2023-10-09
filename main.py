import random
def guess(x):
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        guess = int(input("What number is the computer guessing? "))
        if guess > number:
            print("Oops! Too high. Try again!")
        elif guess < number:
            print("Oops! Too low. Try again!")
    print("Yay! You got it!!")

guess(20)



