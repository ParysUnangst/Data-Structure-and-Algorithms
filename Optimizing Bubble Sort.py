# Basic Bubble Sort Implementation
def bubble_sort(arr):
    '''
    Sorts an array using the basic bubble sort algorithm.

    Parameters:
    arr (list): The list to be sorted

    Returns:
    None. The array is sorted in place
    '''

    n = len(arr)
    #iterate through each element in the array
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Optimized Bubble Sort Implementation
def optimized_bubble_sort(arr):
    '''
    Sorts an array using optimized bubble sort algorithm with early termination

    Parameters:
    arr (list): The list to be sorted

    Returns:
    None. The array is sorted in place
    '''
    n = len(arr)
    swapped = True
    #Continue iterating until no swaps are made in a pass
    while swapped:
        swapped = False
        #Iterate through the array
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True

        #reduce the length of the array 
        n -= 1

# Test Cases
test_cases = [
    [5, 3, 8, 1, 9, 2],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [5, 5, 5, 5, 5],
    [],
    [1],
]

for i, test_case in enumerate(test_cases):
    print(f"Test Case {i+1}: {test_case}")
    # Test Basic Bubble Sort
    arr_copy = test_case.copy()
    bubble_sort(arr_copy)
    print("Basic Bubble Sort Result:", arr_copy)
    
    # Test Optimized Bubble Sort
    arr_copy = test_case.copy()
    optimized_bubble_sort(arr_copy)
    print("Optimized Bubble Sort Result:", arr_copy)
    print()

