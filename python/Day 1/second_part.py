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

# line = "two1nine"
# complex_line = "lq3nine222one8S"
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


def find_spelled_numbers_by_index(string_line):
    # dict of all spelled numbers with indexes of its starting chat in line
    spelling_numbers_indexed = {}
    for spelled_number in list_of_spelled_numbers:
        if spelled_number in string_line:
            spelling_numbers_indexed[string_line.index(spelled_number)] = spelled_number

    if spelling_numbers_indexed:
        return spelling_numbers_indexed
    else:
        return None


def find_first_number(string_line):
    spelled_numbers = find_spelled_numbers_by_index(string_line)
    # print("spelled_numbers - all:", spelled_numbers)
    # print(string_line)
    # if there is any spelled numbers in line than do this...
    if spelled_numbers:
        # find the smallest key - ( index of first letter of spelled number)
        # index where starts first number
        first_spelled_number_index = min([index for index in spelled_numbers.keys()])
        # print("first_spelled_number_index is:", first_spelled_number_index)
        first_spelled_number = find_spelled_numbers_by_index(string_line)[first_spelled_number_index]
        # print("first_spelled_number:",first_spelled_number)
        # print(find_spelled_numbers_by_index(string_line)[last_spelled_number])
        # print("see what stays in: ", string_line[0:first_spelled_number_index])
        in_front_of_first_spelled_number = string_line[0:first_spelled_number_index]
        if first_digit(in_front_of_first_spelled_number):
            return first_digit(in_front_of_first_spelled_number)
        else:
            # print("from_spelled_to_digit[first_spelled_number]", from_spelled_to_digit[first_spelled_number])
            return from_spelled_to_digit[first_spelled_number]
    # there is no spelled numbers in line
    else:
        return first_digit(string_line)


def find_last_number(string_line):
    # list of all spelled numbers
    spelled_numbers = find_spelled_numbers_by_index(string_line)
    print("spelled_numbers - all:", spelled_numbers)
    print(string_line)
    if spelled_numbers:
        # find the biggest key - ( index of first letter of spelled number) at right
        last_spelled_number_index = max([index for index in spelled_numbers.keys()])
        print("last_spelled_number_index", last_spelled_number_index)

        last_spelled_number = find_spelled_numbers_by_index(string_line)[last_spelled_number_index]
        print("last_spelled_number: ", last_spelled_number)
        print("last_spelled_number is:", last_spelled_number_index)
        print("spelled_numbers[last_spelled_number_index]", spelled_numbers[last_spelled_number_index])
        last_spelled_number_index_of_last_char = last_spelled_number_index + len(last_spelled_number)
        print("last_spelled_number_index_of_last_char", last_spelled_number_index_of_last_char)
        behind_last_spelled_number = string_line[last_spelled_number_index_of_last_char:]
        print("behind_last_spelled_number", behind_last_spelled_number)
        if last_digit(behind_last_spelled_number):
            return last_digit(behind_last_spelled_number)
        else:
            print("from_spelled_to_digit[last_spelled_number]", from_spelled_to_digit[last_spelled_number])
            return from_spelled_to_digit[last_spelled_number]
    else:
        return last_digit(string_line)

turbo = ("dsfsdnsevenneoneee")
# print(find_first_number(turbo))
print(find_last_number(turbo))

with open("input.txt", "r", encoding="utf-8") as file:
    list_of_lines_in_values = []
    for line in file:
        print(line)
        # convert all numbers to string first "merge" digits and convert to integer
        make_number = int(str(find_first_number(line)) + str(find_last_number(line)))
        list_of_lines_in_values.append(make_number)
        print(make_number)
    print(list_of_lines_in_values)
    print(len(list_of_lines_in_values))
    print(sum(list_of_lines_in_values))

