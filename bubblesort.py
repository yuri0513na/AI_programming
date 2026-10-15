def bubbles(list):
    for i in range(len(list)):
        for j in range(len(list)-1, i, -1):
            if list[j] < list[j-1]:
                tempo = list[j]
                list[j] = list[j-1]
                list[j-1] = tempo
    return list
print(bubbles([31,53,69,12,74,88,46,92,21]))