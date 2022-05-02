def engtoroman(numberi):
    numdic1 = {
        "0" : "",
        "1" : "I",
        "2" : "II",
        "3" : "III",
        "4" : "IV",
        "5" : "V",
        "6" : "VI",
        "7" : "VII",
        "8" : "VIII",
        "9" : "IX"
    }
    numdic2 = {
        "0" : "",
        "1" : "X",
        "2" : "XX",
        "3" : "XXX",
        "4" : "XL",
        "5" : "L",
        "6" : "LX",
        "7" : "LXX",
        "8" : "LXXX",
        "9" : "XC"
    }
    numdic3 = {
        "0" : "",
        "1" : "C",
        "2" : "CC",
        "3" : "CCC",
        "4" : "CD",
        "5" : "D",
        "6" : "DC",
        "7" : "DCC",
        "8" : "DCCC",
        "9" : "CM"
    }
    number = str (numberi)
    leng = len (number)
    s = 0
    result = ""
    for x in number:
        if s == 0 and leng == 3:
            result = result + numdic3[str (x)]
        elif s == 0 and leng == 2:
            result = result + numdic2 [str (x)]
        elif s == 1 and leng == 3:
            result = result + numdic2 [str (x)]
        if s == leng - 1:
            result = result + numdic1 [str (x)]
        s +=1
    return (result)
def romantoeng(number):
    result = 0
    count1 = 0
    count2 = 0
    count3 = 0
    for x in number:
        if x == "C" and count2 == 0:
            result += 100
            count1 = 1
        elif x == "D" and count1 == 0:
            result += 500
        elif x == "D" and count1 == 1:
            result += 300
            count1 = 0
        elif x == "M" and count1 == 1:
            result += 800
            count1 = 0
        if x == "X" and count3 == 0:
            result += 10
            count2 = 1
        elif x == "L" and count2 == 0:
            result += 50
        elif x == "L" and count2 == 1:
            result += 30
            count2 = 0
        elif x == "C" and count2 == 1:
            result += 80
            count2 = 0
        if x == "I":
            result += 1
            count3 = 1
        elif x == "V" and count3 == 0:
            result += 5
        elif x == "V" and count3 == 1:
            result += 3
            count3 = 0
        elif x == "X" and count3 == 1:
            result += 8
            count3 = 0
    return (result)
print (engtoroman (555))
print (romantoeng ("CCCXXXIII"))