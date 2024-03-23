def arrify(file_path):
    itemArr = []
    with open(ItemList.txt, 'r') as file:
        for line in file:
            # Assuming each line contains elements separated by spaces
            array = line.strip().split()
            itemArr.append(array)
    return arrays

# Example usage:
file_path = 'ItemList.txt'  # Replace 'input.txt' with the path to your text file
arrays = lines_to_arrays(file_path)
print(arrays)