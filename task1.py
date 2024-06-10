list_1 = [10, 11, 12]
list_2 = [4, 5, 6]

def sort_list(a, b):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j +=1

    while i < len(a):
        result.append(a[i])
        i+=1

    while j < len(b):
        result.append(b[j])
        j +=1

    return result[::-1]

answer = sort_list(list_1, list_2)
print(answer)
