# Function to sort an array in descending order
def sort_array_desc(arr):
    return sorted(arr, reverse=True)

# Example array
numbers = [5, 2, 9, 1, 5, 6]

# Sorting the array in descending order
sorted_numbers_desc = sort_array_desc(numbers)

# Output the sorted array
print("Sorted array in descending order:", sorted_numbers_desc)
