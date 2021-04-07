from functools import reduce


def cou(str1):
    coun = 0
    ls = []
    for i in str(str1):
        for j in i:
            ls.append(j)
    for i in ls:
        print(i)
        if i.isdigit():
            coun += 1
    return coun


if __name__ == '__main__':
    lst= ["a123", "bcd1.12", 'sfd321']

    sm1 = reduce(lambda x, y: cou(x) + cou(y), lst)
    print(sm1)
