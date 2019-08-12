'''
def print_order(product):
    print('Thank you for order ' + product, '!' )
    print('There will be $5.00 delivery charge')

print_order()
print_order('Shell Mirror')
print_order('Modern Shag Rug')
'''
'''
def latte_totl ():
    price = 5.50
    sales_tax = .10
    total_amt = price + (price * sales_tax)
    print('The total is ', total_amt)


latte_totl()

'''

'''
def greet_user():
    
    print('Hello!')
greet_user()
'''
'''
def calculate_total(price):
    sales_tax_rate = .10
    total_amount = price + (price * sales_tax_rate)
    print('The total is $', total_amount)

calculate_total(5.5)
calculate_total(4.75)
'''
'''
def calculate_total(price, taxes):
    total_amount = price + (price * taxes)
    print('Total is $ ', total_amount)

calculate_total(5.5, .10)
calculate_total(4.75, .12)

'''
'''
def greet_user(firstName, lastName, year, city):
    print('Hello', firstName, lastName, year, city, '!')

greet_user('Bruce', 'Wayne', 1939,'Gotham')
greet_user('Wayne', 'Bruce', 'Gotham',1939)

'''
'''
def free_shipping(product, order_amount):
    print('Thank you for ordering', product)
    if order_amount >= 35:
        print('It is your luck day, there is no shipping charge for order over 35')
    else:
        print('There will be $5.00 shipping charge')

free_shipping('mirror', 32)
'''
'''
def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

'''
'''
def add_two(number):
    total = number + 3
    print(total)
    return total
add_two(5)

new_number = add_two(5)
print(new_number)

'''
'''
def calculate_total(price, taxes):
  total_amount = price + (price * taxes)
  print('The total is $', total_amount)
  # Send the total_amount for the drink back to the main program.
  return total_amount

# This just calls the function -  we've seen this.
#calculate_total(5.5, .10)

# This is new! Save the amount of this drink into a variable "latte_total."
latte_total = calculate_total(5.5, .10)

# Now, we can  use that variable.
print('Your order total is', latte_total)

'''
'''
def add_bonus_points (score):
    if score > 50:
        return score + 10
    score += 20
    return score
total_points = add_bonus_points(45)
print(total_points)

'''

'''

def add_two(number):
    total = number + 3
    print(total)
    return total
new_total = add_two(5)
print('New total', new_total)

'''
'''
def rock_and_roll(muted):
   song = "It's only Rock 'N' Roll"
   artist = "Rolling Stones"

   if (muted == True):
       return
       # Here, we use return as a way to exit a function
       # We don't actually return any value.
   print("Now playing: ", song, " by ", artist)

rock_and_roll(True)
'''
'''
def categorize(x):
  if (x < 8):
      return 8
  x += 3
  if (x < 15):
      return x
  return 100

'''
'''
def add_two(number):
    total = number + 3
    print(total)
    return total

final_var = add_two(3)
print(final_var)

'''
'''
def copy_list(my_original_list):
    original_list = [1,2,3,4,5,6]
    for my_new_list in original_list:
        print(my_new_list)
'''
'''
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))
'''
'''
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply((8,2,3,-1,7)))

'''

def get_energy(mass, c=3*10**8):
    return mass * c**2
    
  bomb_energy = get_energy(bomb_mass)
  
  print('A 1KG bomb supplies ' + str(bomb_energy) + ' Joules')
  


    
    
    
    
    



