import time

print(time.time())
time.sleep(2)
print("This is printed after 2 secs")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)