a, b = map(int, input().split())

# Please write your code here.
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False

    return True
        

def prime_num(a, b):
    num = 0
    for i in range(a, b+1):
        if is_prime(i):
            num += i
    return num

print(prime_num(a, b))


