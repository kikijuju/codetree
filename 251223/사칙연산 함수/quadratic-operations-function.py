a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def cal(a, o, c):
    if o == "+":
        return a + c
    elif o == "-":
        return a - c
    elif o == "/":
        return a//c
    elif o == "*":
        return a*c

print(f'{a} {o} {c} = {cal(a,o,c)}')