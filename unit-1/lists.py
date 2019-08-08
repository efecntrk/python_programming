'''
efe = ['Holy', 'Juan', 'Ming']

print(efe[2])
'''

'''
'efe = [2, 4, 6, 8]
print(efe[0])
'''

'''
my_class = ['Efe', 'Sami', 'Peter', 'Kerem', 'Rocky', 'Eric', 'Evan']
num_students = len(my_class)
print('There are', num_students, 'students in the class')
'''
'''
my_class = ['Efe', 'Sami', 'Peter', 'Kerem', 'Rocky', 'Eric', 'Evan']
my_class.append('Sony')
print(my_class)
'''
'''
my_class = ['Efe', 'Sami', 'Peter', 'Kerem', 'Rocky', 'Eric', 'Evan']
my_class.insert(1, 'Can')
print(my_class)
'''

'''
my_class = ['Efe', 'Sami', 'Peter', 'Kerem', 'Rocky', 'Eric', 'Evan']
student_that_left = my_class.pop()
print('Student', student_that_left, 'has left the class.')
print(my_class)

'''
'''
classmates = ['Connor', 'Efe', 'Alexandar', 'Bianca', 'Edwin', 'Greg']

#print a list
#print(classmates)

#number of items in a list - use the function len

#print(len(classmates))

#get a specific item - the first

#print(classmates[0])

#print the last element

#print(classmates[len(classmates) -1])

# shortcut for last element

#print(classmates[-1])

#slicing - taking sections of the list
#print(classmates[0:3])

#adding an element to the end of a list

#classmates.append('Princeton')

#print(classmates)

#remove from end of the list

#classmates.pop()
#print(classmates)

#inserting at a specific position
classmates.insert(0, 'Princeton')

print(classmates)

#remove an element
classmates.remove('Princeton')
print(classmates)

#calculate the sum of a list of numbers
'''
#ages = [10,20,30,45,55,65,75,85,95,105]


#print (sum(ages))

#use a for loop
#total_ages = 0 

'''
for age in ages:
    total_ages += age #total_ages = total_ages + age 
print(total_ages)
'''
#another for loop - use range and idexes
'''
for idx in range(len(ages)):
    total_ages += ages[idx]
print(total_ages)
'''

#calculate the sum of all the odd number ages in the list

ages = [10,20,30,45,55,65,75,85,95,105]
total_ages = 0
for age in ages:
    if age % 2 == 1:
        total_ages += age
print(total_ages)


