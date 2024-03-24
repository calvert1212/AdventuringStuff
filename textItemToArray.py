#Parses Items.txt into a list of arrays
def arrify(file_path):
    iArr = []
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming each line contains elements separated by spaces
            array = line.strip().split()
            iArr.append(array)
    return iArr
