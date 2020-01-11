# Find the sum of all the multiples of 3 or 5 below 1000.
def euler1():
    total = 0
    for number in range(1000):
        if number % 5 == 0 or number % 3 == 0:
            total += number
    print(total)


# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.
def euler2():
    first_no = 1
    second_no = 2
    combination = [1, 2]
    total = 0

    while first_no + second_no < 4000000:
        next_no = first_no + second_no
        first_no = second_no
        second_no = next_no
        combination.append(next_no)

    for digit in combination:
        if digit % 2 == 0:
            total += digit

    print(total)
