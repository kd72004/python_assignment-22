def sum_cub(n):
    if(n==0):
        return 0
    return(n*n*n+sum_cub(n-1))

print(sum_cub(10))