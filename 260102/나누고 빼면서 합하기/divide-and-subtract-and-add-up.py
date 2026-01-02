n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def func(m):
    hap = 0
    while m >= 1:
        hap += A[m-1]
        if m % 2 == 0:
            m //= 2
        elif m % 2 == 1:
            m -= 1

    return hap

print(func(m))