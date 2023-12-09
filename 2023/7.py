from enum import Enum
from typing import Tuple
import sys

from misc import start_program

class Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


if sys.argv[2] == "main_1":
    possible_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
elif sys.argv[2] == "main_2":
    possible_cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


class Hand:
    def __init__(self, cards: list, bid: int, part_2=False) -> None:
        self.cards = cards
        self.bid = bid
        self.part_2 = part_2
        self.type: Type = self.get_type()

    def get_type(self) -> Type:
        five_of_a_kind = self.is_n_of_a_kind(5)
        four_of_a_kind = self.is_n_of_a_kind(4)
        three_of_a_kind = self.is_n_of_a_kind(3)
        two_of_a_kind = self.is_n_of_a_kind(2)

        if five_of_a_kind:
            return Type.FIVE_OF_A_KIND
        elif four_of_a_kind:
            return Type.FOUR_OF_A_KIND
        elif self.is_full_house():
            return Type.FULL_HOUSE
        elif three_of_a_kind:
            return Type.THREE_OF_A_KIND
        elif self.is_two_pairs():
            return Type.TWO_PAIRS
        elif two_of_a_kind:
            return Type.ONE_PAIR
        else:
            return Type.HIGH_CARD

    def is_n_of_a_kind(self, n: int) -> bool:
        card_count = self._get_card_count()
        for card, count in card_count.items():
            if self.part_2 and card == "J" and card_count.get("J", 0) != 5:
                continue
            if count == n or (self.part_2 and count + card_count.get("J", 0) == n):
                return True
        return False

    def is_full_house(self) -> bool:
        card_count = self._get_card_count()
        if not self.part_2 or "J" not in card_count.keys():
            return len(card_count.keys()) == 2 and 3 in card_count.values()
        else:
            return sum(1 for count in card_count.values() if count == 2) == 2

    def is_two_pairs(self) -> bool:
        card_count = self._get_card_count()
        pairs = sum(1 for count in card_count.values() if count == 2)
        return pairs == 2 or (pairs == 1 and self.part_2 and "J" in card_count.keys())

    def _get_card_count(self) -> dict:
        card_count = {}
        for card in self.cards:
            card_count[card] = card_count.get(card, 0) + 1
        return card_count

    def card_score(self, index: int) -> int:
        return possible_cards.index(self.cards[index])

    def calc_hand_score(self, rank: int) -> int:
        return self.bid * rank


def main_1(data):
    global hands
    for line in data:
        cards, bid = line.split(" ")
        hands.append(Hand([cards[0], cards[1], cards[2], cards[3], cards[4]], int(bid)))


def main_2(data):
    global hands
    for line in data:
        cards, bid = line.split(" ")
        hands.append(
            Hand(
                [cards[0], cards[1], cards[2], cards[3], cards[4]],
                int(bid),
                part_2=True,
            )
        )


if __name__ == "__main__":
    hands = []

    start_program([main_1, main_2])

    sorted_hands = sorted(
        hands,
        key=lambda hand: (
            hand.type.value,
            hand.card_score(0),
            hand.card_score(1),
            hand.card_score(2),
            hand.card_score(3),
            hand.card_score(4),
        ),
        reverse=False,
    )

    hands_score_sum = 0
    for hand in sorted_hands:
        print(hand.cards, hand.type, hand.calc_hand_score(sorted_hands.index(hand) + 1))
        hands_score_sum += hand.calc_hand_score(sorted_hands.index(hand) + 1)

    print(hands_score_sum)
