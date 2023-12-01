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


list_of_spelled_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

from_spelled_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


# I had bug that count just first "spelled number" the other were lost
def find_spelled_numbers_by_index(string_line):
    # dict of all spelled numbers with indexes of its starting char in line
    # key: value ; index of first char in line: spelled number
    # example: {9: 'three', 5: 'five'}
    spelling_numbers_indexed = {}
    for spelled_number in list_of_spelled_numbers:

        # FIX - use while loop
        start_index = 0
        while start_index != -1:
            start_index = string_line.find(spelled_number, start_index)
            if start_index != -1:
                spelling_numbers_indexed[start_index] = spelled_number
                start_index += len(spelled_number)


        # BUG! for loop find just first "spelled number" in string and then it is done...
        # if spelled_number in string_line:
        #     start_index = string_line.index(spelled_number)
        #     spelling_numbers_indexed[start_index] = spelled_number

    return spelling_numbers_indexed or None


def find_first_number(string_line):
    spelled_numbers = find_spelled_numbers_by_index(string_line)
    # if there is any spelled numbers in line than do this...
    if spelled_numbers:
        # find the smallest key - ( index of first letter of spelled number)
        # index where starts first number
        first_spelled_number_index = min([index for index in spelled_numbers.keys()])
        first_spelled_number = find_spelled_numbers_by_index(string_line)[first_spelled_number_index]
        # slise to first spelled number
        in_front_of_first_spelled_number = string_line[0:first_spelled_number_index]
        if first_digit(in_front_of_first_spelled_number):
            return first_digit(in_front_of_first_spelled_number)
        else:
            return from_spelled_to_digit[first_spelled_number]

    # there is no spelled numbers in line
    else:
        return first_digit(string_line)


def find_last_number(string_line):
    # list of all spelled numbers
    spelled_numbers = find_spelled_numbers_by_index(string_line)
    if spelled_numbers:
        # find the biggest key - ( index of first letter of spelled number) at right
        last_spelled_number_index = max([index for index in spelled_numbers.keys()])
        last_spelled_number = find_spelled_numbers_by_index(string_line)[last_spelled_number_index]
        last_spelled_number_index_of_last_char = last_spelled_number_index + len(last_spelled_number)
        behind_last_spelled_number = string_line[last_spelled_number_index_of_last_char:]
        if last_digit(behind_last_spelled_number):
            return last_digit(behind_last_spelled_number)
        else:
            return from_spelled_to_digit[last_spelled_number]
    else:
        return last_digit(string_line)


with open("input.txt", "r", encoding="utf-8") as file:
     list_of_lines_in_values = []
     for line in file:
        # convert all numbers to string first "merge" digits and convert to integer
        make_number = int(str(find_first_number(line)) + str(find_last_number(line)))
        list_of_lines_in_values.append(make_number)

print(sum(list_of_lines_in_values))


# 54673 --> too high
# right answer --> 54649