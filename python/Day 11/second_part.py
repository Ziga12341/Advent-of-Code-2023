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


universe_from_small_input = read_lines(s)
universe_from_large_input = read_lines(l)


def expand_universe_rows(galaxy):
    expanded_galaxy = []
    for line in galaxy:
        # if just "." in line add line next to it
        if set(line) == set("."):
            expanded_galaxy.append(line)
        expanded_galaxy.append(line)
    return expanded_galaxy


def list_of_spaces_in_rows(universe):
    spaces_in_rows = []
    for i, line in enumerate(universe):
        # if just "." in line add line next to it
        if set(line) == set("."):
            spaces_in_rows.append(i)
    return spaces_in_rows


def list_of_spaces_in_column(universe):
    expanded_galaxy = []
    column_need_dot_index = []
    for column_index, line in enumerate(universe):
        if column_index == len(line) - 1:
            break
        column = ""
        remember_row_index = 0
        for row_index, char in enumerate(line):
            column += (universe[row_index][column_index])
            remember_row_index = column_index

        if set(column) == set("."):
            column_need_dot_index.append(remember_row_index)

    return column_need_dot_index


def lenght_with_spaces_between_galaxy(galaxy1, galaxy2, list_of_spaces, times_galaxy_space_expansion):
    space_counter = 0
    for space_index in list_of_spaces:
        if galaxy1 < space_index < galaxy2 or galaxy1 > space_index > galaxy2:
            space_counter += 1
    return space_counter * times_galaxy_space_expansion + (abs(galaxy1 - galaxy2))


def insert_dot(galaxy, row_index):
    new_line = []
    for line in galaxy:
        new_line.append(line[:row_index] + "." + line[row_index:])
    return new_line


def create_expanded_galaxy(galaxy):
    new_galaxy = [galaxy]
    # expand galaxy by columns
    for i, row_index in enumerate(list_of_spaces_in_column(galaxy)):
        # was buggy - need to add to --> rows (index) that you already added to galaxy
        row_index = row_index + i
        new_galaxy.append(insert_dot(new_galaxy[-1], row_index))
    # expand galaxy by rows
    return expand_universe_rows(new_galaxy[-1])


def convert_galaxy_to_dict_with_number_and_location(universe):
    number = 1
    galaxies_locations_and_number = defaultdict(tuple)
    for y, line in enumerate(universe):
        for x, char in enumerate(line):
            if char == "#":
                galaxies_locations_and_number[number] = x, y
                number += 1
    return galaxies_locations_and_number


def calculate_path_between_galaxies(galaxy_location_1, galaxy_location_2):
    x0, y0 = galaxy_location_1
    x1, y1 = galaxy_location_2
    return abs(x1 - x0) + abs(y1 - y0)


# works slow for big input
def find_pairs(universe):
    all_pairs = set()
    all_galaxies = convert_galaxy_to_dict_with_number_and_location(universe).keys()
    cleaned_pairs = set()
    for galaxy1 in all_galaxies:
        for galaxy2 in all_galaxies:
            # do not add if pair with different order already in set
            # do not include a pair of galaxies if galaxy itself
            all_pairs.add((galaxy1, galaxy2))
    # this part is too slow
    for pair in all_pairs:
        if not pair[::-1] in cleaned_pairs and pair[0] != pair[1]:
            cleaned_pairs.add(pair)

    return cleaned_pairs


