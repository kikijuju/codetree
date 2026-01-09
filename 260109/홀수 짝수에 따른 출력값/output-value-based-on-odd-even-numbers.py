N = int(input())

# Please write your code here.
def func(N):
    if N < 2:
        return N

    if N % 2 == 0:
        return N + func(N-2)
    else:
        return N + func(N-2)
    
print(func(N))