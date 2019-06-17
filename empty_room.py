def time(n):
    m = n.split(':')
    return int(m[0]) * 60 + int(m[1])

def day_to_number(s):
  return {'월': 0, '화': 1, '수': 2, '목': 3, '금': 4}[s]

classroom_info = {
  '424': [
    set(range(time('11:00'), time('12:45'))),
    set(range(time('9:00'), time('10:45'))) |
    set(range(time('11:00'), time('12:45'))) |
    set(range(time('13:00'), time('14:45'))) |
    set(range(time('18:00'), time('20:00'))),
    set(range(time('9:00'), time('10:45'))) |
    set(range(time('11:00'), time('12:45'))) |
    set(range(time('13:00'), time('14:45'))),
    set(range(time('13:00'), time('14:45'))) |
    set(range(time('15:00'), time('16:45'))) |
    set(range(time('18:00'), time('19:00'))),
    set(range(time('15:00'), time('16:45'))) |
    set(range(time('18:30'), time('21:00')))
  ],
  '445': [
    set(range(time('10:30'), time('11:45'))) |
    set(range(time('18:00'), time('20:00'))),
    set(range(time('09:00'), time('10:15'))) |
    set(range(time('10:30'), time('11:45'))) |
    set(range(time('12:00'), time('13:15'))) |
    set(range(time('18:30'), time('22:00'))),
    set(range(time('10:30'), time('11:45'))),
    set(range(time('12:00'), time('13:15'))),
    set(range(time('10:30'), time('12:45')))
  ],
  '611': [
    set(range(time('11:00'), time('13:00'))) |
    set(range(time('13:00'), time('15:00'))),
    set(range(time('10:30'), time('11:45'))) |
    set(range(time('15:00'), time('16:15'))) |
    set(range(time('16:30'), time('17:45'))),
    set(range(time('10:30'), time('11:45'))) |
    set(range(time('13:30'), time('16:15'))) |
    set(range(time('16:30'), time('17:45'))) |
    set(range(time('18:00'), time('20:00'))),
    set(range(time('09:00'), time('10:00'))) |
    set(range(time('10:30'), time('11:45'))) |
    set(range(time('13:00'), time('14:45'))) |
    set(range(time('15:00'), time('15:15'))) |
    set(range(time('16:30'), time('17:45'))) |
    set(range(time('18:00'), time('20:00'))),
    set(range(time('13:00'), time('14:00')))
  ]
}

def search(day, start_time, end_time):
  start_minutes = time(start_time)
  end_minutes = time(end_time)
  day = day_to_number(day)
  classroom_numbers =[]
  for classroom_number in classroom_info.keys():
    minutes_count = 0
    for i in range(start_minutes, end_minutes):
      if i not in classroom_info[classroom_number][day]:
        minutes_count += 1
    if minutes_count >= 30:
      classroom_numbers.append(classroom_number)
  return classroom_numbers

print(search('월', '10:01', '10:31'))
