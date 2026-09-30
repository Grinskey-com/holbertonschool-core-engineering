#!/usr/bin/env python3

my_list1 = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8]

def safe_print_list(my_list=[], x=0):
    count=0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            count += 1

        except IndexError:
            break
    print()
    return(count)

        

safe_print_list(my_list1)

safe_print_list(my_list2)


