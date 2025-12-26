M, D = map(int, input().split())

# Please write your code here.
def TF(M, D):
    lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if M > 12 or D > 31:
        return False
    elif D <= lst[M+1]:
        return True


if TF(M, D): 
    print("Yes")
else:
    print("No")