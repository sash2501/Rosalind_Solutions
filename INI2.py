#Problem Given: Two positive integers a and b, each less than 1000.
#Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

def hypotenuse(a, b):
    return a ** 2 + b ** 2

a = 934
b = 987
s = hypotenuse(a, b)
print(s)
#1846525
