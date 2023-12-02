small = "small_input.txt"
whole_input = "input.txt"
with (open(whole_input, "r", encoding="utf-8") as file):
    # how to parse/ structure data?
    # one line one game if valid/met condition than i need to remember id of game (int)
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    # for game split " " take second list convert to int

    # how to save data that i will easily use
    # split with ; and put into tuple (3, "blue")
    counter = 0
    games = []
    for line in file:
        game_info, bag_info = line.strip().split(": ")
        game_id = int(game_info.split(" ")[1])
        # add game id in games list
        bags_in_sets = bag_info.split("; ")

        for bag_set in bags_in_sets:
            list_of_all_cubes = bag_set.split(", ")
            for one_cube in list_of_all_cubes:
                cube_value, cube_colour = one_cube.split(" ")
                cube_value = int(cube_value)
                if (cube_colour == "red" and cube_value > 12) or \
                        (cube_colour == "green" and cube_value > 13) or \
                        (cube_colour == "blue" and cube_value > 14):
                    break
            else:
                continue
            break
        else:
            counter += game_id
            games.append(game_id)

print("counter", counter)
# condition if it is "valid" possible games
# ... if bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes
# ... check if there is less or equal than 12 red cubes, 13 green cubes, and 14 blue cubes showed to you in one set of game


# sum ids of games if condition met

# 3366 is to high
# 3670 is to high
# small right answer: 8
# 2204 is right answer