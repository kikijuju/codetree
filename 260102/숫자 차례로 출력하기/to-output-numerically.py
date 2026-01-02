n = int(input())

# Please write your code here.
def func(n):
    
    if n == 8:
        return
    
    print(n, end = ' ')
    func(n+1)
    if n == 7:
        print()
    print(n, end = ' ')
    

func(1)
