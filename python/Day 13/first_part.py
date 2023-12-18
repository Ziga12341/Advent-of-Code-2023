import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list[list]:
    with open(file, "r", encoding="utf-8") as file:
        patterns = []
        pattern = []
        for line in file:
            line = line.strip()
            if line == "":
                patterns.append(pattern)
                pattern = []
            else:
                pattern.append(line)
        patterns.append(pattern)
        return patterns


small_patterns: list[list[str]] = read_lines(s)
large_patterns: list[list[str]] = read_lines(l)


def number_of_rows_above_horizontal_line(pattern: list[str]) -> int:
    for i, (line1, line2) in enumerate(zip(pattern, pattern[1:])):
        if line1 == line2:
            # print(i)
            # print(line1, line2)
            up = pattern[:i + 1]
            down = pattern[i + 1:]
            # print("up", up)
            # print("down", down)
            if len(down) < len(up):
                up = up[::-1]
                up = up[:len(down)]
                if up == down:
                    return (i + 1) * 100

            elif len(down) > len(up):
                # bug: if finish up... than you need first to slise "down" and than reverse it
                down = down[:len(up)]
                down = down[::-1]
                if up == down:
                    return (i + 1) * 100
    return 0


# print(number_of_rows_above_horizontal_line(small_patterns[1]))

def from_rows_to_columns(pattern: list[str]) -> list[str]:
    columns_to_rows = []
    for i in range(len(pattern[0])):
        new_line = ""
        for line in pattern:
            new_line += line[i]
        columns_to_rows.append(new_line)
    return columns_to_rows


def number_of_columns_on_left_of_vertical_line(pattern: list[str]) -> int:
    # convert rows to columns
    pattern = from_rows_to_columns(pattern)
    # print(pattern)
    for i, (line1, line2) in enumerate(zip(pattern, pattern[1:])):
        if line1 == line2:
            left_side = pattern[:i + 1]
            right_side = pattern[i + 1:]
            if len(left_side) < len(right_side):
                # bug: if finish on left side.... than you need first to slise "right_side" and then reverse it
                right_side = right_side[:len(left_side)]
                right_side = right_side[::-1]
                if right_side == left_side:
                    return i + 1
            elif len(left_side) > len(right_side):
                left_side = left_side[::-1]
                left_side = left_side[:len(right_side)]
                if right_side == left_side:
                    return i + 1
    return 0


(number_of_columns_on_left_of_vertical_line(small_patterns[0]))


def sum_columns_and_rows_counter(patterns: list[list]) -> int:
    counter = 0
    for i, pattern in enumerate(patterns):
        vertical_counter = number_of_columns_on_left_of_vertical_line(pattern)
        horizontal_counter = number_of_rows_above_horizontal_line(pattern)
        counter += horizontal_counter
        counter += vertical_counter
    return counter


print("Part 1: ", sum_columns_and_rows_counter(large_patterns))


# Part 1:  43614

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_patterns: list[list] = read_lines(s)
        self.sample_grid = ["123457", "123456", "123456", "123456", "123456", "123458"]
        self.sample_grid_converted = ["111111", "222222", "333333", "444444", "555555", "766668"]
        self.last_from_input = ["#..#..#", "######.", ".....#.", "#..####", ".##....", "....###", "#..##.#", "#..###.",
                                "####.#.", ".##.#.#", "#..#.#.", "....###", ".###.#.", ".##..#.", ".##..#."]
        self.fifth_from_input = ["#..####", ".##....", "..#....", "..#.#..", "#.#.#..", "..#....", ".##....", "#..####",
                                 ".#...##", "#..#.##", "#..#...", "..#.###", "..#####", ".###..."]
        self.sixth_from_input = [".####.##......#", "...##.##..##..#", "...##.##..##..#", ".####.##......#",
                                 "#.##.#..#.##.#.",
                                 "..#####.##.###.", ".#...#...#..#..", "#######.######.", ".#.#...########"]

    def test_read_lines(self):
        self.assertEqual(len(self.small_patterns), 2, "small pattern should have 2 lists of lines")
        self.assertEqual(len(self.small_patterns[0]), 7, "first pattern should have 7 lines")

    def test_number_of_rows_above_horizontal_line(self):
        self.assertEqual(number_of_rows_above_horizontal_line(self.small_patterns[1]), 400,
                         "in second pattern rows above vertical line should be 4 * 100")
        self.assertEqual(number_of_rows_above_horizontal_line(self.last_from_input), 1400,
                         "in last pattern from input rows above vertical line should be 14 * 100")
        self.assertEqual(number_of_rows_above_horizontal_line(self.sixth_from_input), 200,
                         "in sixth pattern from input rows above vertical line should be 2 * 100")

    def test_from_rows_to_columns(self):
        self.assertEqual(from_rows_to_columns(self.sample_grid), self.sample_grid_converted,
                         "You should convert columns to rows")

        self.assertEqual(from_rows_to_columns(self.sample_grid_converted), self.sample_grid,
                         "You should convert columns to rows")

    def test_number_of_columns_on_left_of_vertical_line(self):
        self.assertEqual(number_of_columns_on_left_of_vertical_line(self.small_patterns[0]), 5,
                         "in first pattern it should be 5 columns on the left of vertical line")
        self.assertEqual(number_of_columns_on_left_of_vertical_line(self.fifth_from_input), 6,
                         "in fifth pattern from input it should be 6 columns on the left of vertical line")

    def test_sum_columns_and_rows_counter(self):
        self.assertEqual(sum_columns_and_rows_counter(self.small_patterns), 405,
                         "take every first from patteren for vertical sum and every second for horisontal sum, all together should be 405")


if __name__ == '__main__':
    unittest.main()