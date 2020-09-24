def front_times(str,n):
    result = (str[0]+str[1]+str[2])*n
    return  result
print(front_times(input("put your word here: "), int(input("how many times to repeat the code? "))))