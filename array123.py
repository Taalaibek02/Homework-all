def array123(nums):
    n = []
    for i in range(nums):
        n.append(int(input('your numbers here: ')))
    for i in range(len(n)-2):
        if n[i]==1 and n[i+1]==2 and n[i+2] == 3:
            return True
        else:
            return False
print(array123(5))
