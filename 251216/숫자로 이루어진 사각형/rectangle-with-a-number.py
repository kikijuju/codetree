n = int(input())


# Please write your code here.
def square_by_num(n):
    count = 1
    for i in range(n):
        for j in range(n):
            if count > 9:
                count = 1
            print(count, end = ' ')  
            count += 1  
        print()        

square_by_num(n)