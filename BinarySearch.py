"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    final_array = input_array
    while len(input_array) >= 1:
        
	    size_of_list = len(input_array)
	    
	    if (size_of_list % 2) != 0:
	    	middle_element = input_array[size_of_list/2]
	    else:
	    	middle_element = input_array[(size_of_list/2)-1]
	    
	    if value == middle_element:
	    	return final_array.index(middle_element)
	    elif value < middle_element:
	    	input_array = input_array[:(input_array.index(middle_element))]
	    elif value > middle_element:
	       input_array = input_array[(input_array.index(middle_element)+1):]

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 28
test_val2 = 11
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)

