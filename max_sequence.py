def max_sequence(arr):
    maxsum = 0
    tmp = 0
    for num in arr:
        tmp += num
        if tmp > maxsum:
            maxsum = tmp
        elif tmp < 0:
            tmp = 0
    return maxsum
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))