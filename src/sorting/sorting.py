# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    return merged_arr
    
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # If the array is empty, return the emptiness
    if len(arr) == 0:
        return arr
    # if the array is longer than one, split it in half
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

# Recurse on left and right
        merge_sort(left)
        merge_sort(right)

        # one iterator will keep track of one half
        # since they are being set at the same time,
        # they will keep pairs of the same index value
        # once the whole array has been recursed through
        # these variables will be comparing single elements at a time
        # iterators for travelling through halves
        i = 0
        j = 0
        # This iterator is used throughout the whole function,
        # and traverses through the entire list instead of just 
        # going through one half
        # iterator for the main list
        k = 0

        # this while loop will continue as long as the iterators are 
        # working through the halves
        # because it is comparing the iterator counter
        # to the length of the half
        # we dont use equal to signs because that would make us
        # call something out of index of the halves
        while i < len(left) and j < len(right):
            # if the value on the left is smaller than the value on the right
            if left[i] < right[j]:
                # then we assign the slot in our array of [k]
                # with the value of left[i]
                # the value from the left half has been used
                arr[k] = left[i]
                # Move the iterator forward
                # so that the next iteration will check values of the next item
                i += 1

            # if the above statement doesn't work, then j is chosen
            # as the replacement for the location of k in our original array
            else:
                arr[k] = right[j]
                # we move the iterator forward again 
                j += 1
            # Move to the next slot
            # we also move the iterator for our list forward
            k += 1

        # For all the remaining values
        # the left side gets iterated first since it's lower
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        # the right side gets iterated through after since it holds 
        # higher values
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    # once all passes have been made, the returned array has been sorted
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

