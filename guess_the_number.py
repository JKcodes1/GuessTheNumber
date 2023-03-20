# Imports random module
import random

# Creates list of numbers from 1 to 100
list_of_numbers = list(range(1,101))

# While loop with menu options selection
# Allows to select Start or Exit
while True:
    menu = input("""\nType:
     START to start the game
     EXIT to exit the game.
     Good luck! \n""")
    
    # If user decides to start this will generate number first
    # then set bottom range to 0, top to 100 and attempts number to 0
    if menu == "START":
        generated_number = random.choice(list_of_numbers)
        #print(generated_number)
        bottom_range = 0 
        top_range = 100
        attempts = 0

        # Internal while loop to run number checks and comparisons
        while True:
            try:
                # Asks user for a number, errors if the value isn't number
                guessed_number = int(input("\nWhat is your guess? \n")) 

                # This checks if number is the list of numbers
                # Adds number of attempts, checks if it matches generated number
                if guessed_number in list_of_numbers:
                    attempts += 1
                    if guessed_number == generated_number:
                        print(f"How amazing, you have guessed the number on {attempts} attempts! It is {guessed_number} indeed. ")
                        break
                        
                    # If number greater than generated number
                    # Checks the number of attemps, recalculates top range
                    # Prints appropriate message and range if any attempts left
                    elif guessed_number > generated_number:
                        
                        if attempts < 6:         
                            if guessed_number < top_range:
                                top_range = guessed_number
                                                            
                            print("Ah, that number is higher than the one you're looking for. Try again!")
                            print(f"Your guessing range is {bottom_range} to {top_range}")
                            print(f"Number of attempts: {attempts}")
                            
                        elif attempts == 6:
                            print("That number is higher than the one you're looking for. "
                                  "You've used all attempts and lost the game!")
                            print(f"The number you were looking for is {generated_number}")
                            break
                            
                    # If number lower than generated number
                    # Checks the number of attemps, recalculates bottom range
                    # Prints appropriate message and range if any attempts left    
                    elif guessed_number < generated_number:
                        
                        if attempts < 6:
                            if guessed_number > bottom_range:
                                bottom_range = guessed_number
                            
                            print("Ah, that number is lower than the one you're looking for. Try again!")
                            print(f"Your guessing range is {bottom_range} to {top_range}")
                            print(f"Number of attempts: {attempts}")
                            
                        elif attempts == 6:
                            print("That number is lower than the one you're looking for. "
                                  "You've used all attempts and lost the game!")
                            print(f"The number you were looking for is {generated_number}")
                            break
                
                # Error message when number outside of range
                else:
                    print("This number is outside of the range of 1 to 100. Try again!")
                   
            # Error message if user doesn't enter whole number                
            except ValueError:
                print("Please enter a whole number.")     
    
    # Exit program function
    elif menu == "EXIT":
        exit()
    
    # Error when incorrect option selected from menu
    else:
        print("Please choose a valid option")       
                    
  
# by JKCodes1

