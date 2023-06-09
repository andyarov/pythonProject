first_number = int(input("first numer: "))
second_number = int(input("second number: "))
"""
answer = first_number + second_number
print(answer)

answer = first_number - second_number
print(answer)

answer = first_number * second_number
print(answer)
"""

if first_number > second_number:
    print(second_number)
    print(first_number)
elif first_number < second_number:
    print(first_number)
    print(second_number)
else:
    print("The numbers are equal")