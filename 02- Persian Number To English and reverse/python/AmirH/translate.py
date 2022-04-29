engtoperd = {
    1 : '۱',
    2 : '۲',
    3 : '۳',
    4 : '۴',
    5 : '۵',
    6 : '۶',
    7 : '۷',
    8 : '۸',
    9 : '۹',
    0 : '۰'
}
pertoengd = {
    '۱' : 1,
    '۲' : 2,
    '۳' : 3,
    '۴' : 4,
    '۵' : 5,
    '۶' : 6,
    '۷' : 7,
    '۸' : 8,
    '۹' : 9,
    '۰' : 0
}

def engtoper (numb):
    return (engtoperd.get (numb))
def pertoeng (numb):
    return (pertoengd.get (numb))
print (engtoper (5))
print (pertoeng ('۳'))