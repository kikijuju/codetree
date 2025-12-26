n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def func(arr):
    for i in arr:
        print(abs(i), end = ' ')

func(arr)