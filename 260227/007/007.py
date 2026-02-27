secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class Secret:
    def __init__(self, secret_code, meeting_point, time):
        self.code = secret_code
        self.point = meeting_point
        self.time = time
    
secret = Secret(secret_code, meeting_point, time)

print("secret code :", secret.code)
print("meeting point :", secret.point)
print("time :", secret.time)

