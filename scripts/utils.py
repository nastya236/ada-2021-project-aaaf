def iterate(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line
