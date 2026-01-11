n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

def func(A, B):
    A.sort()
    B.sort()
    if A == B:
        return "Yes"
    else:
        return "No"
    
print(func(A, B))