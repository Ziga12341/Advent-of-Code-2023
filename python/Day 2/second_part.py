small = "small_input.txt"
whole_input = "input.txt"
with (open(whole_input, "r", encoding="utf-8") as file):
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    total = 0
    for line in file:
        game_info, bag_info = line.strip().split(": ")
        game_id = int(game_info.split(" ")[1])
        bags_in_sets = bag_info.split("; ")

        biggest_green = 0
        biggest_blue = 0
        biggest_red = 0
        for bag_set in bags_in_sets:
            cubes_in_bag = []
            list_of_all_cubes = bag_set.split(", ")
            for one_cube in list_of_all_cubes:
                cube_value, cube_colour = one_cube.split(" ")
                cube_value = int(cube_value)
                cubes_in_bag.append((cube_value, cube_colour))
                if cube_colour == "green":
                    if cube_value > biggest_green:
                        biggest_green = cube_value

                if cube_colour == "red":
                    if cube_value > biggest_red:
                        biggest_red = cube_value

                if cube_colour == "blue":
                    if cube_value > biggest_blue:
                        biggest_blue = cube_value

        power = biggest_blue * biggest_green * biggest_red
        total += power
print(total)