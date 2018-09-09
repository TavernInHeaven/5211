def in_sort(in_list):
    for j in range(1, len(in_list)):
        key = in_list[j]
        i = j - 1
        while i > -1 and in_list[i] > key:
            in_list[i + 1] = in_list[i]
            i = i - 1
        in_list[i + 1] = key
    return in_list

def in_sort2(in_list):
    for j in range(2, len(in_list)):
        key = in_list[j]
        i = 0
        while i < j and in_list[i] > key:
            in_list[j] = in_list[i]
            i = i + 1
            in_list[i - 1] = key
    return in_list

print(in_sort([5,2,4,6,1,3]))