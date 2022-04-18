#function to check the powers of 4
def powers_of_four(num):
    import math
    from math import log
    powers = log(num, 4)
    return powers

print(powers_of_four(256))