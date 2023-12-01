small = "small_input.txt"
whole_input = "input.txt"


def first_digit(string_line):
    for char in string_line:
        if char.isdigit():
            return char


def last_digit(string_line):
    for char in reversed(string_line):
        if char.isdigit():
            return char


with open(whole_input, "r", encoding="utf-8") as file:
    list_of_lines_in_values = []
    for line in file:
        make_number = int(first_digit(line) + last_digit(line))
        list_of_lines_in_values.append(make_number)
    print(sum(list_of_lines_in_values))


# line = "1abc2"
# print(first_digit(line))
# print(last_digit(line))