def reverse(x):
    string = str(x)

    # negative number
    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])


def reverser(x):
    string = str(x)

    if string[0] == '-':
        return '-' + string[:0:-1]
    else:
        return string[::-1]


print(reverse(-252))
print(reverse(60010))

print(reverser(-252))
print(reverser(-60010))

