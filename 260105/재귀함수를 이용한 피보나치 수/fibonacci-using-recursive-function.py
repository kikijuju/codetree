N = int(input())

# Please write your code here.
def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return fibo(n-1) + fibo(n-2)

n = N-1

print(fibo(n))
