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


def get_starting_points(path_dict):
    return [path for path in path_dict.keys() if path[-1] == "A"]


def get_ending_points(path_dict):
    return [path for path in path_dict.keys() if path[-1] == "Z"]


# ['NBA', 'SXA', 'JVA', 'XVA', 'AAA', 'GRA']
# ['PSZ', 'VTZ', 'ZZZ', 'VGZ', 'BVZ', 'BPZ']
def walk(path, directions):
    steps = 0
    start1 = "GRA"
    start2 = "AAA"
    start3 = "XVA"
    start4 = "JVA"
    start5 = "SXA"
    start6 = "NBA"
    finish = ['PSZ', 'VTZ', 'ZZZ', 'VGZ', 'BVZ', 'BPZ']
    while True:
        for direction in directions:
            starting_points = set()
            starting_points.add(start1)
            starting_points.add(start2)
            starting_points.add(start3)
            starting_points.add(start4)
            starting_points.add(start5)
            starting_points.add(start6)
            # print(starting_points)
            # print(finish)
            # print("presek", set(starting_points) & set(finish))
            if len(set(starting_points) | set(finish)) == 6:
                return steps
            else:
                start1 = path[start1][direction]
                start2 = path[start2][direction]
                start3 = path[start3][direction]
                start4 = path[start4][direction]
                start5 = path[start5][direction]
                start6 = path[start6][direction]

                steps += 1


def finish_simultaneously():
    ...


indexed_directions = (convert_left_right_to_index(left_right(b)))
path = (convert_path_to_dict(b))

starting_points = get_starting_points(path)
ending_points = get_ending_points(path)
# print(starting_points)
# print(ending_points)
print(walk(path, indexed_directions))
# print(len(set(starting_points) | set(ending_points)) )

# too low 11309