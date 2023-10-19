def love(numbers):
    for i in range(len(numbers) - 2):
        result = 0
        this = numbers[i] + numbers[i+1] + numbers[i+2]

        result += this
        if result == P:
            return True

    else:
        return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

P = 12

print(love(numbers))

# N = 8

# P = Ai + Aj + Ak = 3Ai + 3 = 3(Ai + 1)

# 3<= N <= 1000
# 1<= Ai <= 10^9 де 1<= i <=N
# 1<= P <= 3*10^9
