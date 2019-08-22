from random import randint

class Die():    
    """Simulates a die"""
    
    def __init__(self):
        """Initialises self and sets sides to 6 as a default."""
        self.sides = 6
        
    def roll_die(self):
        """Simulates rolling a die."""
        x = randint(1, self.sides)
        print("You rolled a " + str(self.sides) +
              "-sided die and got a " + str(x) + "!")
        
    def fell(self):
        """Simulates the die falling off the table and re-rolling."""
        y = randint(1, self.sides)
        print("The die fell off the table!")
        print("You re-rolled the " + str(self.sides) + 
              "-sided die and got a " + str(y) + "!")
        

# initialises flag to exit program and the die to use
active = True
my_die = Die()

# stores user responses for yes and no
yeses = ["yes", "y", "go on then", "sure"]
nos = ["no", "n"]

# lets the user know how to use the program       
print("Welcome to my dice rolling game!")
print("If you would like to use a different sided die, type 's'." +
      "If you would like to stop, press 'q'.")

while active:
    
    # asks the user how many times to roll the die
    times = input("How many times would you like to roll the die? ")
    
    # if the user decides to change the number of sides on the die, checks
    # input for special use cases, then makes sure that input is a number that
    # makes logical sense. If the number is valid, updates the sides of the die.
    if times == 's':
        sides = ""
        while True:
            sides = input("How many sides would you like the die to have? ")
            if sides == 'q':
                active = False
                break
            elif sides == 's':
                print("You are already choosing how many sides to have!")
                continue
            elif sides.isdigit() == False:
                print("Please enter positive numbers!")
                continue
            elif int(sides) < 2:
                print("It's not possible to make a die with that number!")
                continue
            elif int(sides) == 2:
                print("I think you might be looking for a coin flip!")
                continue
            sides = int(sides)
            break
        my_die.sides = sides
        continue
    # exits the program
    elif times == 'q':
        break
    # if the number is not a number, state that only numbers should be given
    # and restart the loop
    elif times.isdigit() == False:
        print("Please enter positive numbers!")
        continue
    
    # if the user chose to quit during the previous loop, continue exiting    
    if active == False:
        break    
    
        # after checks are finished, convert times to an integer
    times = int(times)
    
    # roll the die, but it might fall off the table!
    for i in range(times):
        fell = randint(0, 199)
        if fell == 27:
            my_die.fell()
        else:
            my_die.roll_die()
        
    # asks user if they want to restart the program and quits if they don't
    while True:
        again = input("Would you like to roll again? ")
    
        if yeses.count(again.lower()) > 0:
            break
        elif nos.count(again.lower()) > 0 or again == 'q':
            active = False
            break

# exit message    
print("Thank you for playing!")
