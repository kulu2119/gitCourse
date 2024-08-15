from random import Random
n = 0
x=Random()
number = (x.randrange(1,100))
print(" Welcoime to the number guessing game. \n I have selected the number between 1 and 100. \n You have 10 attempts to guess the number. ")
while n<10:
    n += 1
    
    choice = int(input("enter your guess"))
    if choice == number :
        print("congratulations! You have guessed the number in {} attempts ".format(n))
        break
    else:
        if choice < number:
            print("Too low! Try again!")
        else:
            
            print("Too High! Try again!")

else:
    print(f"Sorry, you've used all {n} attempts. The correct number was {number}.")
