a, b = map(int, input().split())

# Please write your code here.
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
 
    return True

def prime_number(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_prime(i):
            if (i//10 + i%10)%2 ==0:
                cnt += 1 
    print(cnt)

prime_number(a, b)