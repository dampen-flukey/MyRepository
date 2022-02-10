import random
##


def numberGuess(number):

    guess = 0
    input1 = None
    while(input1 != number):
        input1 = int(input("Enter your guess : \n"))
        guess += 1
        if input1 == number:
            print(f"Bravo!!! You guessed the right num in {guess} guesses!")
        elif input1 > number:
            print("Oops! Wrong Choice. Enter a smaller number..")
        else:
            print("Oops! Wrong Choice. Enter a larger number..")


number = random.randint(1, 100)
print(number)
numberGuess(number)
