n = int(input())

class Sorted_std:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

strs = []
for _ in range(n):
    name, height, weight = input().split()
    strs.append(Sorted_std(name, int(height), int(weight)))

strs.sort(key=lambda x: (x.height, -x.weight))

for i in range(n):
    print(f'{strs[i].name} {strs[i].height} {strs[i].weight}')