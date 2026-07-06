def insertion_sort_desc(arr):
    # Sorting an array in descending order using insertion sort
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shifting elements that are smaller than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


# Quick test
numbers = [12, 5, 8, 19, 3, 15, 7]
print("Original:", numbers)

insertion_sort_desc(numbers)
print("Sorted (Desc):", numbers)