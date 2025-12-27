a, b = map(int, input().split())

# Please write your code here.
def func(a, b):
    if a > b:
        a *= 2
        b += 10
    else:
        b *= 2
        a += 10
    
    print(a, b, end = ' ')

func(a, b)

