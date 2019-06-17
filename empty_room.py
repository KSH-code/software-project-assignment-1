def time(n):
    m = n.split(":")
    return int(m[0]) * 60 + int(m[1])
{
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
  '425': [
    set(range(time('9:00'), time('10:45'))) |
    set(range(time('11:00'), time('12:45'))) |
    set(range(time('13:00'), time('14:45'))) |
    set(range(time('16:00'), time('17:00')))
  ]
}
monRoom445 = (range(time('10:30'), time('11:45')), range(time('18:00'), time('20:00')))
tueRoom445 = (range(time('09:00'), time('10:15')), range(time('10:30'), time('11:45')), range(time('12:00'), time('13:15')), range(time('18:30'), time('22:00')))
wedRoom445 = (range(time('10:30'), time('11:45')))
thuRoom445 = (range(time('12:00'), time('13:15')))
friRoom445 = (range(time('10:30'), time('12:45')))
monRoom611 = (range(time('11:00'), time('13:00')), range(time('13:00'), time('15:00')))
tueRoom611 = (range(time('10:30'), time('11:45')), range(time('15:00'), time('16:15')), range(time('16:30'), time('17:45')))
wedRoom611 = (range(time('10:30'), time('11:45')), range(time('13:30'), time('16:15')), range(time('16:30'), time('17:45')), range(time('18:00'), time('20:00')))
thuRoom611 = (range(time('09:00'), time('10:00')), range(time('10:30'), time('11:45')), range(time('13:00'), time('14:45')), range(time('15:00'), time('15:15')), range(time('16:30'), time('17:45')), range(time('18:00'), time('20:00')))
friRoom611 = (range(time('13:00'), time('14:00')))
