
array = [1, 2, 5, 8, 6, 3, 6, 7, 9, 10, 13, 14, 15, 16]
array = list(set(array))
array.sort()
print(array)

# Things to note here: the function assumes a sorted array. It returns the value which was looked for, not the index.
# What about edge cases, the array is empty? Loop immediatly exits and returns None. Good.
# What about the number not appearing in the array? at some point the lower will be > than upper, exiting the loop and returning None
# What about lower + upper overflow?

def binary_search(array, target):

    lower_pointer = 0
    upper_pointer = len(array) - 1

    while upper_pointer >= lower_pointer:

       # mid = (lower_pointer + upper_pointer) // 2 # this can be rewritten as x + y // 2 = x + (y -x) // 2
        mid = lower_pointer + ((upper_pointer - lower_pointer) // 2)

        if array[mid] == target:
            return mid

        if array[mid] > target:

            upper_pointer = mid - 1

        elif array[mid] < target:

            lower_pointer = mid + 1

    return None


number = binary_search(array, 7)
print(number)
