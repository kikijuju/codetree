n = 5

# Please write your code here.
class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

p_infos = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    p_infos.append(Info(name, int(height), float(weight)))

name_info = sorted(p_infos, key=lambda x : x.name)
height_info = sorted(p_infos, key=lambda x : -x.height)

print('name')
for i in range(n):
    print(f'{name_info[i].name} {name_info[i].height} {name_info[i].weight:.1f}')

print()

print('height')
for i in range(n):
    print(f'{height_info[i].name} {height_info[i].height} {height_info[i].weight:.1f}')

