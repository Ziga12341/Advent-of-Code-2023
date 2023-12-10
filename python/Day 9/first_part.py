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




def go_through_all_lines(all_history_values_from_line):
    sum_all_last_feature_values = 0
    for history_values in all_history_values_from_line:
        stack = until_all_zero(history_values)
        # print(stack)
        sum_all_last_feature_values += sum_last_from_stack(stack)
    return sum_all_last_feature_values


all_history_values = lines_to_list_of_int(l)
print("Part 1:", go_through_all_lines(all_history_values))


# did not succeed with recursion

# all numbers in sequence not zero... continue with process
# i need to sum last element with last element i get
# sum lase element from each recursion call... always know which was last sum and add last sum to
# add last number you get to history_list
# in every step you should have one number less in list
def sum_last_element_when_all_list_zero(history_list):
    new_history_list = []
    if not history_list:
        return 0

    if all(num == 0 for num in history_list):
        return 0
    else:

        print(history_list)
        return sum_last_element_when_all_list_zero(history_list)

# print(sum_last_element_when_all_list_zero(all_history_values[0]))