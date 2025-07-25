
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Test cases
print(selection_sort([64, 25, 12, 22, 11]))  # Expected: [11, 12, 22, 25, 64]
print(selection_sort([5, 2, 9, 1, 5, 6]))    # Expected: [1, 2, 5, 5, 6, 9]
print(selection_sort([3, 0, 2, 5, -1, 4, 1])) # Expected: [-1, 0, 1, 2, 3, 4, 5]
