n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def max(n, arr):
    if n <= 1:
        return arr[0]

    elif arr[0] >= arr[1]:
        del arr[1]

    else:
        del arr[0]

    return max(n-1, arr)

print(max(n, arr))
