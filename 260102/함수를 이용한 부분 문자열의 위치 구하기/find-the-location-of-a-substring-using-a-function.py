text = input()
pattern = input()

# Please write your code here. 

def func():
    if pattern in text:
        idx = 0
        for i in range(0, len(text)):
            if text[i:i+len(pattern)] == pattern:
                idx = i
                return idx
    else:
        return -1


print(func())
