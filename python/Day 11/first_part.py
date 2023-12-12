import unittest
from collections import defaultdict

s = "small_input.txt"
l = "input.txt"


def read_lines(file):
    with open(file, "r", encoding="utf-8") as file:
        galaxy = []
        for line in file:
            line = line.strip()
            galaxy.append(line)
        return galaxy


def expand_universe_rows(galaxy):
    expanded_galaxy = []
    for line in galaxy:
        # if just "." in line add line next to it
        if set(line) == set("."):
            expanded_galaxy.append(line)
        expanded_galaxy.append(line)
    return expanded_galaxy


def index_all_dots_in_column_in_galaxy(galaxy):
    expanded_galaxy = []
    column_need_dot_index = []
    for column_index, line in enumerate(galaxy):
        if column_index == len(line) - 1:
            break
        column = ""
        remember_row_index = 0
        for row_index, char in enumerate(line):
            column += (galaxy[row_index][column_index])
            remember_row_index = column_index

        if set(column) == set("."):
            column_need_dot_index.append(remember_row_index)

    return column_need_dot_index


def insert_dot(galaxy, row_index):
    new_line = []
    for line in galaxy:
        new_line.append(line[:row_index] + "." + line[row_index:])
    return new_line


def create_expanded_galaxy(galaxy):
    new_galaxy = [galaxy]
    # expand galaxy by columns
    for i, row_index in enumerate(index_all_dots_in_column_in_galaxy(galaxy)):
        # was buggy - need to add to --> rows (index) that you already added to galaxy
        row_index = row_index + i
        new_galaxy.append(insert_dot(new_galaxy[-1], row_index))
    # expand galaxy by rows
    return expand_universe_rows(new_galaxy[-1])


def convert_galaxy_to_dict_with_location_and_number(universe):
    number = 1
    galaxies_locations_and_number = defaultdict(int)
    for y, line in enumerate(universe):
        for x, char in enumerate(line):
            if char == "#":
                galaxies_locations_and_number[(x, y)] = number
                number += 1
    return galaxies_locations_and_number


def from_coordinate_to_galaxy_number(universe, x, y):
    return convert_galaxy_to_dict_with_location_and_number(universe)[(x, y)]


def get_galaxies_locations(universe):
    # convert def convert_galaxy_to_dict_with_location_and_number(universe) - keys to values
    return {value: key for key, value in convert_galaxy_to_dict_with_location_and_number(universe).items()}


def calculate_path_between_galaxies(galaxy_location_1, galaxy_location_2):
    x0, y0 = galaxy_location_1
    x1, y1 = galaxy_location_2
    return abs(x1 - x0) + abs(y1 - y0)


def find_pairs(universe):
    all_pairs = set()
    all_galaxies = get_galaxies_locations(universe)
    for galaxy1 in all_galaxies:
        for galaxy2 in all_galaxies:
            # do not add if pair with different order already in set
            # do not include a pair of galaxies if galaxy itself
            if ((galaxy1, galaxy2) not in {pair[::-1] for pair in all_pairs}
                    and (galaxy1, galaxy2) not in {pair for pair in all_pairs}
                    and galaxy1 != galaxy2):
                all_pairs.add((galaxy1, galaxy2))
    return all_pairs


def calculate_all_paths(universe):
    counter = 0
    for galaxy1, galaxy2 in find_pairs(universe):
        galaxy_1_location = get_galaxies_locations(universe)[galaxy1]
        galaxy_2_location = get_galaxies_locations(universe)[galaxy2]
        counter += calculate_path_between_galaxies(galaxy_1_location, galaxy_2_location)
    return counter


universe_from_input = read_lines(l)
print(universe_from_input)
expanded_universe = create_expanded_galaxy(universe_from_input)
# expanded_universe_numbered = convert_hash_to_number(expanded_universe)
# print(expanded_universe_numbered)
galaxies_locations = convert_galaxy_to_dict_with_location_and_number(expanded_universe)
print(galaxies_locations)
# print("galaxies_locations[0]", galaxies_locations[0])
# print(find_pairs(expanded_universe_numbered))
# print(char_from_coordinate(expanded_universe_numbered, 9, 10))
#
print(calculate_all_paths(expanded_universe))


# you should go just x-x0 and y-y0
# think how to calculate... from dx and dy
# 1530 too low

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.universe_from_input = read_lines(s)
        self.expanded_universe = create_expanded_galaxy(self.universe_from_input)
        self.expanded_universe_numbered = convert_galaxy_to_dict_with_location_and_number(self.expanded_universe)
        self.galaxies_locations = get_galaxies_locations(self.expanded_universe)

    def test_convert_galaxy_to_dict_with_location_and_number(self):
        self.assertIn((9, 10), convert_galaxy_to_dict_with_location_and_number(self.expanded_universe))

    def test_from_coordinate_to_galaxy_number(self):
        self.assertEqual(from_coordinate_to_galaxy_number(self.expanded_universe, 4, 0), 1, "Should be 1")
        self.assertEqual(from_coordinate_to_galaxy_number(self.expanded_universe, 9, 1), 2, "Should be 2")
        self.assertEqual(from_coordinate_to_galaxy_number(self.expanded_universe, 0, 2), 3, "Should be 3")
        self.assertEqual(from_coordinate_to_galaxy_number(self.expanded_universe, 9, 10), 7, "Should be 7")

    def test_get_galaxies_location(self):
        self.assertEqual(get_galaxies_locations(self.expanded_universe)[1], (4, 0),
                         "Should get location of universe 1")
        self.assertEqual(get_galaxies_locations(self.expanded_universe)[3], (0, 2),
                         "Should get location of universe 3")
        self.assertEqual(get_galaxies_locations(self.expanded_universe)[6], (12, 7),
                         "Should get location of universe 6")

    def test_calculate_path_between_galaxies(self):
        self.assertEqual(calculate_path_between_galaxies((5, 1), (10, 2)), 6, "Should be 6")
        # galaxy location is stored in dict --> key "3" return location fo galaxy "3"
        self.assertEqual(
            calculate_path_between_galaxies(self.galaxies_locations[3], self.galaxies_locations[6]), 17,
            "Should be 17")
        self.assertEqual(
            calculate_path_between_galaxies(self.galaxies_locations[8], self.galaxies_locations[9]), 5,
            "Should be 5")

    def test_find_number_of_pairs(self):
        self.assertEqual(len(find_pairs(self.expanded_universe)), 36, "you should have 36 pairs")
        self.assertIn((1, 2), (find_pairs(self.expanded_universe)), "galaxy ('1','2') not in pairs ")

    def test_calculate_all_paths(self):
        self.assertEqual(calculate_all_paths(self.expanded_universe), 374,
                         "the sum of the shortest path between all 36 pairs of galaxies is NOT 374")


if __name__ == '__main__':
    unittest.main()