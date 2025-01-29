array = [1, 5, 2, 4, 6, 3, 7, 8, 43, 5, 1, 3]

def find_k_largest(array, k):

    array.sort()
    array = list(set(array))

    if k > len(array):
        return None
    print(array[k-1])
    return array[k-1]
        
def find_k_largest_optimized(array, k):
    # Using heap (priority queue)
    import heapq
    
    # Keep k largest elements
    return heapq.nlargest(k, set(array))[-1]


find_k_largest(array, 85)