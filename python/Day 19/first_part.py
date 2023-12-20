import unittest

s = "small_input.txt"
l = "input.txt"


# px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
def parse_workflows(file: str) -> dict[str:list[str]]:
    workflows = {}
    with open(file, "r", encoding="utf-8") as file:
        for line in file:
            if line == "\n":
                break

            key, value = line.strip()[:-1].split("{")
            value = value.split(",")
            workflows[key] = value

    return workflows


# {x=787,m=2655,a=1222,s=2876}
def parse_part(part: str) -> dict[str:int]:
    ratings = part.strip()[1:-1].split(",")
    # print(ratings)
    part = {}
    for rating in ratings:
        ratings = rating.strip().split("=")
        key, value = ratings
        part[key] = int(value)
    return part


def parse_parts(file: str) -> list[dict]:
    with open(file, "r", encoding="utf-8") as file:
        list_of_parts = []
        new_line = False
        for line in file:
            if new_line:
                list_of_parts.append(parse_part(line))
            if line == "\n":
                new_line = True
        return list_of_parts


# main part
def next_workflow(part_xmas: dict[str:int], workflow_rule: str) -> str | None:
    if "<" in workflow_rule:
        condition, next_workflow_name = workflow_rule.split(":")
        rating_key, limit = condition.split("<")
        if part_xmas[rating_key] < int(limit):
            return next_workflow_name
        else:
            return None

    elif ">" in workflow_rule:
        condition, next_workflow_name = workflow_rule.split(":")
        rating_key, limit = condition.split(">")
        if part_xmas[rating_key] > int(limit):
            return next_workflow_name
        else:
            return None
    else:
        return workflow_rule


def process_part(part_xmas: dict[str:int], workflow_name: str, workflow: dict[str:list[str]]) -> int:
    rules = workflow[workflow_name]
    for rule in rules:
        next_name = next_workflow(part_xmas, rule)
        if next_name == "R":
            return 0
        elif next_name == "A":
            return sum(part_xmas.values())
        elif next_name:
            return process_part(part_xmas, next_name, workflow)
        # else next_name was None, so continue with the loop
    assert False


def part_1(file_input):
    parts = parse_parts(file_input)
    workflows = parse_workflows(file_input)
    return sum(process_part(part, "in", workflows) for part in parts)


print(part_1(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.example: list[str] = s

    def test_sum_all_accepted(self):
        self.assertEqual(part_1(self.example), 19114)


if __name__ == '__main__':
    unittest.main()