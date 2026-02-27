user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class NextLevel:
    def __init__(self, id='codetree', lv=10):
        self.id = id
        self.lv = lv

nextlevel = NextLevel()
user1 = NextLevel(user2_id, user2_level)
print('user', nextlevel.id, 'lv', nextlevel.lv)
print('user', user2_id, 'lv', user2_level)