

def load_data() -> list:
    with open('3.txt', 'r') as file:
        return [line.replace("\n", "").strip() for line in file.readlines()]

matrix = load_data()

results = []
excluded = []

def check_coordinate_for_symbol(x, y) -> bool:
    if (not matrix[y][x].isdigit()) and (matrix[y][x] != "."):
        return True
    return False


def check_line_for_symbol(index_x, index_y, num_len) -> bool:
    list_start = index_x - 1
    list_end = index_x + num_len
    
    # check if the left is out of range and correct it
    if list_start < 0:
        list_start = 0

    # check if the right is out of range and correct it
    if list_end > len(matrix[index_y]):
        list_end = len(matrix[index_y]) - 1

    shorted_list = matrix[index_y][list_start:list_end]

    for char in shorted_list:
        if (not char.isdigit()) and (char != "."):
            return True
    
    return False


def check_number(index_x, index_y, num_len) -> bool:
    # check for symbol left
    if index_x > 0:
        if check_coordinate_for_symbol(index_x - 1, index_y):
            return True
        
    # check for symbol right
    if index_x + num_len < len(matrix[index_y]) - 1:
        if check_coordinate_for_symbol(index_x + num_len, index_y):
            return True
        
    # check for symbol top
    if index_y > 0:
        if check_line_for_symbol(index_x, index_y - 1, num_len):
            return True
    
    # check for symbol bottom
    if index_y + 1 < len(matrix):
        if check_line_for_symbol(index_x, index_y + 1, num_len):
            return True
        
    return False
    


def search_for_number():
    number = ""
    temp_x = None
    temp_y = None

    for y, zeile in enumerate(matrix):
        for x, char in enumerate(zeile):
            if char.isdigit():
                number += char

                # Here was one of the biggest mistakes. We forgot that while happily iterating through the matrix
                # until we found the next . after a number, the . could be already in the next line, screwing up the whole
                # coordinate. Fix: We save the coordinates the first time we encounter a number and use them until we
                # found the next point. Afterwards, we reset the coordinates to None. The weird if statements in the next 
                # two lines is needed to prevent overwriting the coordinates.
                temp_x = x if temp_x is None else temp_x 
                temp_y = y if temp_y is None else temp_y
            elif number != "":
                if check_number(temp_x, temp_y, len(number)): # here we can actually use the saved coordinates
                    results.append(int(number))
                else:
                    excluded.append(int(number))
                    
                # reset number to contiune    
                number = ""
                temp_x = None
                temp_y = None
            else:
                continue

search_for_number()

print(results)
print(excluded)

print(sum(results))
print(sum(excluded))