

def load_data() -> list:
    with open('3.txt', 'r') as file:
        return [line.replace("\n", "").strip() for line in file.readlines()]

matrix = load_data()

gears = []

class Gear:
    def __init__(self, coordinates, number) -> None:
        self.coordinates = coordinates
        self.numbers = [number]
        print(f"Gear created at {coordinates} with number {number}")

    def add_number(self, number) -> None:
        self.numbers.append(number)
        print(f"Number {number} added to gear at {self.coordinates}. In total {len(self.numbers)} numbers.")
    
    def get_coordinates(self) -> tuple:
        return self.coordinates
    
    def calculate_gear_ratio(self) -> float:
        if len(self.numbers) == 1:
            return 0
        ratio = 1
        for number in self.numbers:
            ratio *= number
        return ratio
    
def get_gear(coordinates) -> Gear or None:
    for gear in gears:
        if gear.get_coordinates() == coordinates:
            return gear
    return None
        

def check_coordinate_for_symbol(x, y) -> bool:
    if matrix[y][x] == "*":
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

    for index, char in enumerate(matrix[index_y]):
        if index >= list_start and index <= list_end:
            print(f"Symbol found: {char} at {index}")
            if char == "*":
                return tuple([index, index_y])

    return None


def check_number(index_x, index_y, num_len) -> bool:
    # check for symbol left
    if index_x > 0:
        if check_coordinate_for_symbol(index_x - 1, index_y):
            return True, tuple([index_x - 1, index_y])
        
    # check for symbol right
    if index_x + num_len < len(matrix[index_y]) - 1:
        if check_coordinate_for_symbol(index_x + num_len, index_y):
            return True, tuple([index_x + num_len, index_y])
        
    # check for symbol top
    if index_y > 0:
        if check_line_for_symbol(index_x, index_y - 1, num_len):
            return True, check_line_for_symbol(index_x, index_y - 1, num_len)
    
    # check for symbol bottom
    if index_y + 1 < len(matrix):
        if check_line_for_symbol(index_x, index_y + 1, num_len):
            return True, check_line_for_symbol(index_x, index_y + 1, num_len)
        
    return False, None
    


def search_for_number():
    number = ""
    temp_x = None
    temp_y = None

    for y, zeile in enumerate(matrix):
        for x, char in enumerate(zeile):
            if char.isdigit():
                number += char
                temp_x = x if temp_x is None else temp_x 
                temp_y = y if temp_y is None else temp_y
            elif number != "":
                outcome, coordinates = check_number(temp_x, temp_y, len(number))
                if outcome:
                    gear = get_gear(coordinates)
                    if gear is None:
                        gear = Gear(coordinates, int(number))
                        gears.append(gear)
                    else:
                        gear.add_number(int(number))
                # reset number to contiune    
                number = ""
                temp_x = None
                temp_y = None
            else:
                continue

search_for_number()

sum = 0
for gear in gears:
    sum += gear.calculate_gear_ratio()
    print(gear.calculate_gear_ratio())

print(sum)