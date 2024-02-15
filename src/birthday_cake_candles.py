def birthdayCakeCandles(candles):
    current_max = candles[0]
    answer = {"Max_Height": current_max, "Count": 1}

    for height in candles[1:]:
        if height == current_max:
            answer["Count"] += 1
        elif height > current_max:
            current_max = height
            answer = {"Max_Height": current_max, "Count": 1}

    return answer["Count"]
