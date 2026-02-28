n = int(input())

# Please write your code here.
class List:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
persons = []   
for _ in range(n):
    name, height, weight = tuple(input().split())
    persons.append(List(name, height, weight))

persons.sort(key=lambda x : x.height)

for i in range(n):
    print(f'{persons[i].name} {persons[i].height} {persons[i].weight}')
