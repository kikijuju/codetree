N = int(input())

# Please write your code here.
def func(count, N):
    if N == 1:
        return count
    
    if N % 2 == 0:
        return func(count+1, N // 2)
    else:
        return func(count+1, N // 3)
    
print(func(0, N))
    