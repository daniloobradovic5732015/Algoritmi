def quick_sort(s):
    less = []
    equal = []
    greater = []

    if len(s) > 1:
        pivot = s[len(s)-1]
        for i in s:
            if i<pivot:
                less.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                greater.append(i)

        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return s
