def birthday_cake_candles(candles):
    current_max = candles[0]
    answer = update_answer_current_max(current_max)

    for height in candles[1:]:
        if equals_current_max(height, current_max):
            increment_count(answer)
        elif greater_than_current_max(current_max, height):
            current_max = update_current_max(current_max, height)
            answer = update_answer_current_max(current_max)

    return answer["Count"]


def update_answer_current_max(current_max):
    return {"Max_Height": current_max, "Count": 1}


def update_current_max(current_max, height):
    current_max = height
    return current_max


def greater_than_current_max(current_max, height):
    return height > current_max


def increment_count(answer):
    answer["Count"] += 1


def equals_current_max(height, current_max):
    return height == current_max


# Driver code
example_candles = [3, 2, 1, 3]
print(birthday_cake_candles(example_candles))  # 2
