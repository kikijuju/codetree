a, b = map(int, input().split())

# Please write your code here.
def perfect_number(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0):
            cnt += 1
    
    length = b-a+1
    print(length-cnt)

perfect_number(a, b)