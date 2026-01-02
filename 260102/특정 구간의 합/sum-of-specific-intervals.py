n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def func():
    global n, m
    for i in range(0, m):
        hap = sum(arr[queries[i][0]-1:queries[i][1]])
        print(hap)

func()