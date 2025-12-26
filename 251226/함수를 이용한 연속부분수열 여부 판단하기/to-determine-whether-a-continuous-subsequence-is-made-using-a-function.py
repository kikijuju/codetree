n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def func(a, b):
    if len(b) == 1:
        return False
    str_a = ''
    str_b = ''
    for i in a:
        str_a += str(i) + ' '
    for j in b:
        str_b += str(j) + ' '

    if str_b in str_a:
        return True
    else:
        return False

if func(a, b):
    print('Yes')
else:
    print('No')
    