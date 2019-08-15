def item_count(a_list, key):
    count = 0
    for item in a_list:
        if item == key:
            count += 1

    return count

print(item_count([1, 2, 3, 4], 3))




    



#item_count([1, 2, 3, 4, 5], -2) -2