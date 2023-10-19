def love(numbers):
    result = 0
    first = 0
    second = 0
    third = 0
    for i in range(len(numbers) - 2):
        first += 1
        this = first + second + third

        for j in range(len(numbers) - 1):
            second += 1

            for k in range(len(numbers)):
                third += 1

        result += this
        if result == P:
            return True

    else:
        return False




numbers = [1, 2, 3, 4, 5, 6, 7, 8]

P = 12

print(love(numbers))
