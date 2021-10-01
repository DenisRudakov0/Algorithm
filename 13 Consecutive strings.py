def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''
    if len(strarr) == 2 and k == 2 and len(strarr[0]) == len(strarr[1]):
        return strarr[0]
    max_length = ''
    for i in range(len(strarr) - (k - 1)):
        s = strarr[i]
        for j in range(1, k):
            s += strarr[i + j]
        if len(max_length) < len(s):
            max_length = s
    return max_length
