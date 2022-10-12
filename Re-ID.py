def solution(i):
    listOfPrimes = []
    primeDigitAmount = 0
    for number in range(2, 100000):
        numberStatus = True
        if primeDigitAmount >= (i+5):
            stringOfPrimes = ''.join(str(e) for e in listOfPrimes)
            return stringOfPrimes[i:i+5]
        for prime in listOfPrimes:
            if (number%prime) == 0:
                numberStatus = False
                break
        if numberStatus:
            primeDigitAmount += len(number.__str__())
            listOfPrimes.append(number)

if __name__ == "__main__":
    print(solution(3))
else:
    print("?")