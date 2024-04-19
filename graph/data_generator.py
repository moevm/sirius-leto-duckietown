def data_genterator(size):
    arr_a = []
    arr_b = []
    import random
    for a in range(size):
        arr_a = []
        for b in range(size):
            if a == b:
                arr_a.append(float('inf'))
            else:
                arr_a.append(0)
        arr_b.append(arr_a)
    for x in range(size):
        for y in range(size):
            if arr_b[x][y] == 0:
                rand = random.randint(1,1e3)
                arr_b[x][y] = rand
                rand = random.randint(1,1e3)
                arr_b[y][x] = rand

    with open("data.txt", 'w') as file:
        for string in arr_b:
            for element in string:
                file.write(str(element) + ' ')
            file.write('\n')
                #file.close()

        