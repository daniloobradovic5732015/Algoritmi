def msort(s):
    result = []
    if len(s)<2:
        return s
    mid = int(len(s)/2)
    y = msort (s[:mid])
    z = msort (s[mid:])
    while (len(y) > 0 ) or (len(z) > 0 ):
        if len(y) > 0 and len(z) > 0:
            if y[0]>z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0 :
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result
