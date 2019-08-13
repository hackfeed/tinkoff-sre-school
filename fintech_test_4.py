dim_list = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(dim_list[0])]

ans = 0
stack = []
dynamic = [-1] * dim_list[1]
dynamic_f = [0] * dim_list[1]
dynamic_s = [0] * dim_list[1]

for i in range(dim_list[0]):
    for j in range(dim_list[1]):
        if matrix[i][j] == 1:
            dynamic[j] = i

    while len(stack):
        stack.pop()

    for j in range(dim_list[1]):
        while len(stack) and dynamic[stack[-1]] <= dynamic[j]:
            stack.pop()
        dynamic_f[j] = -1 if not len(stack) else stack[-1]
        stack.append(j)

    while len(stack):
        stack.pop()

    for j in range(dim_list[1] - 1, -1):
        while len(stack) and dynamic[stack[-1]] <= dynamic[j]:
            stack.pop()
        dynamic_s[j] = dim_list[1] if not len(stack) else stack[-1]
        stack.append(j)

    for j in range(dim_list[1]):
        ans = max(ans, (i - dynamic[j]) * (dynamic_s[j] - dynamic_f[j] - 1))

print(ans)
