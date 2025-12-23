a, b = map(int, input().split())

# Please write your code here.
def func(a, b):
    result = a
    for _ in range(b-1):
        result *= a

    print(result)

func(a, b)