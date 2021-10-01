def swap(s,n):
    # Провека исключения
    if n == 0:
        return ('the lord of the rings')
    # Преобразование в двоичную систему счисления
    n1, s1, n2, j = '', '', '', 0
    while n != 0:
        n1 += str(n % 2)
        n = n // 2
    n1 = n1[::-1]
    # Создание строки битов такого же размера, как и нашего текстового сообщения
    for i in range(len(s)):
        if s[i] != ' ' and (s[i] not in '!?.,@#$%^&*():;""'):
            n2 += n1[(i - j)  % (len(n1))] 
        else:
            n2 += ' '
            j += 1            
    # Алгоритм изменения символов если соответствует "1"
    for i in range(len(s)):
        if n2[i] == ' ':
            s1 += s[i]
        elif n2[i] == '0':
            s1 += s[i]
        elif n2[i] == '1':
            if s[i] == s[i].upper():
                s1 += s[i].lower()
            else:
                s1 += s[i].upper()
    return(s1)
