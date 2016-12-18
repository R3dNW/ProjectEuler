count = 0

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

dd = 0
mm = 1
yy = 1901

day = 0 # 1 Jan 1901 is a Tuesday

while True:
    dd += 1
    day = (day + 1) % 7

    if dd > 30 and mm in [9, 4, 6, 11]:
        dd %= 30
        mm += 1
    elif dd > 31 and mm in [1, 3, 5, 7, 8, 10, 12]:
        dd %= 31
        mm += 1
    elif dd > 29 and mm == 2 and yy % 4 == 0 and (yy % 100 != 0 or yy % 400 == 0):
        dd %= 29
        mm += 1
    elif dd > 28 and mm == 2:
        dd %= 28
        mm += 1

    if mm > 12:
        mm %= 12
        yy += 1

    if dd == 1 and mm == 1 and yy == 2001:
        break

    if days[day] == "Sunday" and dd == 1:
        count += 1

print(count)
