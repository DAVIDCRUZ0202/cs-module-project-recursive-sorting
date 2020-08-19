# Things for A Recursive Function:

### Need a Base Case
### Need a function that calls itself
### Need a way to progress toward base case

# Recursive functions are often elegant, terse, with few lines of code

# Divide and conquer:
## can divide one large problem into sub-problems
## the sub-problems habe the same "shape" as the large problem
## if you can solve sub-problems
## combine the sub-problem solutions and the large problem is solved

# Example

## Finding the most efficient route to deliver all mail at once
## divide the mailing region into subregions
## find efficient routes for each subregion 
## all subregions delivered means all regions are delivered!


# Sorting
## Break up the array
## sort each piece
## put them back together


## Quicksort


# Choose Pivot: Median, first, or last number in an array
array = [5, 7, 3, 1, 2, 9, 0, 8, 4, 6]
# base case is empty array


def partition(arr):

    pivot = arr[0]
    left = []
    right = []

    for num in arr:
        if num < pivot:
            left.append(num)
        if num > pivot:
            right.append(num)
    return left, pivot, right
# choose pivot
# partition around the pivot left and right 


## recurse on left and right partitions
def quicksort(arr):
    if len(arr) == 0:
        return arr

    left, pivot, right = partition(arr)

    return quicksort(left) + [pivot] + quicksort(right)    


# Mergesort walkthrough
## For merge sort, the sorting takes place on the returns not on the pivots
## halve each group until we only have arrays of length 1
## combine the sub arrays and return sorted combinations
## compare the first elements of each combined sort, and send up the lowest values first
## this creates sorted arrays
## Merge sorting compares first elements every time