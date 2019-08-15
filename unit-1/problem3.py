
'''
word = (input('Enter a word or sentence please') [::-1])

print(word)

'''

my_string = 'This is a sentence'


reversed_string = ''

#loop from last to first character

for i in range(len(my_string) -1, -1, -1):
    reversed_string += my_string[i]

print(reversed_string)


