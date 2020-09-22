def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open (csv_file_path, "r") as file:
    line = file.readlines()
    for l in line:
        l = l.split(",")
        for i in range(len(l)):
            l[i] = eval(l[i])
        result.append(l)
    return result
