# you need to add dots over input... to avoid index otu of range
def add_dots(engine):
    first_last_line = ["." * (len(engine[0]) + 2)]
    new_engine = [f".{row}." for row in engine]
    return first_last_line + new_engine + first_last_line

small = "small_input.txt"
whole_input = "input.txt"
with (open(whole_input, "r", encoding="utf-8") as file):
    engine2 = []
    for line in file:
        line_in_list = line.strip()
        engine2.append(line_in_list)
engine = add_dots(engine2)
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
    dx, dy = directions[direction]
    char_in_new_position = engine[y + dy][x + dx]
    # check if special char in new position
    return not char_in_new_position.isalnum() and char_in_new_position != "."
# print(is_valid_char(engine, 3, 2, 0, -1)) # --> 5 - *
# print(is_valid_char_in_direction(engine, directions, 2, 0, "RD"))  # --> True

def is_valid_all_directions(engine, directions, x, y):
    return any(is_valid_char_in_direction(engine, directions, x, y, direction) for direction in directions)


# figure out where is one number - index of one number
# check if digits
list_of_numbers = []
accumulator = ""
valid_char = []
for x, engine_line in enumerate(engine):
    for y, char in enumerate(engine_line):

        if char.isdigit():
            # make sure you change x , y!
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
print(sum(list_of_numbers))