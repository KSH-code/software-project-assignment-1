def time(n):
    m = n.split(":")
    return int(m[0]) * 60 + int(m[1])
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
