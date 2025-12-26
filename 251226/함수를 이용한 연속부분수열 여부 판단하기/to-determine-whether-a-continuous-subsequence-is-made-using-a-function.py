n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def func(a, b):
    str_a = ''
    str_b = ''
    for i in a:
        str_a += str(i) + ' '
    for j in b:
        str_b += str(j) + ' '

    if str_b in str_a:
        print('Yes')
    else:
        print('No')

func(a, b)
    