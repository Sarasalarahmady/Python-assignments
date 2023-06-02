import random

number_of_guesses = 0
number =  random.randint(1,20)

name = input("hi! what's your name? ")
print("ok " + name + " , i chose a number between 1 and 20 , can you guess it?\n")

while True:
    guess = int(input("guess a number : "))
    number_of_guesses += 1
    if guess == number:
        print("wow! you gussed it right :)")
        print("you tried" , number_of_guesses , "times")
        break
    else:
        if guess < number:
            print("the number you guessed is less than the number I chose\n")
        else:
            print("the number you guessed is more than the number I chose\n")
        continue