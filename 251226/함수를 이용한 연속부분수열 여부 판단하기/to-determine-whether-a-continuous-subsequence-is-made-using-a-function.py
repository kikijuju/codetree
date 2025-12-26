n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def func(a, b):
    if len(b) ==1 and len(a) == 1 and a[0] == b[0]:
        return True
    elif len(b) ==1 or len(a) == 1:
        return False
    else:
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
    