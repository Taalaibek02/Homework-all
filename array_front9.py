def array_front9(nums):
    n = []
    for i in range(nums):
      n.append(int(input('your numbers: ')))
    if n[0]==9 or n[1]==9 or n[2]==9 or n[3]==9:
        return True
    else:
        return False

print(array_front9(int(input('How many numbers are in your set? '))))