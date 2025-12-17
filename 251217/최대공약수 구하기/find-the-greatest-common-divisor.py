n, m = map(int, input().split())

# Please write your code here.
def func(n, m):
    result = 0
    if n == m:
        result = n
    elif(n > m):
        result = n % m
    else:
        result = m % n

    if result == 0:
        print(1)
    else: 
        print(result)


func(n, m)