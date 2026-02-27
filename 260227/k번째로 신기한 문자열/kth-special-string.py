n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

str.sort()


def is_it(i, t):
    if t in i:
        return True
    else:
        return False

for i in str:
    if not is_it(i, t):
        str.remove(i)

     
    
print(str[k-1])