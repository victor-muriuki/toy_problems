def two_positive_numbers(a, b, c):
    #checks whether only 2 argurments are positve
    if a > 0 and b > 0 and c > 0:
        print("false")
    elif a > 0 and b > 0 and c < 0:
        print("true")
    elif a > 0 and b < 0 and c > 0:
        print("true")
    elif a < 0 and b > 0 and c > 0:
        print("true")
    elif a < 0 and b < 0 and c < 0:
        print("false")


two_positive_numbers(-1, -2, -3)
