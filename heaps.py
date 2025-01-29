array = [3, 4, 1, 3, 2, 6, 90, 0]


def find_k_smallest(array, k):

    import heapq
    max_heap = []

    for item in range(k):
        heapq.heappush(max_heap, -array[item])

    for item in range(k, len(array)):

        if -array[item] > max_heap[0]:

            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -array[item])

    
    max_heap = [-x for x in max_heap]
    print(max_heap)

find_k_smallest(array, 3)


# Complexity analysis: So we go through the array once, which is O(N)
# We then insert elements into the heap which is O(log k)
# At the end we again go through the heap which is O(k) which results in O(k) + O(N*log k)
# Since O(k) < O(N), the final complexity is O(N*log k)

# Space complexity: O(k)