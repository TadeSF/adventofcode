

class Game:
    def __init__(self, line):
        self.line = line
        self.id = None
        self.red = []
        self.green = []
        self.blue = []
        self.parse_line()

    def parse_line(self):
        id_with_game, all_results = self.line.split(':')
        self.id = int(id_with_game.split(' ')[1].strip())

        raw_results = all_results.split(':')

        for result in raw_results:
            result = result.replace('\n', '').strip()
            single_result = result.split(';')
            for single in single_result:
                single = single.strip()
                for color in single.split(','):
                    color = color.strip()
                    if 'red' == color.split(' ')[1].strip():
                        new_red = color.split(' ')[0].strip()
                        self.red.append(new_red)
                    elif 'green' == color.split(' ')[1].strip():
                        new_green = color.split(' ')[0].strip()
                        self.green.append(new_green)
                    elif 'blue' == color.split(' ')[1].strip():
                        new_blue = color.split(' ')[0].strip()
                        self.blue.append(new_blue)

    def get_id(self):
        return self.id
    
    def check_red(self, max_red):
        for red in self.red:
            if int(red) > max_red:
                return False
        return True
    
    def check_green(self, max_green):
        for green in self.green:
            if int(green) > max_green:
                return False
        return True
    
    def check_blue(self, max_blue):
        for blue in self.blue:
            if int(blue) > max_blue:
                return False
        return True
    
    def check_all(self, max_red, max_green, max_blue):
        if self.check_red(max_red) and self.check_green(max_green) and self.check_blue(max_blue):
            return True
        return False
    
    def get_max_red(self):
        max_red = 0
        for red in self.red:
            if int(red) > max_red:
                max_red = int(red)
        return max_red
    
    def get_max_green(self):
        max_green = 0
        for green in self.green:
            if int(green) > max_green:
                max_green = int(green)
        return max_green
    
    def get_max_blue(self):
        max_blue = 0
        for blue in self.blue:
            if int(blue) > max_blue:
                max_blue = int(blue)
        return max_blue
    
    def get_max_all(self) -> tuple:
        return self.get_max_red(), self.get_max_green(), self.get_max_blue()
    

def main_task_1():
    with open('2.txt', 'r') as f:
        games = []
        for line in f:
            games.append(Game(line))
        
        max_red = 12
        max_green = 13
        max_blue = 14

        id_sum = 0

        for game in games:
            if game.check_all(max_red, max_green, max_blue):
                id_sum += game.get_id()

        print(id_sum)


def main_task_2():
    with open('2.txt', 'r') as f:
        games = []
        for line in f:
            games.append(Game(line))

    power_sum = 0
    for game in games:
        red, green, blue = game.get_max_all()
        power_sum += red * green * blue

    print(power_sum)


main_task_2()