'''
def sum_everything(*args):
    total = 0
    for x in args:
        total += x
    return total
print(sum_everything(4,5,6))
'''
'''
def triple_divide(x,y,z):
    print(x / y / z)
triple_divide(z=1, y=2, x=10)

'''

def yogurt_land(spoon, **kwargs):
    print(spoon)
    # We need a loop, because we don't know how many kwargs there are.
    for keyword, flavor in kwargs.items():
      # kwargs.items has the keyword and the value, which we're calling "flavor" in the loop.
      print("My", keyword, "is a", flavor)
  
  # Like before, the unnamed arg has to come first!
print(yogurt_land("large!", first_froyo="vanilla", second_froyo="chocolate", third_froyo="banana"))

