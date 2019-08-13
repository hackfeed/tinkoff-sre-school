dim_list = list(map(int, input().split()))
skills_matrix = [list(map(int, input().split())) for _ in range(dim_list[0])]

people_per_task = [0] * dim_list[1]
used_employees = []
tasks_done = 0

for i in range(dim_list[1]):
    for j in range(dim_list[0]):
        if skills_matrix[j][i]:
            people_per_task[i] += 1

for i in range(dim_list[1]):
    min_people_per_task = min(people_per_task)
    task_ind = people_per_task.index(min_people_per_task)
    for j in range(dim_list[0]):
        if skills_matrix[j][task_ind] and j not in used_employees:
            used_employees.append(j)
            tasks_done += 1
            break
    people_per_task[task_ind] = dim_list[0] + 1

print(tasks_done)
