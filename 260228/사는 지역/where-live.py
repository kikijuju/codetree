n = int(input())

# Please write your code here.
class Live:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

info = []
for _ in range(n):
    name, address, region = tuple(input().split())
    info.append(Live(name, address, region))

result = sorted(info, key = lambda x : x.name)
print(f'name {result[-1].name}')
print(f'addr {result[-1].address}')
print(f'city {result[-1].region}')
