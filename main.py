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


a = []
b = ""
f_4953(3, 30, b, "")
print(a)

count = 0
for item in a:
    if item.count('11') == 0:
        count += 1
        print(item)
print(count)
