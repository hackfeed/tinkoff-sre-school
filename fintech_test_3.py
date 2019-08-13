from math import sqrt
from itertools import combinations


def is_on_section(x1, y1, x2, y2, x3, y3):
    return abs(sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2) +
               sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2) -
               sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) < 0.000001


n = int(input())

dots_list = []
matches = 0

for _ in range(n):
    dots_list.append(tuple(map(int, input().split())))

for two_dots in combinations(dots_list, 2):
    cur_dots_list = dots_list[:]
    flag = True

    for x in two_dots:
        while x in cur_dots_list:
            cur_dots_list.remove(x)

    for dot in cur_dots_list:
        if is_on_section(two_dots[0][0], two_dots[0][1],
                         two_dots[1][0], two_dots[1][1],
                         dot[0], dot[1]):
            flag = False

    if flag:
        matches += 1

matches *= 2

print(matches)
