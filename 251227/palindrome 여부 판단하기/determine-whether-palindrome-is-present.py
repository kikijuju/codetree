A = input()

# Please write your code here.
def palin(A):
    if A == A[::-1]:
        print('Yes')
    else:
        print('No')

palin(A)