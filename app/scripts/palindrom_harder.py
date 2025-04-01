# Napisz funkcję, która sprawdzi, czy dany ciąg znaków można przekształcić w palindrom poprzez przestawienie jego liter.


def can_form_palindrome(str):
    dic = {}
    for char in str:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    table = sorted(dic.values())
    for idx, count in enumerate(table):
        if idx == 0:
            if count == 1 or count % 2 == 0 :
                continue
            else:
                return False
        else:
            if count % 2 != 0:
                return False
    return True



print(can_form_palindrome("civic"))  # True (już jest palindromem)
print(can_form_palindrome("ivicc"))  # True (można przestawić na "civic")
print(can_form_palindrome("hello"))  # False (nie da się ułożyć palindromu)
print(can_form_palindrome("aabbcc"))  # True (można ułożyć np. "abcacba")
