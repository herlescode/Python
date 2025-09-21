valid_input = False
while not valid_input:
    user_input = int(input("Please enter a number greater than 0:"))
    if user_input > 0:
        valid_input = True
    else:
        print ("invalid input please try again")