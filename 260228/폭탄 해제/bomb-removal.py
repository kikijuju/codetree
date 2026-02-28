unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class Boomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
    
boomb1 = Boomb(unlock_code, wire_color, seconds)
print(f'code : {boomb1.code}')
print(f'color : {boomb1.color}')
print(f'second : {boomb1.second}')