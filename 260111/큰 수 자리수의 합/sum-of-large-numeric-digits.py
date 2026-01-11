a, b, c = map(int, input().split())

# Please write your code here.
def func(N):
    if N < 10:
        return N
    return (N%10) + func(N // 10)

print(func(a*b*c))