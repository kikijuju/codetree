N = int(input())

# Please write your code here.
def fec(N):
    if N < 2:
        return 1

    return N * fec(N-1)

print(fec(N))