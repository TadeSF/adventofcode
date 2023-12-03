

class Elf:
    def __init__(self):
        self.calories = 0

    def eat(self, added_calories):
        self.calories += added_calories

    def get_calories(self):
        return self.calories
    

def main():
    elfs = [Elf()]

    with open('1_1.txt', 'r') as f:
        for line in f:
            if line != '\n':
                elfs[-1].eat(int(line.replace('\n', '')))
            else:
                elfs.append(Elf())

    calories = []
    for elf in elfs:
        calories.append(elf.get_calories())

    calories.sort()

    print(calories[-1] + calories[-2] + calories[-3])

main()