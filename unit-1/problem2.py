'''
num = 7

num_list = [1,3,5,7,9,11]

my_new_list = [i * 7 for i in num_list]

print(my_new_list)

'''

#go thru each element and multiply by num

num_list = [2, 4, 6, 8, 10]
num = 5

'''
for x in num_list:
    print(x * num)

'''

for idx in range(len(num_list)):
    num_list[idx] *= num
print(num_list)