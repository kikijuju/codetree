text = input()
pattern = input()

# Please write your code here. 

def func():
    if pattern in text:
        idx = 0
        for i in range(0, len(text)):
            if text[i] == pattern[0] and text[i+1] == pattern[1]:
                idx = i
                return idx
    else:
        return -1



print(func())
