def sum_squ(n):
    if(n==0):
        return 0
    return (n*n+sum_squ(n-1))

print(sum_squ(5))