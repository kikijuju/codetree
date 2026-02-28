n = int(input())

# Please write your code here.

class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

rain_day = []
for _ in range(n):
    date, day, weather = tuple(input().split())
    rain_day.append(Weather(date, day, weather))

rain_day = sorted(rain_day, key=lambda x : x.date)

i = 0
while True:
    if rain_day[i].weather == 'Rain':
        print(f'{rain_day[i].date} {rain_day[i].day} {rain_day[i].weather}')
        break
    i+=1