def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        if target_sum > current_sum:
            left += 1
        else:
            right -= 1
    return [-1, -1]


def pair_with_targetsum_withmap(arr, target_sum):
    nums = {}
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
