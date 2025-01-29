array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def prefix_sum(array):

    sum_array = []
    sum = 0

    for item in array:
        sum += item
        sum_array.append(sum)

    #print(sum_array)

prefix_sum(array)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1 2 3
# 4 5 6
# 7 8 9

#biggest_sum_of_squares(matrix)


