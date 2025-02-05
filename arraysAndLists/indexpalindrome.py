

a = "abbdbbbd"

mid_index = len(a) // 2

left = a[:mid_index]
right = a[mid_index:]

print(left)
print(right)

from collections import Counter

left_counter = Counter(left)
right_counter = Counter(right)
diff_counter = left_counter - right_counter
print(left_counter - right_counter)
sum = sum(diff_counter.values())
print(sum)

one = 'aaab' #(first query)
two = 'baa' #(second query)
three = 'aaa' #(third query
four = 'abaa'

checker = one

from collections import deque

left_string = one[0]    
right_queue = deque(checker)

right_queue.popleft() #from aaab now its aab 

new_string = "".join([item for item in right_queue])

if new_string == new_string[::-1]:
    print("palindrome!")
    print("0")
    exit()

for index in range(1, len(checker) + 1):

    left_string = checker[:index]
    print(left_string)

    right_queue.popleft()
    right_string = "".join(right_queue)

    final_string = left_string + right_string
    print(f"Final: {final_string}")

    if final_string == final_string[::-1]:
        print(f"PALINDROME! with {index}")
        break


    
