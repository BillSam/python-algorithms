
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
# Notes:
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.

num1 = '3640'
num2 = '183654'

# Approach 1


def solution(one, two):
    eval(one) + eval(two)
    return str(eval(one)+eval(two))


print(solution(num1, num2))


# Approach 2
# Given a string of length one, the ord() function returns an integer representing the Unicode code point of the
# character
# when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.


def solution2(first, second):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(first)-1), 10**(len(second)-1)

    print(len(first)-1)
    print(10**(len(first)-1))
    print(10**(len(second)-1))
    print(20//2)
    for i in first:
        n1 += (ord(i) - ord("0")) * m1
        m1 = m1//10

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2 // 10

    return str(n1 + n2)


print(solution2(num1, num2))




