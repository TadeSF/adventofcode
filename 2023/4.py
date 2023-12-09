import math
import re

from misc import start_program


cards = []

def check_card(winning_numbers: list, my_numbers: list) -> list:
    card_winners = []
    for number in my_numbers:
        if number in winning_numbers:
            card_winners.append(number)
    return card_winners

class Card:
    def __init__(self, raw_card: str):
        self.id = int(re.search(r"\d+", raw_card.split(":")[0]).group())
        self.raw_card = raw_card
        self.winning_numbers = []
        self.my_numbers = []
        self.card_winners = []

        self.number_copies = 1
        
        self.parse_card()


    def parse_card(self):
        raw_data = self.raw_card.split(":")[1]
        self.winning_numbers = raw_data.split("|")[0].split(" ")
        self.my_numbers = raw_data.split("|")[1].split(" ")

        self.winning_numbers = list(filter(lambda x: x != "", self.winning_numbers))
        self.my_numbers = list(filter(lambda x: x != "", self.my_numbers))

        self.card_winners = check_card(self.winning_numbers, self.my_numbers)


    def calculate_score(self):
        return math.floor(2 ** (len(self.card_winners) - 1))
    
    def get_copy_id_list(self):
        return list(map(lambda x: self.card_winners.index(x) + self.id + 1, self.card_winners))
    
    def add_copies(self, number_copies: int):
        self.number_copies += number_copies

    def get_number_copies(self):
        return self.number_copies

def main_1(data):
    for line in data:
        cards.append(Card(line))
    
    sum_points = 0
    for card in cards:
        sum_points += card.calculate_score()
    print(sum_points)


def main_2(data):
    for line in data:
        cards.append(Card(line))

    sum_cards = 0

    for card in cards:
        print(f"Card: {card.id}, Copies: {card.get_number_copies()}")
        for copy_id in card.get_copy_id_list():
            for original_card in cards:
                if original_card.id == copy_id:
                    original_card.add_copies(card.get_number_copies())
                    break

    for card in cards:
        sum_cards += card.get_number_copies()


    print(sum_cards)


if __name__ == "__main__":
    start_program([main_1, main_2])