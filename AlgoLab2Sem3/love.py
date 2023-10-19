def love(numbers, P):
    for i in range(0, len(numbers) - 2):

        for j in range(i+1, len(numbers) - 1):

            for k in range(j+1, len(numbers)):

                if numbers[i] >= 0 and numbers[j] >= 0 and numbers[k] >= 0:

                    if numbers[i] != numbers[j] and numbers[i] != numbers[k] and numbers[j] != numbers[k]:

                        if numbers[i] + numbers[j] + numbers[k] == P:
                            print("Такі числа є:", numbers[i], ",", numbers[j], ",", numbers[k])
                            return True

    print("Таких чисел немає")
    return False


# P = 20
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
# print(love(numbers, P))


# P = Ai + Aj + Ak = 3Ai + 3 = 3(Ai + 1)

# i ≠ j ≠ k
# 3 <= N <= 1000
# 1 <= Ai <= 10^9, де 1 <= i <= N
# 1 <= P <= 3*10^9

