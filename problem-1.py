def sum_of_num(n):
    sum=0
    if(n==0):
        return 0
    return n+sum_of_num(n-1)

print(sum_of_num(10))