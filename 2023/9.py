from typing import List
from misc import start_program


class SensorData:
    def __init__(self, data: List[int]) -> None:
        self.data: List[int] = data
        self.differences = []
        self.calculate_differences()

    def calculate_differences(self):
        for i in range(len(self.data) - 1):
            self.differences.append(self.data[i + 1] - self.data[i])

    def check_for_all_zero(self):
        if all([x == 0 for x in self.differences]):
            return True
        return False

    def add_extrapolation(self, value: int):
        self.differences.append(value)

    def calculate_extrapolation(self):
        if len(self.differences) == len(self.data):
            raise Exception("No extrapolation needed")
        self.data.append(self.data[-1] + self.differences[-1])

    def get_differences(self):
        return self.differences

    def get_extrapolation_value(self):
        return self.data[-1]

    def __str__(self) -> str:
        return f"{self.data}"


class SensorDataCollection:
    def __init__(self, data: List[int]) -> None:
        self.calculations = [SensorData(data)]
        self.final_extrapolation = None

        while not self.calculations[-1].check_for_all_zero():
            self.calculations.append(
                SensorData(self.calculations[-1].get_differences())
            )

    def calculate_extrapolations(self):
        for i in range(len(self.calculations) - 1, 0, -1):
            self.calculations[i].calculate_extrapolation()
            self.calculations[i - 1].add_extrapolation(
                self.calculations[i].get_extrapolation_value()
            )
        self.calculations[0].calculate_extrapolation()

        self.final_extrapolation = self.calculations[0].get_extrapolation_value()

    def get_extrapolation(self):
        return self.final_extrapolation

    def __str__(self) -> str:
        output = ""
        for calculation in self.calculations:
            output += f"{calculation}\n"
        return output


def main(data: List[str], reverse: bool = False):
    sensor_data = []
    for line in data:
        if not reverse:
            sensor_data.append(SensorDataCollection([int(x) for x in line.split(" ")]))
        else:
            sensor_data.append(
                SensorDataCollection([int(x) for x in line.split(" ")][::-1])
            )

    extrapolation_sum = 0
    for sensor in sensor_data:
        sensor.calculate_extrapolations()
        extrapolation_sum += sensor.get_extrapolation()

    print("Extrapolation sum:", extrapolation_sum)


def main_1(data: List[str]):
    main(data)


def main_2(data: List[str]):
    main(data, True)


if __name__ == "__main__":
    start_program([main_1, main_2])
