n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def func(n1, n2, a, b):
    for i in range(n1 - n2 + 1):
        if a[i:i + n2] == b:
            return True
    

if func(n1, n2, a, b):
    print('Yes')
else:
    print('No')
    