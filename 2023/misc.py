# misc.py:
import sys 
from typing import List, NoReturn


def start_program(main_functions: List[NoReturn]):
    if len(sys.argv) < 3:
        print("Missing second argument (task_number): 1 or 2\npython3 8.py <input_file> <task_number>")

    with open(f"data/{sys.argv[1]}") as file:
        data = [line.replace("\n", "").strip() for line in file.readlines()]

    for index, function in enumerate(main_functions):
        if sys.argv[2] == str(index + 1):
            function(data)
            break