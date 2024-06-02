def selection_sort(arr):
    """
    Implementation of Selection Sort algorithm.
    
    Parameters:
    arr (list of int): The list of integers to be sorted in ascending order.
    
    Returns:
    list of int: The sorted list of integers.
    """
    n = len(arr)
    
    # all elements of the array
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Test cases
def test_selection_sort():
    test_cases = [
        [5, 3, 8, 2, 7, 4, 1, 9, 6],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],   
        [9, 8, 7, 6, 5, 4, 3, 2, 1],   
        [4, 4, 4, 4, 4, 4, 4, 4, 4],
        [],                            
        [42],                       
    ]
    
    for i, arr in enumerate(test_cases):
        sorted_arr = selection_sort(arr)
        print(f"Test case {i+1}: {sorted_arr}")

test_selection_sort()
