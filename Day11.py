a = str(input("Enter a time in 12-hour AM/PM format(hh:mm:ss AM/PM): "))


def convert(a):
    if a[-2:] == "AM" and a[:2] == "12":
        return "00" + a[2:-2]

    elif a[-2:] == "AM":
        return a[:-2]

    elif a[-2:] == "PM" and a[:2] == "12":
        return a[:-2]

    else:
        return str(int(a[:2]) + 12) + a[2:-2]


print("Time in 24-hour format: ",convert(a))