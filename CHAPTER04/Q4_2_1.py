def number_to_day(num=0):
    if num == 0:
        day = '水曜日'
    elif num = 1:
        day = '木曜日'
    elif num = 2:
        day = '金曜日'
    elif num = 3:
        day = '土曜日'
    elif num = -1:
        day = '火曜日'
    elif num = -2:
        day = '月曜日'
    elif num = -3:
        day = '日曜日'
    else:
        day = '今週より１日超えた曜日'
    return day
