n = int(input())

# Please write your code here.
class Hap:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    
hap_scores = []
for _ in range(n):
    name, score1, score2, score3 = tuple(input().split())
    hap_scores.append(Hap(name, int(score1), int(score2), int(score3)))

hap_scores.sort(key=lambda x : (x.score1 + x.score2 + x.score3))

for i in range(n):
    print(f'{hap_scores[i].name} {hap_scores[i].score1} {hap_scores[i].score2} {hap_scores[i].score3}')