def calculate_all_paths(universe, times_galaxy_space_expansion=1):
    counter = 0
    indexed_spaces_in_rows = list_of_spaces_in_rows(universe)
    indexed_spaces_in_columns = list_of_spaces_in_column(universe)
    # bug - need to remove one space
    if times_galaxy_space_expansion != 1:
        times_galaxy_space_expansion = times_galaxy_space_expansion - 1

    for galaxy1, galaxy2 in find_pairs(universe):
        x0, y0 = convert_galaxy_to_dict_with_number_and_location(universe)[galaxy1]
        x1, y1 = convert_galaxy_to_dict_with_number_and_location(universe)[galaxy2]
        # when calculating path in row need to take spaces in columns
        calculate_path_in_rows = lenght_with_spaces_between_galaxy(x0, x1, indexed_spaces_in_columns,
                                                                   times_galaxy_space_expansion)
        # when calculating path in column need to take spaces in rows
        calculate_path_in_columns = lenght_with_spaces_between_galaxy(y0, y1, indexed_spaces_in_rows,
                                                                      times_galaxy_space_expansion)

        counter += calculate_path_in_rows + calculate_path_in_columns
    return counter


print("Part 1: small input ", calculate_all_paths(universe_from_small_input, times_galaxy_space_expansion=10))
print("Part 1: ", calculate_all_paths(universe_from_large_input, times_galaxy_space_expansion=1))
print("Part 2: ", calculate_all_paths(universe_from_large_input, times_galaxy_space_expansion=1000000))


# you should go just x-x0 and y-y0
# think how to calculate... from dx and dy
# part 2 9609130 too low
# part 2 702152906986 too high
class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.universe_from_small_input = read_lines(s)
        self.expanded_universe = create_expanded_galaxy(self.universe_from_small_input)
        self.expanded_universe_numbered = convert_galaxy_to_dict_with_number_and_location(self.expanded_universe)
        self.galaxies_locations = convert_galaxy_to_dict_with_number_and_location(self.expanded_universe)

    def test_convert_galaxy_to_dict_with_location_and_number(self):
        self.assertIn(9, convert_galaxy_to_dict_with_number_and_location(self.expanded_universe))

    def test_from_coordinate_to_galaxy_number(self):
        self.assertEqual(convert_galaxy_to_dict_with_number_and_location(self.expanded_universe)[1], (4, 0))
        self.assertEqual(convert_galaxy_to_dict_with_number_and_location(self.expanded_universe)[2], (9, 1))
        self.assertEqual(convert_galaxy_to_dict_with_number_and_location(self.expanded_universe)[3], (0, 2))
        self.assertEqual(convert_galaxy_to_dict_with_number_and_location(self.expanded_universe)[7], (9, 10))

    def test_get_galaxies_location(self):
        self.assertEqual(convert_galaxy_to_dict_with_number_and_location(self.expanded_universe)[1], (4, 0),
                         "Should get location of universe 1")
        self.assertEqual(convert_galaxy_to_dict_with_number_and_location(self.expanded_universe)[3], (0, 2),
                         "Should get location of universe 3")
        self.assertEqual(convert_galaxy_to_dict_with_number_and_location(self.expanded_universe)[6], (12, 7),
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
        self.assertEqual(calculate_all_paths(self.universe_from_small_input), 374,
                         "the sum of the shortest path between all 36 pairs of galaxies is NOT 374")
        self.assertEqual(calculate_all_paths(self.universe_from_small_input, times_galaxy_space_expansion=10), 1030)
        self.assertEqual(calculate_all_paths(self.universe_from_small_input, times_galaxy_space_expansion=100), 8410)

    def test_list_of_spaces_in_rows(self):
        self.assertEqual(len(list_of_spaces_in_rows(self.universe_from_small_input)), 2)

    def test_list_of_spaces_in_column(self):
        self.assertEqual(list_of_spaces_in_column(self.universe_from_small_input), [2, 5, 8])

    def test_list_of_spaces_in_row(self):
        self.assertEqual(list_of_spaces_in_rows(self.universe_from_small_input), [3, 7])

    def test_lenght_with_spaces_between_galaxy(self):
        self.assertEqual(lenght_with_spaces_between_galaxy(3, 7, [2, 5, 8], 1), 5)
        self.assertEqual(lenght_with_spaces_between_galaxy(2, 5, [3, 7], 1), 4)
        self.assertEqual(lenght_with_spaces_between_galaxy(2, 9, [3, 7], 1), 9)


if __name__ == '__main__':
    unittest.main()