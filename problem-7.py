def sum_digit(n):
    if(n==0):
        return 0
    while(n>0):
        return((n%10)+(sum_digit(n//10)))

print(sum_digit(123))