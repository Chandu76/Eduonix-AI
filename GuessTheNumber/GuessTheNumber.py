import random
try:
    n = int(input("How many times would you like to play?"))
    #Limit of number of guesses isn't specified in the question.
    secret_number =  random.randint(1,25)
    guesses = 0           #No. of guesses
    numbers_guessed = []  #List of numbers users guessed
    for i in range(0,n):
        try:
            guesses += 1
            guess = int(input("Select a random number between 1-25"))
            if(guess > secret_number):
                print("Higher")
            elif(guess < secret_number):
                print("Lower")
            else:
                print("Congo! You guessed the number in ",guesses," guesses.\nNumbers you guessed are: ",numbers_guessed)
                break
            numbers_guessed.append(guess)
        except:
            print("Invalid value. But still counts as a guess :) :p")
            continue
    if(guesses == n):
        print("Oops! You didn't guess the number in specified number of tries.")
        print("Numbers you guessed: ",numbers_guessed)
except:
    print("Invalid input. Please specify an Integer number.")
