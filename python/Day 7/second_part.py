from collections import defaultdict
from operator import itemgetter

small = "small_input.txt"
whole_input = "input.txt"
card_mapper = {
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14
}


# remember bid and cards
# change letters to number of cards (hands)
# ranking card based on other cards in the biggest challenge
# create dict with groups of each type - each hand has one type
# order hands in one group and append to list, from group with the lowest rank the highest

# get hand rank
# sum all hand * rank

def card_to_digit(card):
    if card.isdigit():
        return int(card)
    elif card in card_mapper:
        return card_mapper[card]


def hand_and_bid_into_tuple(file_input):
    with open(file_input, "r", encoding="utf-8") as file:
        hand_with_bid = []
        for line in file:
            hand, bid = line.strip().split(" ")
            hand_in_digit = []
            for card in hand:
                hand_in_digit.append(card_to_digit(card))
            hand_with_bid.append((hand_in_digit, int(bid)))
    return hand_with_bid


def unique_numbers_in_list(list):
    return len(set(list)) == len(list)


def two_numbers_the_same_in_list(list):
    return len(set(list)) + 1 == len(list)


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


def count_cards_in_hand(hand):
    hand_in_dict = defaultdict(int)
    for card in hand:
        hand_in_dict[card] += 1
    return hand_in_dict


# J cards can pretend to be whatever card is best for the purpose of determining hand type

# {11: 1, 12: 3, 14: 1} --> [11, 12, 12, 12, 14]
def from_counter_dict_to_list(hand_counter_dict):
    hand_in_list = []
    for card, counter in hand_counter_dict.items():
        for i in range(counter):
            hand_in_list.append(card)
    return hand_in_list


def find_best_card_and_its_counter_without_joker(hand_in_dict):
    max_counter = 0
    max_counter_card = int
    for card, counter in hand_in_dict.items():
        # remove joker
        if card != 1:
            # find card with most the same cards in one hand
            if counter > max_counter:
                max_counter = counter
                max_counter_card = card
    return max_counter_card, max_counter


def change_joker_to_best_card(hand):
    hand_in_list = hand
    unique_cards_in_hand = set(hand)
    count_jokers = hand_in_list.count(1)
    # if only jokers return jokers
    if count_jokers == 5:
        return hand
    hand_in_dict = count_cards_in_hand(hand)  # -->  {4: 1, 1: 2, 2: 2} loop over
    best_card, its_counter = find_best_card_and_its_counter_without_joker(
        hand_in_dict)  # number that represent best card (4, 2)
    # change hand so that you add joker to best card
    enhanced_hand_with_joker = [best_card] * (its_counter + count_jokers)

    for card, counter in hand_in_dict.items():
        # if not best card and if not joker ---> append all others cards
        if card != best_card and card != 1:
            for i in range(counter):
                enhanced_hand_with_joker.append(card)

    return enhanced_hand_with_joker


def hands_to_category(hands_with_bid):
    # lowest to highest
    ranking_hands = {
        "high card": [],
        "one pair": [],
        "two pair": [],
        "three of a kind": [],
        "full house": [],
        "four of a kind": [],
        "five of a kind": [],

    }
    for hand_in_list, bid in hands_with_bid:
        assert len(hand_in_list) == 5, "not valid game/hand_in_list"
        enhanced_hand_in_list = change_joker_to_best_card(hand_in_list)
        # print(len(hand_in_list))
        # print(len(set(hand_in_list)))

        if unique_numbers_in_list(enhanced_hand_in_list):
            ranking_hands["high card"].append((hand_in_list, bid))

        elif two_numbers_the_same_in_list(enhanced_hand_in_list):
            ranking_hands["one pair"].append((hand_in_list, bid))

        elif two_different_numbers_in_list(enhanced_hand_in_list):
            # could be 4 of a kind or full house
            # write function is for of a kind
            if is_four_of_a_kind(enhanced_hand_in_list):
                ranking_hands["four of a kind"].append((hand_in_list, bid))
            # is full house
            else:
                ranking_hands["full house"].append((hand_in_list, bid))

        elif all_numbers_the_same_in_list(enhanced_hand_in_list):
            ranking_hands["five of a kind"].append((hand_in_list, bid))

        elif three_different_numbers_the_same_in_list(enhanced_hand_in_list):
            # could be two pairs or three of a kind
            if is_three_of_a_kind(enhanced_hand_in_list):
                ranking_hands["three of a kind"].append((hand_in_list, bid))

            # two pairs
            else:
                ranking_hands["two pair"].append((hand_in_list, bid))

        else:
            # should not go there
            print("should be empty")

    return ranking_hands


def reorder_hands_in_category(list_of_hands_in_category):
    return sorted(list_of_hands_in_category, key=itemgetter(0))


def collect_ordered_categories(categories):
    # dict of category
    ranked_ordered_hands = []
    for category_name, list_of_hands_with_bid_in_category in categories.items():
        if list_of_hands_with_bid_in_category:
            ordered_list_of_hands = reorder_hands_in_category(list_of_hands_with_bid_in_category)
            for ordered_hands in ordered_list_of_hands:
                ranked_ordered_hands.append(ordered_hands)
    return (ranked_ordered_hands)


def calculate_total_winnings(rank_ordered_hands):
    sumaraza = 0
    for i, hand_with_bid in enumerate(rank_ordered_hands):
        rank = i + 1
        hand, bid = hand_with_bid
        sumaraza += rank * bid
    return sumaraza


hands_with_bid = hand_and_bid_into_tuple(whole_input)
categories = hands_to_category(hands_with_bid)
ranked = (collect_ordered_categories(categories))
hands_with_bid = hand_and_bid_into_tuple(whole_input)

print(calculate_total_winnings(ranked))