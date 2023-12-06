small = "small_input.txt"
whole_input = "input.txt"
with open(whole_input, "r", encoding="utf-8") as file:
    points = 0
    for line in file:
        card_id, game = line.strip().split(":")
        wining_cards, my_cards = "".join(game).split("|")
        wining_cards = "".join(wining_cards).strip().split(" ")
        my_cards = "".join(my_cards).strip().split(" ")
        wining_cards = {card for card in wining_cards if card != ""}
        my_cards = {card for card in my_cards if card != ""}
        wins = my_cards & wining_cards
        if len(wins) != 0 and wins != "":
            points += 2**(len(wins)-1)
    print(points)

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

# too high 41608
# right answer: 27454