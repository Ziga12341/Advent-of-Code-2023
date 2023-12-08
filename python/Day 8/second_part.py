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

# "NBA" : "BVZ" - 13939
# "SXA" : "VGZ" - 17621
# "JVA" : "VTZ" - 11309
# "XVA" : "BPZ" - 20777
# "AAA" : "ZZZ" - 19199
# "GRA" : "PSZ" - 15517


# do nort work as expected
def walk(path, directions):
    steps = 0
    start1 = "GRA"
    start2 = "AAA"
    start3 = "XVA"
    start4 = "JVA"
    start5 = "SXA"
    start6 = "NBA"

    finish1 = "PSZ"
    finish2 = "ZZZ"
    finish3 = "BPZ"
    finish4 = "VTZ"
    finish5 = "VGZ"
    finish6 = "BVZ"

    while True:
        for direction in directions:

            if start1 == finish1 and start2 == finish2 and start3 == finish3 and start4 == finish4 and start5 == finish5 and start6 == finish6:
                return steps
            else:
                start1 = path[start1][direction]
                start2 = path[start2][direction]
                start3 = path[start3][direction]
                start4 = path[start4][direction]
                start5 = path[start5][direction]
                start6 = path[start6][direction]

                steps += 1


def walk_2(path, directions, start, finish):
    steps = 0
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


def finish_simultaneously(walk_path, directions, starting_points, ending_points):
    all_possible = defaultdict(tuple)
    for starting_point in starting_points:
        for ending_point in ending_points:
            all_possible[starting_point] = (ending_point, walk_2(walk_path, directions, starting_point, ending_point))
    return all_possible


indexed_directions = (convert_left_right_to_index(left_right(b)))
path = (convert_path_to_dict(b))

starting_points = get_starting_points(path)
ending_points = get_ending_points(path)
# print(starting_points)
# print(ending_points)
#print(walk(path, indexed_directions))
# print(len(set(starting_points) | set(ending_points)) )
#finish_simultaneously(path, indexed_directions, starting_points, ending_points)

# "NBA" : "BVZ" - 13939
# "SXA" : "VGZ" - 17621
# "JVA" : "VTZ" - 11309
# "XVA" : "BPZ" - 20777
# "AAA" : "ZZZ" - 19199
# "GRA" : "PSZ" - 15517
# ['PSZ', 'VTZ', 'ZZZ', 'VGZ', 'BVZ', 'BPZ']
# ['PSZ', 'VTZ', 'ZZZ', 'VGZ', 'BVZ', 'BPZ']


# too low 11309

steps = [13939, 17621, 11309, 20777, 19199, 15517]

from math import gcd
#will work for an int array of any length
lcm = 1
for i in steps:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)