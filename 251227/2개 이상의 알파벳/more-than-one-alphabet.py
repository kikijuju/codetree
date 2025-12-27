A = input()

# Please write your code here.
def func(A):
    unique_chars = set(A)
    if len(unique_chars) >= 2:
        return True


if func(A):
    print("Yes")
else:
    print("No")