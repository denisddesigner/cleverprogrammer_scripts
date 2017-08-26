# print ranges using the for loop
# range(start, finish)
# range(0 ,2) --> [0, 1, 2]
# print([0, 1, 2, 3, 4])

for number in range(5):
    print(number)

# print numbers from 20 to 41 (excluding 41)
for number in range(20, 41):
    print(number)

# [1, 2, 3] --> 6
count = 0
for number in range(1, 4):
    # new_count = old_count + number
    count = count + number

# It should be 6
print(count)



# write a function that sums all elements of a list and returns them

def sum_list(my_list):
    count = 0
    for number in my_list:
        count = count + number

    return count

# assert sum_list([1, 2, 3]) == 6 # --> 6
assert sum_list([1, 2, 3]) == 6
assert sum_list([1, 2, 3, 4]) == 10
print(sum_list([1, 2]))

