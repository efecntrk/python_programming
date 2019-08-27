'''

Read a sentece
Print each word and frequency
'''

#use a dictionary
'''
'This is a sentece that has many words it is a good sentece'
{
    'This': 1,
    'is': 2,
    'a': 2,
    'setence': 2,
    'that': 1,
    'has': 1,
    'many': 1,
    'words': 1,
    'it': 1,
    'good': 1,

}
'''
#create dictionary

frequency = {}

#read in a sentence 
sentence = input('Enter a sentece: ')

#break sentence into words (tokenize)

words = sentence.split(' ')

#loop over our words

for word in words:
    #check if in dictionary
    if word in frequency:
        frequency[word] += 1   
    else:
        frequency[word] = 1

print(frequency)
