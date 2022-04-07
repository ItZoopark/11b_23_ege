import sys


def f_5011(x, y, p):
    if p != 1 and p == 9 and x == y:
        return 1
    elif p > 9:
        return 0
    else:
        return f_5011(x + 3, y, p + 1) + f_5011(x - 1, y, p + 1)


# print(f(1000, 1000, 1))

def f_4953(x, y, b, m):
    if m == "1":
        b += "1"
    elif m == "2":
        b += "2"
    elif m == "3":
        b += "3"

    if x == y:
        a.append(b)
    elif x > y:
        b = ""
    else:
        f_4953(x + 1, y, b, "1")
        f_4953(x + 3, y, b, "3")
        f_4953(x * 2, y, b, "2")


# a = []
# b = ""
# f_4953(3, 30, b, "")
# print(a)
#
# count = 0
# for item in a:
#     if item.count('11') == 0:
#         count += 1
#         print(item)
# print(count)

def zero(a):
    size = len(bin(a)[3:])
    return 2 ** size


def check(a):
    x = bin(a)[2:]
    if x[0] == '1' and set(x[1:]) == {'0'}:
        return True
    else:
        return False


# print(check(16))

# print(set(bin(16)[3:]) == {'0'})

# # ob10011 = 19
#   10000 = 2**4

def f_3717(x, y):
    if check(x):
        return 0
    if x == y:
        return 1
    elif x < y:
        return 0
    else:
        return f_3717(zero(x), y) + f_3717(x - 1, y)


print(f_3717(1000000, 1000))
