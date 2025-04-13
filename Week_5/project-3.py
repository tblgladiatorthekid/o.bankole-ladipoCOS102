def find_factors (z):
    factors = []
    for i in range (1,z + 1):
        if z % i == 0:
            factors.append(i)
            print(f"The factors of {z} are {factors}")
        else:
            continue
    return z
find_factors(z = int(input("Enter your number")))