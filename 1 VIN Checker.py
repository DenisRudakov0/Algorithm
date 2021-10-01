def check_vin(number):
    number = number.upper()
    if len(number) != 17 or 'I' in number or 'O' in number or 'Q' in number: 
        return False 
    kod = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
           'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'P': 7,
           'R': 9, 'S': 2, 'T': 3, 'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9}
    decoded = []
    for num in number:
        if num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            decoded.append(int(num))
        else:
            decoded.append(kod.get(num))
    weights = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]
    product = [int(weights[i]) * int(decoded[i]) for i in range(len(decoded))]
    moduls = sum(product) % 11
    if number[8] == str(moduls):
        return True
    elif (moduls == 10 and number[8] == 'X'):
        return True
    else:
        return False
