def preff(a):
    return a[:5]


def ban(b):
    res = ''
    word = ['Сэм']
    for i in b.split():
        if i in word:
            res += i[0] + '*'*(len(i)-1) + ' '
        else:
            res += i + ' '
    return res[:-1]


ww = 'Сэм чепщошщокшош лол'
print(ban(preff(ww)))