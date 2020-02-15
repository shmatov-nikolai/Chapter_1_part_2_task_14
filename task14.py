'''
Given a list of numbers, find and print all elements that are an even number. In
this case use a for-loop that iterates over the list, and not over its indices! That
is, don't use range
'''

def even_num_in_list(some_list):
    even_num = []
    for number in some_list:
        if number % 2 == 0:
            even_num.append(number)
    print(even_num)

number_list = [1, 4, 2, 5, 7, 8, 9, 1, 3, 6, 7, 10] 

even_num_in_list(number_list)
