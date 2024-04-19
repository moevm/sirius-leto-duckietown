
def read_file_with_inf(name:str):
    matrix = [[]]
    N = 0
    file_to_open = str
    try:
        file_to_open = open(name, "r")
    except:
        print(f"Error! No such file or directory {name}!")
        raise FileExistsError(name)
    for line in file_to_open:
        if line == ("\n" or " \n"):
            continue
        list_of_input_string = line.split()
        for i in range(len(list_of_input_string)):
            if "п»ї" in list_of_input_string[i]:
                list_of_input_string[i] = list_of_input_string[i][3:]
            if list_of_input_string[i] == "inf":
                matrix[N].append(float("inf"))
            elif list_of_input_string[i] == "-":
                matrix[N].append(float("inf"))
            else:
                try:
                    matrix[N].append(float(list_of_input_string[i]))
                except:
                    print("Warning!")
                    print(f"Incorrect value of node: {list_of_input_string[i]}\tcheck file: {name}")
                    matrix[N].append(float("inf"))

        matrix.append([])
        N += 1
    matrix.pop()
    file_to_open.close()
    if N != len(matrix[0]):
        print("Height of matrix == ", N, "\tWidth of matrix == ", len(matrix[0]))
        raise "Error of file-input values"
    print("Height of matrix == ", N, "\nWidth of matrix == ", len(matrix[0]))
    return matrix, N


def read_file(name:str):
    matrix = [[]]
    N = 0
    file_to_open = str
    try:
        file_to_open = open(name, "r")
    except:
        print(f"Error! No such file or directory {name}!")
        raise FileExistsError(name)
    for line in file_to_open:
        if line == ("\n" or " \n"):
            continue
        list_of_input_string = line.split()
        for i in range(len(list_of_input_string)):
            if "п»ї" in list_of_input_string[i]:
                list_of_input_string[i] = list_of_input_string[i][3:]
            if list_of_input_string[i] == "inf":
                matrix[N].append(float("0"))
            elif list_of_input_string[i] == "-":
                matrix[N].append(float("0"))
            else:
                try:
                    matrix[N].append(float(list_of_input_string[i]))
                except:
                    print("Warning!")
                    print(f"Incorrect value of node: {list_of_input_string[i]}\tcheck file: {name}")
                    matrix[N].append(float("0"))

        matrix.append([])
        N += 1
    matrix.pop()
    file_to_open.close()
    if N != len(matrix[0]):
        print("Height of matrix == ", N, "\tWidth of matrix == ", len(matrix[0]))
        raise "Error of file-input values"
    #print("Height of matrix == ", N, "\nWidth of matrix == ", len(matrix[0]))
    return matrix, N
   