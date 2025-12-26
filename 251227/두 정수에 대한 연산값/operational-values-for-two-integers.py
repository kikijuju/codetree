a, b = map(int, input().split())

# Please write your code here.\
def func(a, b):
    if a > b:
        print(a+25, b*2)
    else:
        print(a*2, b+25)

func(a,b)