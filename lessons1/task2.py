#Задание 2

time_sec = int(input("Введите время в секундах:"))
if time_sec < 60:
    print(f"00:00:{time_sec}")
elif time_sec >= 60 | time_sec < 3600:
    time_min = time_sec // 60
    sec = time_sec % 60
    print(f"00:{time_min}:{sec}")
else:
    hour = time_sec // 3600
    time_min = (time_sec-3600) // 60
    sec = (time_sec-3600) % 60
    print(f"{hour}:{time_min}:{sec}")
