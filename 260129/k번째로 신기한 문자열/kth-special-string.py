n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
new_lst = []

for i in range(n):
    if t in str[i]:
        new_lst.append(str[i])
        
list(set(new_lst))
new_lst.sort()
print(new_lst[k-1])  