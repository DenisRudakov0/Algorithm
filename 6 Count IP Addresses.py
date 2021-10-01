def ips_between(start, end):
    start, end, count = start.split('.'), end.split('.'), []
    count = [int(end[i]) - int(start[i]) for i in range(4)]
    start = [int(start[i]) for i in range(4)]
    end = [int(end[i]) for i in range(4)]
    num1, num2 = 0, 0
    if start[1] == end[1] and start[2] == end[2] and start[0] == end[0]:
        return count[3]
    elif start[2] < end[2] and start[1] == end[1] and start[0] == end[0]:
        return 255 * count[2] + count[2] + count[3]
    elif start[1] < end[1] and start[0] == end[0]:
        num1 = start[1] * 65535 + 255 * start[2] + start[2] + start[3] + start[1]
        num2 = end[1] * 65535 + 255 * end[2] + end[2] + end[3] + end[1]
        return num2 - num1
    else:
        num1 = start[0] * 16777216 + start[1] * 65535 + 255 * start[2] + start[2] + start[3] + start[1]
        num2 = end[0] * 16777216 + end[1] * 65535 + 255 * end[2] + end[2] + end[3] + end[1] 
        return num2 - num1
