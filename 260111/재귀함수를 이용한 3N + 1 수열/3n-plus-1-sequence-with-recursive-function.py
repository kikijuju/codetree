n = int(input())

# Please write your code here.
def func(cnt, n):
    if n == 1:
        return cnt
    if n % 2 == 0:
        cnt += 1
        return func(cnt, n//2)
    else:
        cnt += 1
        return func(cnt, n*3 +1)

print(func(0, n))
