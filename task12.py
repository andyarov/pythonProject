tallies = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_decimal(roman_number):
    result = [value for key, value in tallies.items() if key == roman_number]
    print(result)


roman_to_decimal("I")
