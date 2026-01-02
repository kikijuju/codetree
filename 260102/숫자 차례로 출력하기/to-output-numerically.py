n = int(input())

# Please write your code here.
m = n
def func(n):
    global m

    if n == 0:
        return
    
    print(n, end = ' ')
    func(n-1)
    if n == 1:
        print()
    print(n, end = ' ')
    

func(n)
