small = "small_input.txt"
whole_input = "input.txt"


# remember bid and cards
# chang letters do number of cards

# ranking card based on other cards in the biggest challenge
# create dict with groups of each type - each hand has one type
# order hands in one group and append to list, from group with the highest rank the lowest


# get hand rank
# sum all hand * rank

def card_to_digit(card):
    if card.isdigit():
        return int(card)
    elif card in card_mapper:
        return card_mapper[card]


def hand_and_bid_into_tuple(file):
    with open(small, "r", encoding="utf-8") as file:
        hand_with_bid = []
        for line in file:
            hand, bid = line.strip().split(" ")
            hand_in_digit = []
            for card in hand:
                hand_in_digit.append(card_to_digit(card))
            hand_with_bid.append((hand_in_digit, int(bid)))
    return hand_with_bid


card_mapper = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483

print(hand_and_bid_into_tuple(small))
hands_with_bid = hand_and_bid_into_tuple(small)


def unique_numbers_in_list(list):
    return len(set(list)) == len(list)


def two_numbers_the_same_in_list(list):
    # print(list)
    # print(len(list))
    return len(set(list)) + 1 == len(list)


# print(two_numbers_the_same_in_list([3, 2, 10, 3, 13]))


def three_different_numbers_the_same_in_list(list_of_cards_in_hand):  # can be three i a kind or two pair
    return len(set(list_of_cards_in_hand)) + 2 == len(list_of_cards_in_hand)


def two_different_numbers_in_list(list_of_cards_in_hand):  # two numbers equal - can be full house or 4 of a kind
    return len(set(list_of_cards_in_hand)) + 3 == len(list_of_cards_in_hand)


def all_numbers_the_same_in_list(list_of_cards_in_hand):
    return len(set(list_of_cards_in_hand)) + 4 == len(list_of_cards_in_hand)

def is_four_of_a_kind(list_of_cards_in_hand):
    two_numbers = list(set(list_of_cards_in_hand))
    first = two_numbers[0]
    second = two_numbers[1]
    return list_of_cards_in_hand.count(first) == 4 or list_of_cards_in_hand.count(second) == 4

def is_three_of_a_kind(list_of_cards_in_hand):
    # needs to have exactly 3 different cards in hand
    three_numbers = list(set(list_of_cards_in_hand))
    first = three_numbers[0]
    second = three_numbers[1]
    third = three_numbers[2]
    return list_of_cards_in_hand.count(first) == 3 or list_of_cards_in_hand.count(
        second) == 3 or list_of_cards_in_hand.count(third) == 3

def rank_hands(hands_with_bid):
    ranking_hands = {
        "five of a kind": [],
        "four of a kind": [],
        "full house": [],
        "three of a kind": [],
        "two pair": [],
        "one pair": [],
        "high card": [],

    }
    for hand_in_list, bid in hands_with_bid:
        assert len(hand_in_list) == 5, "not valid game/hand_in_list"
        # hand_in_list = hand_in_list
        # print(len(hand_in_list))
        # print(len(set(hand_in_list)))
        if unique_numbers_in_list(hand_in_list):
            ranking_hands["high card"].append((hand_in_list, bid))

        elif two_numbers_the_same_in_list(hand_in_list):
            ranking_hands["one pair"].append((hand_in_list, bid))

        elif two_different_numbers_in_list(hand_in_list):
            # could be 4 of a kind or full house
            # write function is for of a kind
            if is_four_of_a_kind(hand_in_list):
                ranking_hands["four of a kind"].append((hand_in_list, bid))
            # is full house
            else:
                ranking_hands["full house"].append((hand_in_list, bid))

        elif all_numbers_the_same_in_list(hand_in_list):
            ranking_hands["five of a kind"].append((hand_in_list, bid))

        elif three_different_numbers_the_same_in_list(hand_in_list):
            # could be two pairs or three of a kind
            if is_three_of_a_kind(hand_in_list):
                ranking_hands["three of a kind"].append((hand_in_list, bid))

            # two pairs
            else:
                ranking_hands["two pair"].append((hand_in_list, bid))


        else:
            print("should be empty")

    return ranking_hands


print(rank_hands(hands_with_bid))
print(rank_hands([([3, 2, 10, 3, 13], 765), ([3, 3, 3, 33, 33], 622), ([1, 1, 1, 1, 1], 6000), ([13, 2, 10, 3, 1], 76522), ([3, 3, 3, 3, 43], 76),([3, 3, 3, 33, 43], 6), ([10, 5, 5, 11, 5], 684), ([13, 13, 6, 7, 7], 28), ([13, 10, 11, 11, 10], 220), ([12, 12, 12, 11, 12], 483)]))

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456