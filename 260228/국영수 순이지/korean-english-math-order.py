n = int(input())

# Please write your code here.
class Subject:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

subs = []
for _ in range(n):
    name, korean, english, math = tuple(input().split())
    subs.append(Subject(name, int(korean), int(english), int(math)))

subs.sort(key = lambda x : (-x.korean, -x.english, -x.math))
for i in range(n):
    print(f'{subs[i].name} {subs[i].korean} {subs[i].english} {subs[i].math}')