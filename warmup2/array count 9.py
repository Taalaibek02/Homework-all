def array_count9(nums):
    n = []
    for i in range(nums):
        n.append(int(input('numbers here: ')))
    count = 0
    for i in n:
        if n == 9:
            count = count + 1
    return count
print(array_count9(5))