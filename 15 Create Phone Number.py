def create_phone_number(n):
    a = [str(n[i]) for i in range(len(n))]
    return '('+(a[0]+a[1]+a[2])+') '+(a[3]+a[4]+a[5])+'-'+(a[6]+a[7]+a[8]+a[9])
