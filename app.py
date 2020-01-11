counter = 0

for number in range(1000):
    if number % 5 == 0 or number % 3 == 0:
        counter += number
print(counter)
