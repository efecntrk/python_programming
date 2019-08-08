'''
visible_colors = ["red", "orange", "yellow", "green", "blue", "violet"]

for each_color in visible_colors:
  print(each_color)
  '''
'''
magicians = ['alica', 'david', 'caroline']
for magician in magicians:
    print(magician.title() + ' that was a great trick!')
    '''
'''
magicians = ['alica', 'david', 'caroline']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    '''
'''
for name in ['Tom', 'Deborah', 'Murray', 'Axel']:
    print('Now appering in the Refreshment Room...')
    print(name)
    print('applause')
    '''
'''
my_string = 'Hello World'

for caharacter in my_string:
    print(caharacter)
'''
'''
guest_list = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']
for guest in guest_list:
    print('Hello ' , guest , '!' )
    '''
'''
square = []

for num in range(5):
    sqr = num ** 2
    square.append(sqr)
print(square)

'''
'''
even_numbers = list(range(2,11,2))
print(even_numbers)
'''

'''
squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)
print(squares)
'''
'''
squares = []
for value in range (1,11):
    squares.append(value**2)
print(squares)
'''
'''
a = 0
while a < 10:
    print (a)
    a += 1
'''
'''
glass = 0
glass_capacity = 12

while glass < glass_capacity:
  glass += 1
'''
'''
answer = 4
guess = input ('Guess what number I am thinking of (1-10): ')
while guess != answer:
  guess = input ('Nope, try again: ')
print('You got it')

'''
'''
names = ['Efe', 'Sami', 'Evan', 'Peter', 'Eric', 'Kerem']
for each_name in range(len(names)):
  print(names[each_name])

'''
'''
my_string = 'Hello World!'

for character in my_string:
  print(character)
'''
'''
names = ['Efe', 'Sami', 'Evan', 'Peter']
for each_name in range (4):
  print(names[each_name])

'''
'''
guest_name = ['Efe', 'Sami', 'Evan', 'Peter']

for guest in range(len(guest_name)):
  guest_name[guest]  = 'A new name'
  print(guest_name)
'''
'''
glass = 0
glass_capacity = 12

while glass < glass_capacity:
  glass += 1
  print (glass)
'''
'''
answer = 4
guess = input ('Guess what number I am thinking of (1-10): ')
while guess != answer:
  guess = input ('Nope, try again: ')
print('You got it')
'''
'''
answer = "4"
guess = input("Guess what number I'm thinking of (1-10): ")
while guess != answer:
  guess = input("Nope, try again: ")
print("You got it!")

'''

'''
while True:

  if my_condition == 1:
      # my condition is met! No need to continue on
      break
  else my_condition == 0:
      my_condition = 1

  # note that this is within the scope of the while loop
  print('This doesn\'t get run if the break is triggered!')

'''
'''
height = input('How tall are you, in inches?')
height = int(height)

if height >= 36:
  print('You are tall enough to ride! ')
else:
  print('You will be able to ride when you are a little older.')
'''
'''
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
  city = input(prompt)

  if city == 'quit':
    break
  else:
    print('I would like to go to ' + city.title() + '!')
    
'''
'''
current_number = 0
while current_number < 10:
  current_number += 1
  if current_number % 2 == 0:
    continue
  print(current_number)
'''
'''
number = 0
for number in range(5):
    number = number + 1
    if number == 3:
       pass
       print('My number is currently 3')
    print(f'Number is {str(number)}')
print('Out of loop')

'''

def my_empty_function():
      raise NotImplementedError