n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

str.sort()
strr = []

def is_it(i, t):
    if i[:len(t)] == t:
        return True
    else:
        return False

for i in str:
    if is_it(i, t):
        strr.append(i)
    else:
        pass
     
print(strr[k-1])