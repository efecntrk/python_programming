'''
def areBotheven(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return True
    else:
        return False
print(areBotheven(2,3))
'''
'''
def lightordark(hour):
    if hour > 24:
        print('That is not an hour in the day')
        return hour #????? 
       
    if hour < 7 or hour > 17:
        print('It is dark outside')
    else:
        print('It is light outside')
    
print(lightordark(4))
    
'''
'''
def multiply (x,y):
    print(x*y)
multiply(1,2)

'''

def multiply(*args):
    product = 1
    for num in args:
        product *= num
    print(product)
print()

multiply(4,5,6)
