def happy_birthday():
    return('Happy Birthday!')
happy_birthday()

def happy_birthday(age, name):
    return(f'Happy Birthday {name} and congratulations on turning {age} years old!')
happy_birthday(22, "Nora")


import random
def get_lucky_number():
    
    lucky_num = random.randint(1,100)
    return(lucky_num)
lucky_number = get_lucky_number()
    
print("Your lucky number is:", lucky_number)


# aula 4 modulo 3 função e modulos 
def calc_sale_price(amount, member):
	if member:
		# Members receive a 15% discount (0.15)
		amount = amount - (amount * 0.15)
	else:
		# Non-members get a 5% discount (0.05)
		amount = amount - (amount * 0.05)

	amount = round(amount, 2)
	return amount
	

# Example price (already provided)
full_price = 150.50

# Call function for members
member_price = calc_sale_price(full_price, True)
print("Member price:",member_price)

# Call function for non-members
non_member_price = calc_sale_price(full_price, False)
print("Non-member price:",non_member_price)

#
shirt_color = "Pink"
def display_color_works(shirt_color):
  
  print("First shirt color is:", shirt_color)
  
def display_color_failure(shirt_color):
  # Try to access 'color' directly (this will cause an error)
  print("Your shirt color is:", shirt_color)


# The shirt_color variable is in scope in this function
display_color_works(shirt_color)

# The shirt_color variable is not in scope in this function
display_color_failure(shirt_color)
    