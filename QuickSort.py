"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, low, high):
    if low >= high:
        return array
    
    pivot_position = low
    current = low
    pivot = array[high]
    
    while current < high :
        if array[current] < pivot:
            temp = array[current]
            array[current] = array[pivot_position]
            array[pivot_position] = temp
            pivot_position += 1
            current += 1
        else:
            current += 1

    array[high]  = array[pivot_position]
    array[pivot_position] = pivot
    quicksort(array, low, pivot_position - 1)
    quicksort(array, pivot_position + 1, high)

    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test, 0 , len(test)-1)
