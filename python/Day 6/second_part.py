small = "small_input.txt"
whole_input = "input.txt"
with open(whole_input, "r", encoding="utf-8") as file:
    time, distance = file.readlines()
    time = [time for time in (time.strip().split(" ")) if time][1:]
    distance = [distance for distance in (distance.strip().split(" ")) if distance][1:]
    time = int("".join(time))
    distance = int("".join(distance))
    winning_ways = []
    for i in range(time):
        case = time - i
        result = case * i
        if result > distance:
            winning_ways.append(result)
    print(len(winning_ways))