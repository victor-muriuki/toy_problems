def two_positive_numbers(a, b, c):
    #checks whether only 2 argurments are positve
    if a > 0 and b > 0 and c > 0:
        return False
    elif a > 0 and b > 0 and c < 0:
       return True
    elif a > 0 and b < 0 and c > 0:
        return True
    elif a < 0 and b > 0 and c > 0:
        return True
    elif a < 0 and b < 0 and c < 0:
        return False


# two_positive_numbers(-1, -2, -3)

a = 1
b = 2
c = -4
result = two_positive_numbers(a, b, c)
print(result)
