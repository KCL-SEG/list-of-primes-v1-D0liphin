def primes(number_of_primes:int) -> list[int]:
    """
    generates the first `number_of_primes` primes and returns them as 
    a list
    """
    primes = [2]
    for _ in range(number_of_primes - 1):
        tmp = primes[-1]
        while True:
            tmp += 1
            for prime in primes:
                if tmp % prime == 0:
                    break
            else:
                primes.append(tmp)
                break
    return primes
