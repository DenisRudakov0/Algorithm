def format_duration(seconds):
    time_one = (31536000, 86400, 3600, 60, 1)
    time = []
    answer = ''
    if seconds == 0 or seconds == '':
        return 'now'
    for i in range(len(time_one)):
        time.append(seconds // time_one[i])
        seconds = seconds - (seconds // time_one[i]) * time_one[i]
    if time[0] != 0:
        if time[0] == 1:
            answer += '1 year'
        else:
            answer += str(time[0]) + ' years'
        if time[3] > 0 or time[2] > 0 or time[1] > 0:
            answer += ','           
    if time[1] != 0:
        if time[1] == 1:
            answer += ' 1 day'
        else:
            answer += ' ' + str(time[1]) + ' days'
        if time[3] > 0 or time[2] > 0:
            answer += ','           
    if time[2] != 0:
        if time[2] == 1:
            answer += ' 1 hour'
        else:
            answer += ' ' + str(time[2]) + ' hours'
        if time[3] > 0 and time[4] > 0:
            answer += ','  
    if time[3] != 0:
        if (time[0] > 0 or time[1] > 0 or time[2] > 0) and time[4] == 0:
            answer += ' and'
        if time[3] == 1:
            answer += ' 1 minute'
        else:
            answer += ' ' + str(time[3]) + ' minutes'
    if time[4] != 0:
        if time[0] > 0 or time[1] > 0 or time[2] > 0 or time[3] > 0:
            answer += ' and' 
        if time[4] == 1:
            answer += ' 1 second' + ' '
        else:
            answer += ' ' + str(time[4]) + ' seconds'
    print(time)
    return answer.strip()
