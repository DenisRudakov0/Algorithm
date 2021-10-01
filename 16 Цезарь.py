from math import *

def lower_en(i, n):
    en = 'abcdefghijklmnopqrstuvwxyz'
    return en[(en.index(i) + n) % 26]

def upper_en(i, n):
    en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return en[(en.index(i) + n) % 26]
    
def symbol_s(n):
    dl = len(n)
    for i in range(len(n)):
        if n[i] in '"",.!@#$%^&*()-=+=':
            dl -= 1
    return dl

s, sms = input().split(), []
for i in range(len(s)):
    n = len(s[i])
    count = 0
    for j in range(len(s[i])):
        if count == 0:
            n = symbol_s(s[i])
            count += 1
        if s[i][j] in 'abcdefghijklmnopqrstuvwxyz':
            sms.append(lower_en(s[i][j], n))
        elif s[i][j] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            sms.append(upper_en(s[i][j], n))
        else:
            sms.append(s[i][j])
    sms.append(' ')
sms = ''.join(sms)
print(sms)
