n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
sortt = []
for i in range(len(arr)):
    sortt.append(arr[i])
    sortt.sort()
    if (i+1) % 2 == 1:
        print(sortt[(i+1)//2], end=' ')
        