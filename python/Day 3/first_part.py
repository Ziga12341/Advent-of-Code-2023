# you need to add dots over input... to avoid index otu of range
small = "small_input.txt"
whole_input = "input.txt"
with (open(whole_input, "r", encoding="utf-8") as file):
    engine = []
    for line in file:
        line_in_list = line.strip()
        engine.append(line_in_list)

# L - left
# R - right
# D - down
# U - up
# LD - left down
# RD - right down
# LU - left up
# RU - right up

directions = {
    "L": (-1, 0),
    "R": (1, 0),
    "D": (0, 1),
    "U": (0, -1),
    "LD": (-1, 1),
    "RD": (1, 1),
    "LU": (-1, -1),
    "RU": (1, -1),

}


def is_valid_char_in_direction(engine, directions, x, y, direction):
    # index all numbers... go left right diagoneale for each number end check if ther is any symbole
    # right down diagonale - df +(1,1)
    # function that checks if is valid number
    # dx, dy = 1 ,1 RightDown - diagonale
    dx, dy = directions[direction]
    # print(engine[y][x])
    # print(engine[y + dy][x + dx])
    char_in_new_position = engine[y + dy][x + dx]
    # print(char_in_new_position)
    # if char_in_new_position.isdigit():
    #     print("is didgit")
    # if char_in_new_position.isalnum():
    #     print("is alnum")
    # if char_in_new_position == ".":
    #     print("is .")
    # if char_in_new_position == "*":
    #     print("is *")
    # check if special char in new position
    return not char_in_new_position.isalnum() and char_in_new_position != "."


# print(is_valid_char(engine, 2, 0, 1,1)) # --> 7 - *
# print(is_valid_char(engine, 3, 2, 0, -1)) # --> 5 - *
print(is_valid_char_in_direction(engine, directions, 2, 0, "RD"))  # --> True
print(is_valid_char_in_direction(engine, directions, 1, 9, "RD"))  # --> True


def is_valid_all_directions(engine, directions, x, y):
    return any(is_valid_char_in_direction(engine, directions, x, y, direction) for direction in directions)


print(is_valid_all_directions(engine, directions, 2, 0))
print(is_valid_all_directions(engine, directions, 0, 0))

# figure out where is one number - index of one number
# check if digits
list_of_numbers = []
accumulator = ""
valid_char = []
for x, engine_line in enumerate(engine):
    for y, char in enumerate(engine_line):

        if char.isdigit():
            print((char, (y, x)))
            print(is_valid_all_directions(engine, directions, y, x))
            valid_char.append(is_valid_all_directions(engine, directions, y, x))
            accumulator += char
        else:
            if accumulator != "":
                # I need to figure out how to check if a valid number and only   if valid append it to list

                accumulator = int(accumulator)
                if any(valid_char):
                    list_of_numbers.append(accumulator)

            accumulator = ""
            valid_char = []
print(accumulator)
print(list_of_numbers)
print(sum(list_of_numbers))

# you need to know coordinates for each digit in number and if all digit pass conditions than append number to list

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
print(is_valid_all_directions(engine, directions, 9, 6))