import sys
import threading


def check_triplet(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        print("a = {0}, b = {1}, c = {2}, abc = {3}".format(a, b, c, a * b * c))
        sys.exit()


for a in range(1, 501):
    for b in range(1, 501):
        c = 1000 - a - b

        if a < b < c:
            t = threading.Thread(target=check_triplet, args=[a, b, c])
            t.daemon = True
            t.start()
