n = int(input())

base_distance = 100
best_distance = 100
steps_list = []

for i in range(n):
    steps_list.append(int(input()))

len_steps_list = len(steps_list)

for i in range(len_steps_list):
    base_distance += steps_list[i]
    base_distance = abs(base_distance)
    if base_distance < best_distance:
        best_distance = base_distance

print(best_distance)
