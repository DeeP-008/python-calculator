"""Creating a calculator application!

Start date: July 31, 2023 6:01 PM
Author: Dhyeya Padhya"""

inputs = [] #user Input
def get_User_Input():
    """Take in User Input.
    
    This function will take input from users in the form of numbers and a single string 'Done', which is when it will end.
    The inputs will be saved in a list in float form and throw an exception when anything other than the allowed inputs is 
    entered by the user. In case an exception is thrown, it  will then allow the user another opportunity to enter a number!
    Input - None
    Output - inputs: a list of inputs."""
    user_Exit = False   # will be true once the user enters 'done'
    
    while not user_Exit:
        user_Input = input("Enter a number if you wish or enter 'Done' to finish:")
        if user_Input.lower() == "done":
            user_Exit = True #will become true and the loop would terminate since not True = False
            break
        else:
            try:
                inputs.append(float(user_Input))
                print(inputs)
            except ValueError:
                print("Invalid Input! Please enter a number or 'Done'!")
                continue #allows user another chance
    return inputs

#Main method to test all methods
def main():
    get_User_Input()    #Run the main method and input numbers
    print(get_User_Input())
    inputs.clear()  #empties the inputs list
    

if __name__ == "__main__":
    main()
