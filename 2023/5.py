from typing import List
from tqdm import tqdm

def load_data() -> list:
    with open('5.txt', 'r') as file:
        return [line.replace("\n", "").strip() for line in file.readlines()]
    

class SingleMapping:
    def __init__(self, source, destination, length) -> None:
        self.source = int(source)
        self.destination = int(destination)
        self.length = int(length)

    def check(self, source_int: int):
        '''
        Returns:
            changed: bool - if the number was changed or if it stays the input value
            result: int - the result of the mapping
            skipping_value: int - for how many numbers above the source_int is the mapping still valid
        '''
        source_int = int(source_int)
        changed = False
        skipping_value = 0
        result = source_int
        if self.source <= source_int < (self.source + self.length):
            result = source_int - self.source + self.destination
            skipping_value = self.source + self.length - source_int - 1
            changed = True
        elif self.source > source_int:
            skipping_value = self.source - source_int - 1
        else:
            skipping_value = -1
        return changed, result, skipping_value

class Map:
    def __init__(self, source_name, destination_name) -> None:
        self.source_name = source_name
        self.destination_name = destination_name
        self.mapping_list: List[SingleMapping] = []

    def add_mapping(self, map: SingleMapping):
        self.mapping_list.append(map)

    def check_mapping(self, source_int: int):
        skipping_value = 10000000000000000000000
        for mapping in self.mapping_list:
            int_changed, source_int, new_skipping_value = mapping.check(source_int)
            if new_skipping_value < skipping_value and new_skipping_value != -1:
                skipping_value = new_skipping_value
            if int_changed: break;
        
        return source_int,  skipping_value


def parse_for_mapping(raw_data: List[str]):
    seed_numbers = []
    maps: List[Map] = []

    for index, line in enumerate(raw_data):
        if index == 0:
            seed_numbers = line.split(":")[1].strip().split(" ")
        else:
            if line == "":
                continue
            elif line[0].isalpha():
                source_name = line.split(" ")[0].split("-")[0]
                dest_name = line.split(" ")[0].split("-")[2]
                maps.append(Map(source_name, dest_name))
            elif line[0].isdigit():
                dest = line.split(" ")[0]
                source = line.split(" ")[1]
                length = line.split(" ")[2]

                maps[-1].add_mapping(SingleMapping(source, dest, length))

    return seed_numbers, maps


def main_1():
    seed_numbers, maps = parse_for_mapping(load_data())

    lowest_result = 10000000000000000000000

    for number in seed_numbers:
        print(f"Now handeling: {number}")
        result = number
        for map in maps:
            result, _ = map.check_mapping(result)
        
        if result < lowest_result:
            lowest_result = result

    print(f"Lowest result: {lowest_result}")

def main_2():
    seed_numbers_raw, maps = parse_for_mapping(load_data())

    lowest_result = 10000000000000000000000
    seed_numbers_pairs = []

    temp = None
    for number in seed_numbers_raw:
        if temp is None:
            temp = number
        else:
            seed_numbers_pairs.append(tuple((temp, number)))
            temp = None
    
    skipping_value = -1
    for start_number, length in seed_numbers_pairs:
        for i in tqdm(range(int(length))):
            result = int(start_number) + i
            if  skipping_value > 0:
                skipping_value -= 1
                continue
            else:
                skipping_value = -1

            for map in maps:
                result, new_skipping_value = map.check_mapping(result)
                if new_skipping_value < skipping_value or  skipping_value == -1:
                    skipping_value = new_skipping_value

            if result < lowest_result:
                lowest_result = result

    print(f"Lowest result: {lowest_result}")





main_1()