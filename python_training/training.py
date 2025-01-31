

arr = [1, 5, 3, 7, 9]
arr.sort()
print(arr)

def binary_search(arr, target):
    # returns the index of the target with O(nlogn)

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2 # imagine my array is of size 5 // 2 -> gives 2, which is the index of the middle element

        if arr[mid] == target:
            return mid

        if arr[mid] < target: #[1, 2, 3, 4, 5] target = 4 

            left = mid + 1
        elif arr[mid] > target:

            right = mid - 1

    return None


def test_bs(arr, target, index):

    result = binary_search(arr, target)

    assert result == index
    print("Assertion cleared!")


test_bs([1, 2, 3], 3, 2)
test_bs([], 3, None)
test_bs([1, 2, 3, 4, 5, 6, 7, 1000], 1000, 7)
test_bs([1, 2, 3, 99], 2, 1)
test_bs([0, 1, 2, 3], 0, 0)
