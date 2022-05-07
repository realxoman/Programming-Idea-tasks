def symmetrycheck(list):
    n = 1
    n2 = 0
    length = int(len (list) / 2)
    list1 = [None for x in range (length)]
    list2 = [None for x in range (length)]
    for x in list:
        if n <= length:
            list1[n-1] = x
        elif n > (length) + 1:
            list2[length-n2-1] = x
            n2 +=1
        n +=1
    if list1 == list2:
        return True
if symmetrycheck ([1,2,77,8,77,2,1]):
    print ("The reverend he turned to me, without a tear in his eyes")