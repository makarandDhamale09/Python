import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
if hour < 12:
    print("Good Morning Sir !!!!")
elif hour < 16:
    print("Good Afternoon Sir!!")
elif hour < 20:
    print("Good Evening Sir!!!")
else:
    print("Good Night Sir !!!")
