import re
from datetime import datetime

dates = ('Sun 10:00-20:00\nFri 05:00-10:00\nFri 16:30-23:50\nSat 10:00-24:00\nSun 01:00-04:00\nSat 02:00-06:00\n'
         'Tue 03:30-18:15\nTue 19:00-20:00\nWed 04:25-15:14\nWed 15:14-22:40\nThu 00:00-23:59\nMon 05:00-13:00\n'
         'Mon 15:00-21:00')


def solution(string):
    max_sleep = 0
    start_sleep_time = '00:00'

    days_order = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    meetings = sorted(re.findall(r"(\w{3})\s(.*?)-(.*?)\n", string), key=lambda x: (days_order[x[0]], x[1]))
    for meeting in meetings:
        if (sleep_minutes := time_diff_mins(start_sleep_time, meeting[1])) > max_sleep:
            max_sleep = sleep_minutes
        start_sleep_time = meeting[2]
    if (sunday_sleep := time_diff_mins(meetings[-1][2], '00:00')) > max_sleep:
        max_sleep = sunday_sleep

    return max_sleep


def time_diff_mins(former, latter):
    former_dt = datetime.strptime(former.replace('24:00', '00:00'), '%H:%M')
    latter_dt = datetime.strptime(latter.replace('24:00', '00:00'), '%H:%M')
    diff = latter_dt - former_dt
    return int(diff.seconds / 60)


print(solution(dates))
