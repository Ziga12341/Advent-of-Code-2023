import unittest
from typing import List

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> List[str]:
    with open(file, "r", encoding="utf-8") as file:
        return file.readline().split(",")


def sum_one_sequence(sequence: str) -> int:
    result = 0
    for char in sequence:
        char_ascii_value = ord(char)
        result += char_ascii_value
        result = (result * 17) % 256
    return result


def sum_results(pattern: List[str]) -> int:
    return sum(sum_one_sequence(sequence) for sequence in pattern)


small_pattern: List[str] = read_lines(s)
large_pattern: List[str] = read_lines(l)
print("Part 1:", sum_results(large_pattern))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        # ['rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']
        self.example: List[List] = read_lines(s)
        self.first_sequence = "rn=1"
        self.second_sequence = "cm-"

    def test_sum_one_sequence(self):
        self.assertEqual(sum_one_sequence(self.first_sequence), 30)
        self.assertEqual(sum_one_sequence(self.second_sequence), 253)

    def test_sum_results(self):
        self.assertEqual(sum_results(self.example), 1320)


if __name__ == '__main__':
    unittest.main()