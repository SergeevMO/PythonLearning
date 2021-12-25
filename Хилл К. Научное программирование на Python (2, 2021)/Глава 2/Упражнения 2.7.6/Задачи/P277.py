# Палиндромы
def ispalindrom(s):
    if len(s) < 2:
        return True

    return s[0] == s[-1] and ispalindrom(s[1:-1])


string = "казак"
print(ispalindrom(string))
