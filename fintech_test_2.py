input_string = input()

input_string_len = len(input_string)
moded_list = list(input_string[0:(input_string_len // 2)])
nonmoded_list = list(input_string[(input_string_len // 2):input_string_len])

res_str = ""

if len(moded_list) == len(nonmoded_list):
    for i in range(len(moded_list)):
        res_str += nonmoded_list[i] + moded_list[i]
else:
    for i in range(len(moded_list)):
        res_str += nonmoded_list[i] + moded_list[i]
    res_str += nonmoded_list[len(nonmoded_list) - 1]

print(res_str)
