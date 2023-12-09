import re
from collections import defaultdict
from math import gcd

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


def walk(path, directions, start, finish):
    steps = 0
    count_while_loop = 0
    while start != finish:
        # point!
        if steps > 40000:
            break
        for direction in directions:
            if start == finish:
                return steps
            else:
                start = path[start][direction]
                steps += 1
        count_while_loop += 1
    return steps


def finish_simultaneously(walk_path, directions, starting_points, ending_points):
    all_possible = defaultdict(list)
    for starting_point in starting_points:
        for ending_point in ending_points:
            all_possible[starting_point].append(
                (ending_point, walk(walk_path, directions, starting_point, ending_point)))
    return all_possible


def find_min_steps_in_all_possible_paths(dict_possible_collections):
    start_finish_steps_in_list = []
    for start, possible_finish_with_steps in dict_possible_collections.items():
        min = float('inf')  # number bigger than all others
        min_finish_name = ""
        for finish, steps in possible_finish_with_steps:
            if steps < min:
                min = steps
                min_finish_name = finish
        start_finish_steps_in_list.append((start, min_finish_name, min))
    return start_finish_steps_in_list


def steps_only(start_finish_steps):
    return [steps for start, finish, steps in start_finish_steps]


def greatest_common_divider(list_of_steps):
    # find the greatest common divider
    lcm = 1
    for i in list_of_steps:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


indexed_directions = (convert_left_right_to_index(left_right(b)))
path = (convert_path_to_dict(b))
starting_points = get_starting_points(path)
ending_points = get_ending_points(path)
dict_all_valid = (finish_simultaneously(path, indexed_directions, starting_points, ending_points))
start_finish_steps = find_min_steps_in_all_possible_paths(dict_all_valid)
steps = steps_only(start_finish_steps)

print("Part 1: ", walk(path, indexed_directions, "AAA", "ZZZ"))
print("Part 2: ", greatest_common_divider(steps))

# "NBA" : "BVZ" - 13939
# "SXA" : "VGZ" - 17621
# "JVA" : "VTZ" - 11309
# "XVA" : "BPZ" - 20777
# "AAA" : "ZZZ" - 19199
# "GRA" : "PSZ" - 15517
# ['PSZ', 'VTZ', 'ZZZ', 'VGZ', 'BVZ', 'BPZ']
# ['PSZ', 'VTZ', 'ZZZ', 'VGZ', 'BVZ', 'BPZ']