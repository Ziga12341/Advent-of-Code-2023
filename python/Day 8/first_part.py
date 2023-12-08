import re
from collections import defaultdict

s = "small_input.txt"
b = "input.txt"


def left_right(file):
    with open(file, "r", encoding="utf-8") as file:
        return file.readlines()[0]  # --> sting


def convert_left_right_to_index(direction):
    # direction as string
    directions_in_index = []
    for l_r in direction:
        if l_r == "L":
            directions_in_index.append(0)
        if l_r == "R":
            directions_in_index.append(1)
    return directions_in_index


def convert_path_to_dict(file_input):
    path = defaultdict(tuple)
    with open(file_input, "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            if i > 1:
                pattern = r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)"
                # Match the pattern
                match = re.match(pattern, line)
                # Extract where_to and from_to
                where_to = match.group(1)
                from_to = (match.group(2), match.group(3))
                path[where_to] = from_to

    return path


def walk(path, directions):
    steps = 0
    start = "AAA"
    finish = "ZZZ"
    count_while_loop = 0
    while start != finish:
        for direction in directions:
            if start == finish:
                return steps
            else:
                start = path[start][direction]
                steps += 1
        count_while_loop += 1
    return steps


indexed_directions = (convert_left_right_to_index(left_right(b)))
path = (convert_path_to_dict(b))

print(walk(path, indexed_directions))