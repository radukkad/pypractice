input_arr = [3,6,1,2,8,4,0]
for i in range(len(input_arr)):
    for j in range(len(input_arr)):
        if input_arr[i] < input_arr[j]:
            temp = input_arr[i]
            input_arr[i] = input_arr[j]
            input_arr[j] = temp
print(input_arr)