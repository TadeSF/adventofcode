import math
import sys
import time
from typing import List, Tuple
from misc import start_program

class Instruction:
    def __init__(self, origin: str, nodes: List[str]) -> None:
        self.origin: str = origin
        self.left, self.right = nodes
        
        self.is_start: bool = self.origin.endswith("A")
        
    def get_left_node(self):
        return self.left
    
    def get_right_node(self):
        return self.right
    
class Path:
    def __init__(self, directions: str, map: List[Instruction], current_node: str) -> None:
        self.directions: str = directions
        self.map: List[Instruction] = map
        
        self.current_node: str = current_node
        self.current_direction_index: int = 0
        
    def search_next_step(self):
        for instruction in self.map:
            if instruction.origin != self.current_node:
                continue
            
            if self.directions[self.current_direction_index] == "L":
                self.current_node = instruction.get_left_node()
            elif self.directions[self.current_direction_index] == "R":
                self.current_node = instruction.get_right_node()
            else:
                continue
            
            self.current_direction_index += 1
            if self.current_direction_index == len(self.directions):
                self.current_direction_index = 0
            break
        
    def is_end(self):
        return self.current_node.endswith("Z")
    
        
def parse_data(data: List[str]) -> Tuple[str, List[Instruction]]:
    map_with_instructions: List[Instruction] = []
    for index, line in enumerate(data):
        if index == 0:
            directions = line
            continue
        
        if line == "":
            continue
        
        splitline = line.split(" = ")
        map_with_instructions.append(Instruction(splitline[0], splitline[1].replace("(", "").replace(")", "").split(", ")))
    
    return directions, map_with_instructions
        
    
    
    
def main_1(data: List[str]):
    steps = 0
    
    directions, map_with_instructions = parse_data(data)

    path = Path(directions, map_with_instructions, "AAA")
    
    while path.current_node != "ZZZ":
        path.search_next_step()
        steps += 1
    print("Steps:", steps)


def main_2(data: List[str]):
    steps = 0
    pathways: List[Path] = []
    path_outcome_steps: List[int] = []

    directions, map_with_instructions = parse_data(data)
    
    for instruction in map_with_instructions:
        if instruction.is_start:
            pathways.append(Path(directions, map_with_instructions, instruction.origin))
    
    for path in pathways:
        while not path.is_end():
            path.search_next_step()
            steps += 1
        path_outcome_steps.append(steps)
        steps = 0
        
    print(math.lcm(*path_outcome_steps))
    
    

if __name__ == "__main__":
    start_program([main_1, main_2])