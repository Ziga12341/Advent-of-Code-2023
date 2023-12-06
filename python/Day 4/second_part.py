from collections import defaultdict

small = "small_input.txt"
whole_input = "input.txt"
with open(whole_input, "r", encoding="utf-8") as file:
    winning_copies = defaultdict(int)
    winning_initial = defaultdict(int)
    for line in file:
        card_id, game = line.strip().split(":")
        winning_cards, my_cards = "".join(game).split("|")
        winning_cards = "".join(winning_cards).strip().split(" ")
        my_cards = "".join(my_cards).strip().split(" ")
        winning_cards = {card for card in winning_cards if card != ""}
        my_cards = {card for card in my_cards if card != ""}
        wins = my_cards & winning_cards
        # card_id = ("".join(card_id).strip(" ")[1])
        card_id = int(card_id.split(" ")[-1])
        winning_copies[card_id] = len(wins)
        winning_initial[card_id] = 1

    from collections import defaultdict


    def apply_impact(game_id_and_wins, global_dict):
        keys = list(game_id_and_wins.keys())
        for i in range(len(keys)):
            game_id = keys[i]
            impact = global_dict[game_id]
            # Apply impact to subsequent games based on current game's wins
            for j in range(i + 1, min(i + game_id_and_wins[game_id] + 1, len(keys))):
                next_game_id = keys[j]
                global_dict[next_game_id] += impact

    apply_impact(winning_copies, winning_initial)

    print(sum(winning_initial.values()))

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

# right answer: 6857330