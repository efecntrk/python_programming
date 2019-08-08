'''
num = 4

if num > 5:  
    print ('too high')
elif num < 3:    
    print('too low')
else:
    print('just right')

#print corresponding letters for grades
'''
#80 - 100, print 'a'
#79 - 60, print 'b'
#50 - 59, print 'c'
#0 - 49, print 'f'

'''
grade = 82

if grade <= 49:
    print('F')
elif grade >= 50:
    print('C')
elif grade >= 60:
    print('B')
else:
    print('A')
'''
'''
grade = 78
if grade >= 80:
    print('A')
elif grade >= 60:
    print('B')
elif grade >=50:
    print('C')
else:
    print('F')

'''
'''
grade = 55

if grade < 50:
    print('F')
elif grade < 60:
    print('C')
elif grade < 80:
    print('B')
else:
    print('A')

'''

#fizzbuzz

#for the first 50 integers
#if its a multiple of 3, print 'fizz'
#if its a multiple of 5, print 'buzz'
#if its a multiple of 15, print 'fizzbuzz'
#otherwise, just print the number
'''
for num in range(1, 51):    

    if num % 15 == 0:    
        print('Fizzbuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

'''
'''
name = 'Fizzbuzz'

if len(name) > 4: 
    print('Longer than 4')
if len(name) > 6:
    print('Longer than 6')
'''

#using 'and' and 'or' in conditionals


num = 14

#display a message if the number is odd and also less than 20

'''
if num % 2 == 1 and num < 20:
    print('odd number less than 20')
else:
    print('something else')

'''
'''
n = 55

if n % 2 == 1:
    print('Weird')
elif n % 2 == 0 and n >= 2 and n <= 5:
    print('Not Weird')
elif n % 2 == 0 and n >= 6 and n <= 20:
    print('Weird')
elif n % 2 == 0 and n >= 20:
    print('Not weird')
'''

#group print statements together
n = 6
if n % 2 == 1 or (n % 2 == 0 and n >= 6 and n <= 20):
    print('Weird')
if (num % 2 == 0 and (n >= 2 and n <= 5)) or (n % 2 == 0 and n > 20):
    print('Not Weird')