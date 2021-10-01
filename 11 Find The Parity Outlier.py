def find_outlier(integers):
    if len([i for i in range(len(integers)) if integers[i] % 2 == 0]) < 2:
        num = ''.join([str(integers[i]) for i in range(len(integers)) if integers[i] % 2 == 0])
        return int(num)
    else:
        num = ''.join([str(integers[i]) for i in range(len(integers)) if integers[i] % 2 == 1])
        return int(num)
