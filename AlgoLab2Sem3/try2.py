def love(numbers):
    result = 0
    for i in range(len(numbers) - 2):

        for j in range(len(numbers) - 1):

            for k in range(len(numbers)):

                this = numbers[i] + numbers[j] + numbers[k]

        result += this
        if result == P:
            return True

    else:
        return False




numbers = [1, 2, 3, 4, 5, 6, 7, 8]

P = 12

print(love(numbers))
