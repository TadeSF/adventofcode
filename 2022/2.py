

class GameResult:
    win = 6
    draw = 3
    lose = 0

    rock = 1
    paper = 2
    scissors = 3


    def __init__(self, opponent, player) -> None:
        self.opponent = opponent
        self.player = player

        if self.player == "X":
            self.player = "A"
        elif self.player == "Y":
            self.player = "B"
        elif self.player == "Z":
            self.player = "C"
    
    def get_result(self):

        score = 0
        if self.opponent == self.player:
            score = GameResult.draw
        
        elif self.opponent == "A":
            if self.player == "B":
                score = GameResult.win
            elif self.player == "C":
                score = GameResult.lose
        
        elif self.opponent == "B":
            if self.player == "A":
                score = GameResult.lose
            elif self.player == "C":
                score = GameResult.win

        elif self.opponent == "C":
            if self.player == "A":
                score = GameResult.win
            elif self.player == "B":
                score = GameResult.lose

        if self.player == "A":
            score += GameResult.rock
        elif self.player == "B":
            score += GameResult.paper
        elif self.player == "C":
            score += GameResult.scissors

        return score
    
def calculate_move(opponent, outcome):
    if outcome == "X":
        if opponent == "A":
            return "C"
        elif opponent == "B":
            return "A"
        elif opponent == "C":
            return "B"
        
    elif outcome == "Y":
        return opponent
    
    elif outcome == "Z":
        if opponent == "A":
            return "B"
        elif opponent == "B":
            return "C"
        elif opponent == "C":
            return "A"
        



def main_1():
    with open("2.txt", "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "").strip().split(" ") for line in lines]

        sum_score = 0

        for line in lines:
            opponent = line[0].strip()
            player = line[1].strip()

            game_result = GameResult(opponent, player)
            sum_score += game_result.get_result()

        print(sum_score)

def main_2():
    with open("2.txt", "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "").strip().split(" ") for line in lines]

        sum_score = 0

        for line in lines:
            opponent = line[0].strip()
            outcome = line[1].strip()

            player = calculate_move(opponent, outcome)

            game_result = GameResult(opponent, player)
            sum_score += game_result.get_result()

        print(sum_score)

main_2()
