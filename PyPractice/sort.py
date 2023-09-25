input_arr = [3, 6, 1, 2, 8, 4, 0]
# bruteforce
for i in range(len(input_arr)):
    for j in range(len(input_arr)):
        if input_arr[i] < input_arr[j]:
            temp = input_arr[i]
            input_arr[i] = input_arr[j]
            input_arr[j] = temp


# print(input_arr)
# selection sort
# time complexity O(n*n)
# sorting by finding min_index
def selection_sort(array, array_size):
    for ind in range(array_size):
        min_index = ind
        for j in range(ind + 1, array_size):
            # select the minimum element in each iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping ghe elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selection_sort(arr, size)
print(arr)
