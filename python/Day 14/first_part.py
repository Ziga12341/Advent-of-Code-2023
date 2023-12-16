import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


small_platform: list[str] = read_lines(s)
large_platform: list[str] = read_lines(l)


def from_rows_to_columns(platform: list[str]) -> list[str]:
    columns_to_rows = []
    for i in range(len(platform[0])):
        new_line = ""
        for line in platform:
            new_line += line[i]
        columns_to_rows.append(new_line)
    return columns_to_rows


def count_number_of_total_load_in_line(converted_line: str) -> int:
    count_load = 0
    converted_line = list(converted_line)
    i_while = 0
    while i_while < len(converted_line):
        i = 0
        while i < len(converted_line):
            if converted_line[i] == "O":
                #
                if converted_line[i - 1] != "#" and converted_line[i - 1] != "O" and i != 0:
                    converted_line[i - 1] = "O"
                    converted_line[i] = "."
            i += 1
        i_while += 1

    for for_i, char in enumerate(converted_line):
        if char == "O":
            count_load += len(converted_line) - for_i
    return count_load


def total_load(platform: list[str]) -> int:
    count_total_load = 0
    for converted_line in platform:
        count_total_load += count_number_of_total_load_in_line(converted_line)
    return count_total_load


print("Part 1: ", total_load(from_rows_to_columns(large_platform)))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_platform: list[str] = read_lines(s)
        self.sample_grid = ["123457", "123456", "123456", "123456", "123456", "123458"]
        self.sample_grid_converted = ["111111", "222222", "333333", "444444", "555555", "766668"]
        self.converted = from_rows_to_columns(self.small_platform)
        self.first_column_to_line = 'OO.O.O..##'
        self.second_column_to_line = '...OO....O'

    def test_read_lines(self):
        self.assertEqual(len(self.small_platform), 10, "small platform should have 10 rows")
        self.assertEqual(len(self.small_platform[0]), 10, "first line in platform should have 10 char")

    def test_from_rows_to_columns(self):
        self.assertEqual(from_rows_to_columns(self.sample_grid), self.sample_grid_converted,
                         "You should convert columns to rows")

        self.assertEqual(from_rows_to_columns(self.sample_grid_converted), self.sample_grid,
                         "You should convert columns to rows")

    def test_count_number_of_total_load_in_line(self):
        self.assertEqual(count_number_of_total_load_in_line(self.first_column_to_line), 34)
        self.assertEqual(count_number_of_total_load_in_line(self.second_column_to_line), 27)

    def test_total_load(self):
        self.assertEqual(total_load(self.converted), 136)


if __name__ == '__main__':
    unittest.main()
# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....