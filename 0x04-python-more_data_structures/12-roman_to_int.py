#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    r_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    r_list = []
    for i in roman_string:
        l_idx = len(r_list) - 1
        if l_idx >= 0 and (r_list[l_idx] == r_dict[i]):
            r_list[l_idx] = r_list[l_idx] + r_dict[i]
        else:
            r_list.append(r_dict[i])
    prev = 0
    new_list = []
    for i in range(len(r_list)):
        if prev != 0 and prev < r_list[i]:
            new_list[i - 1] = -prev
        new_list.append(r_list[i])
        prev = r_list[i]
    sum = 0
    for i in new_list:
        sum += i
    return sum