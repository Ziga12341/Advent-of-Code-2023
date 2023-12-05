def add_dots(engine):
    first_last_line = ["." * (len(engine[0]) + 2)]
    new_engine = [f".{row}." for row in engine]
    return first_last_line + new_engine + first_last_line


# you need to add dots over input... to avoid index out of range
small = "small_input.txt"
whole_input = "input.txt"
with open(whole_input, "r", encoding="utf-8") as file:
    engine2 = []
    for line in file:
        line_in_list = line.strip()
        engine2.append(line_in_list)
engine = add_dots(engine2)


def get_gear_location(engine):
    gears = []
    for y, engine_line in enumerate(engine):
        for x, char in enumerate(engine_line):
            if char == "*":
                gears.append((x, y))

    return gears


# get small grid 3 rows 7 columns
def get_small_grid(gear_location):
    # 4,2
    x, y = gear_location
    # limit for row
    row_limited_engine = engine[y - 1:y + 2]
    # limit around x - column
    limited_grid = [row[x - 3: x + 4] for row in row_limited_engine]
    return limited_grid

# if number not on edge... replace char with "."
# removing char (numbers) that do not count
def from_grid_to_number(small_grid):
    numbers = []
    for line in small_grid:
        if not line[2].isdigit() and not line[4].isdigit():
            line = "..." + line[3:4] + "..."
        if not line[2].isdigit():
            line = "..." + line[3:]
        if not line[4].isdigit():
            line = line[:4] + "..."
        if line[2].isdigit() and line[3].isdigit() and line[4].isdigit():
            line = ".." + line[2:5] + ".."
        if line[0].isdigit() and line[1].isdigit() and line[2].isdigit() and line[4].isdigit() and line[5].isdigit() and \
                line[6].isdigit():
            return [int(line[:3]), int(line[4:])]
        if line[1].isdigit() and line[2].isdigit() and line[4].isdigit() and line[5].isdigit() and line[6].isdigit():
            return [int(line[1:3]), int(line[4:])]
        if line[0].isdigit() and line[1].isdigit() and line[2].isdigit() and line[4].isdigit() and line[5].isdigit():
            return [int(line[:3]), int(line[4:6])]
        accumulator = ""
        for char in line:
            if char.isdigit():
                accumulator += char
            else:
                if accumulator != "":
                    accumulator = int(accumulator)
                    numbers.append(accumulator)
                    accumulator = ""
        if accumulator != "" and len(accumulator) != 1:
            numbers.append(int(accumulator))
    return numbers


def multiply_grid_numbers(small_grid):
    numbers = from_grid_to_number(small_grid)
    multiplication = 1

    assert len(numbers) == 2 or len(numbers) == 1, "Length of numbers not 1 not 2"
    if len(numbers) == 2:
        for number in numbers:
            multiplication *= number
    return multiplication


def main(engine):
    all_multiplied_numbers = []
    for x, y in get_gear_location(engine):
        small_grid = get_small_grid((x, y))  # this is string of 3 lines
        multiply = multiply_grid_numbers(small_grid)
        if multiply and multiply != 1:
            all_multiplied_numbers.append(multiply)
    return sum(all_multiplied_numbers)



print(main(engine))
# !!!! 81709807 !!!! right answer