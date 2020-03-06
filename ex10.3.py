# write function that takes list of numbers and returns cumulative sum
# where nth element is sum of first i + 1 elements from original list
# input: [1, 2, 3]
# output: [1, 3, 6]

list1 = [1, 2, 3]
list2 = [2, 5, 10]

def cumulative_sum(number_list):
    sum_list = []
    count = 0

    for number in number_list:
        number += count
        sum_list.append(number)
        count = number

    return sum_list


print(cumulative_sum(list1))
print(cumulative_sum(list2))
