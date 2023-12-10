s = "small_input.txt"
l = "input.txt"


def lines_to_list_of_int(file):
    with open(file, "r", encoding="utf-8") as file:
        file_in_list = []
        for line in file:
            line = line.strip().split(" ")
            char_to_int = []
            for char in line:
                char_to_int.append(int(char))
            file_in_list.append(char_to_int)
        return file_in_list


def interactive_new_list(history_list):
    new_history_list = []
    for i in range(len(history_list) - 1):
        new_history_list.append(history_list[1 + i] - history_list[0 + i])
    return new_history_list


def until_all_zero(history_list):
    all_stack = [history_list]
    while not all(num == 0 for num in all_stack[-1]):
        all_stack.append(interactive_new_list(all_stack[-1]))
    all_stack.append(interactive_new_list(all_stack[-1]))
    return all_stack


def sum_last_from_stack(all_stack):
    sumaraza = 0
    for history_list in all_stack:
        sumaraza += history_list[-1]
    return sumaraza


# added for part 2
def get_first_element_from_stack(whole_stack):
    return [values[0] for values in whole_stack]


# added for part 2
def calculate_history(whole_stack):
    old_value = 0
    for element in reversed(get_first_element_from_stack(whole_stack)):
        # takes me tooo much time to figure out
        old_value = -old_value + element
    return old_value


def go_through_all_lines(all_history_values_from_line):
    sum_all_last_feature_values = 0
    for history_values in all_history_values_from_line:
        stack = until_all_zero(history_values)
        sum_all_last_feature_values += calculate_history(stack)
    return sum_all_last_feature_values


all_history_values = lines_to_list_of_int(l)
print("Part 2:", go_through_all_lines(all_history_values))