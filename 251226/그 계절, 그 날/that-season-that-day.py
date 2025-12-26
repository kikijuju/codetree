Y, M, D = map(int, input().split())

# Please write your code here.

def yoon(Y):
    if Y % 4 == 0:
        if Y % 400 == 0:
            return True
        elif Y % 100 == 0:
            return False
        return True
    return False

def season(Y, M, D):
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if yoon(Y) and M == 2:
        Feb = 29
        if D <= Feb:
            print("Winter")
        else: 
            print(-1)
    else:
        if 12 == M or M < 2 and D <= day[M-1]:
            print("Winter")
        elif 3 <= M and M < 6 and D <= day[M-1]:
            print("Spring")
        elif 6 <= M and M < 9 and D <= day[M-1]:
            print("Summer")
        elif 9 <= M and M < 12 and D <= day[M-1]:
            print("Fall")
        else:
            print(-1)
        
season(Y, M, D)