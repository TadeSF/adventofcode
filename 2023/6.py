from typing import List
import sys


with open(sys.argv[1], 'r') as file:
    data = [line.replace("\n", "").strip() for line in file.readlines()]


class Race:
    def __init__(self, time: int, record_distance: int) -> None:
        self.time: int = time
        self.record_distance: int = record_distance
        self.winning_button_times: List = []

        self.calculate_winning_button_times()


    def calculate_winning_button_times(self):
        for button_hold_time in range(self.time):
            distance = button_hold_time * (self.time - button_hold_time)
            if distance > self.record_distance:
                self.winning_button_times.append(distance)

    def get_possible_winning_times(self):
        return len(self.winning_button_times)



def main_1():
    times = []
    records = []
    races: List[Race] = []

    for split in data[0].split(":")[1].split(" "):
        if split != "":
            times.append(int(split))

    for split in data[1].split(":")[1].split(" "):
        if split != "":
            records.append(int(split))

    
    for i in range(len(times)):
        races.append(Race(times[i], records[i]))
    
    possibilities = 1

    for race in races:
        possibilities *= race.get_possible_winning_times()

    print(possibilities)


def main_2():
    time = int(data[0].split(":")[1].replace(" ", ""))
    record = int(data[1].split(":")[1].replace(" ", ""))
    race: Race = Race(time, record)

    print(race.get_possible_winning_times())


if __name__ == "__main__":
    if sys.argv[2] == "main_1":
        main_1()
    elif sys.argv[2] == "main_2":
        main_2()
    else:
        print("Missing second argument: main_1 or main_2")
