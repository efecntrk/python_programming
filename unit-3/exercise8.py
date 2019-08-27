'''
Create a list of destinations
Go through the list, add rank to each destination
'''
import random

cities = ['chicago', 'montreal', 'vancouver', 'calgary', 'new_york', 'toronto', 'miami', 'orlando', 
'antalya', 'istanbul']
new_rankin = []

for idx in range(len(cities)):
    rank = random.randint(1,10)
    cities[idx] += '-' + str(rank)
print(cities)





