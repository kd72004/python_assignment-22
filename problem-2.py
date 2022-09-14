def sum_odd(n):
    if(n==0):
        return 0
    if(n%2!=0):
        return(n+sum_odd(n-1))
    else:
        return(sum_odd(n-1))
print(sum_odd(10))