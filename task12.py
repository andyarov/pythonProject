tallies = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_decimal(roman_number):
    sum = 0
    for i in range(len(roman_number) - 1):
        left = roman_number[i]
        right = roman_number[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[right]
    sum += tallies[roman_number[-1]]
    return sum


print(roman_to_decimal("III"))
