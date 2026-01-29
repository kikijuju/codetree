n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
new_lst = []

for i in range(n):
    if t == str[i][0:2]:
        new_lst.append(str[i])
        
new_lst.sort()

if len(new_lst) == 1:
    print(new_lst[0])
else:
    print(new_lst[k-1])  