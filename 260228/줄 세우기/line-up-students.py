n = int(input())

# Please write your code here.
class Students:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num
    
stds = []
for i in range(n):
    height, weight = map(int, input().split())
    stds.append(Students(height, weight, i+1))

stds.sort(key=lambda x: (-x.height, -x.weight, x.num))

for i in range(n):
    print(f'{stds[i].height} {stds[i].weight} {stds[i].num}')