# [21, 38, 92, 37, 57, 22, 69, 67, 31, 66, 12, 22, 22, 72, 33, 96, 35, 28, 29, 44, 37, 55, 83, 83, 44, 92, 24, 34, 29, 62, 86, 88, 12, 74, 62, 91, 17, 75, 97, 66, 81, 92, 48, 37, 73, 26, 73, 97, 28, 18, 93, 12, 53, 53, 54, 46, 15, 91, 74, 66, 15, 88, 45, 19, 68, 79, 33, 12, 93, 39, 37, 33, 28, 76, 68, 77, 78, 87, 61, 66, 68, 72, 27, 45, 45, 75, 28, 95, 22, 95, 98, 17, 76, 61, 76, 71, 79, 46, 79, 68, 27, 15, 88, 12, 79, 84, 37, 17, 71, 88, 26, 95, 86, 52, 84, 68, 55, 27, 18, 41, 39, 61, 24, 59, 93, 13, 87, 66, 55, 84, 28, 45, 73, 88, 87, 68, 82, 37, 78, 46, 67, 33, 28, 98, 38, 96, 12, 28, 45, 68, 44, 46, 88, 86, 65, 42, 88, 16, 79, 95, 18, 18, 13, 19, 36, 96, 22, 14, 39, 12, 95, 68, 94, 84, 13, 16, 53, 53, 43, 24, 81, 39, 67, 22, 37, 14, 76, 64, 56, 15, 75, 17, 51, 81, 36, 35, 17, 83, 68, 13, 35, 42, 17, 94, 22, 51, 29, 74, 54, 11, 54, 68, 55, 12, 14, 22, 45, 49, 72, 33, 56, 69, 32, 18, 88, 37, 74, 71, 83, 37, 28, 99, 44, 29, 71, 76, 82, 14, 62, 57, 54, 87, 86, 34, 29, 85, 85, 49, 56, 59, 37, 23, 72, 76, 73, 73, 53, 44, 14, 66, 16, 17, 22, 61, 46, 52, 96, 39, 87, 89, 81, 12, 28, 22, 33, 27, 12, 64, 64, 31, 12, 88, 31, 29, 42, 62, 93, 43, 52, 15, 11, 26, 41, 67, 78, 42, 26, 57, 72, 18, 22, 11, 15, 11, 24, 57, 77, 61, 15, 79, 14, 88, 71, 56, 18, 98, 11, 21, 86, 43, 53, 64, 28, 69, 67, 66, 62, 54, 53, 33, 66, 42, 78, 77, 44, 74, 15, 28, 11, 37, 83, 64, 94, 78, 92, 11, 83, 64, 92, 56, 25, 56, 64, 54, 56, 53, 79, 18, 88, 32, 64, 99, 75, 84, 23, 81, 25, 88, 84, 63, 31, 13, 78, 89, 94, 99, 85, 61, 55, 58, 85, 69, 25, 17, 64, 68, 98, 16, 32, 22, 61, 14, 88, 54, 56, 94, 67, 27, 64, 72, 44, 12, 38, 33, 15, 15, 68, 47, 52, 66, 21, 69, 87, 16, 22, 75, 21, 89, 41, 44, 81, 87, 69, 64, 63, 73, 97, 42, 94, 23, 73, 28, 79, 67, 96, 67, 45, 41, 93, 64, 18, 28, 14, 66, 68, 55, 66, 69, 82, 51, 48, 69, 62, 87, 79, 21, 92, 38, 93, 18, 39, 46, 65, 18, 84, 94, 28, 59, 49, 14, 25, 73, 81, 62, 41, 69, 87, 55, 98, 54, 23, 27, 45, 68, 86, 72, 44, 27, 15, 14, 92, 77, 74, 36, 21, 52, 38, 15, 55, 65, 34, 22, 75, 48, 76, 86, 22, 97, 34, 81, 67, 49, 68, 83, 48, 72, 76, 47, 51, 95, 62, 97, 74, 22, 24, 75, 15, 31, 22, 34, 87, 35, 57, 34, 82, 76, 35, 46, 79, 52, 92, 58, 41, 17, 62, 64, 46, 57, 45, 37, 74, 47, 14, 39, 15, 51, 69, 64, 51, 88, 36, 67, 57, 58, 21, 71, 54, 98, 42, 99, 52, 65, 19, 17, 86, 31, 77, 24, 47, 41, 77, 49, 57, 15, 99, 88, 39, 15, 25, 94, 88, 64, 99, 81, 92, 85, 72, 86, 18, 82, 65, 65, 33, 18, 59, 27, 69, 78, 47, 86, 58, 75, 82, 46, 27, 81, 86, 73, 78, 62, 79, 26, 57, 75, 47, 95, 43, 14, 33, 64, 91, 28, 21, 63, 45, 36, 88, 25, 16, 98, 53, 32, 25, 29, 75, 49, 62, 45, 77, 12, 13, 25, 46, 11, 11, 52, 11, 59, 89, 38, 67, 35, 11, 55, 96, 18, 29, 12, 77, 69, 34, 63, 47, 37, 54, 64, 78, 47, 87, 25, 22, 64, 94, 63, 34, 79, 49, 79, 77, 54, 89, 61, 33, 98, 81, 69, 11, 32, 59, 98, 11, 91, 19, 78, 73, 69, 77, 39, 23, 55, 27, 18, 32, 81, 44, 42, 47, 33, 81, 87, 42, 54, 65, 22, 68, 48, 22, 41, 24, 49, 16, 38, 55, 58, 31, 66, 37, 76, 95, 59, 35, 34, 52, 32, 11, 94, 37, 85, 45, 53, 13, 86, 77, 17, 72, 36, 99, 56, 81, 34, 38, 75, 44, 29, 96, 37, 84, 41, 35, 22, 91, 78, 17, 23, 95, 86, 76, 78, 55, 48, 78, 81, 39, 95, 99, 46, 92, 37, 33, 18, 33, 77, 51, 87, 28, 67, 36, 88, 47, 64, 85, 59, 77, 14, 81, 15, 96, 28, 99, 22, 79, 29, 34, 99, 77, 81, 61, 66, 79, 75, 89, 19, 57, 78, 63, 19, 94, 43, 85, 91, 16, 88, 18, 36, 27, 33, 34, 99, 18, 74, 38, 28, 86, 39, 57, 64, 55, 35, 35, 75, 62, 62, 84, 88, 89, 13, 72, 85, 14, 13, 39, 85, 78, 98, 48, 16, 32, 22, 32, 89, 15, 53, 61, 98, 35, 52, 29, 46, 83, 58, 35, 86, 54, 88, 87, 92, 19, 71, 69, 31, 94, 88, 26, 62, 35, 29, 15, 46, 47, 13, 53, 71, 86, 55, 96, 54, 57, 88, 36, 75, 89, 39, 94, 55, 91, 31, 75, 11, 82, 29, 48, 85, 88, 44, 51, 45, 28, 77, 95, 94, 85, 31, 83, 39, 42, 97, 99, 24, 76, 43, 81, 65, 11, 16, 91, 49, 11, 75, 49, 68, 23, 29, 35, 11, 17, 72, 96, 28, 63, 95, 97, 77, 81, 55, 74, 24, 76, 77, 47, 66, 22, 66, 88, 65, 84, 39, 73, 81, 87, 68, 43, 42, 85, 22, 41, 99, 57, 15, 11, 53, 69, 54, 12, 87, 19, 83, 12, 83, 82, 91]

# 54673 --> too high