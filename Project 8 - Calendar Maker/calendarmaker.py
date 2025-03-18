import datetime

week_day_number = {'Sunday':1,'Monday':2,'Tuesday':3,'Wednesday':4,'Thursday':5,'Friday':6,'Saturday':7}
calendar=[]
for i in range(1,29):
    calendar.append(i)

print("Enter the year for the calendar:")
year = int(input('> '))
print("Enter the month for the calendar, 1~12:")
month = int(input('> '))

date = datetime.date(year,month,1)
day_of_the_week = date.strftime("%A")
month_name = date.strftime("%B")

prev_month = 0

if month in [1,3,5,7,8,10,12]:
    days = 31
    if month in [1,8]:
        prev_month = 31
    elif month in[5,7,10,12]:
        prev_month = 30
    else: # month == 3
        prev_month = 28
    for i in range(29,days+1):
        calendar.append(i)
elif month in [4,6,9,11]:
    days = 30
    prev_month = 31
    for i in range(29,days+1):
        calendar.append(i)
else:
    days = 28
    if year % 4 == 0:
        days += 1
        calendar.append(29)
    if day_of_the_week != 'Sunday':
        prev_month = 31

if day_of_the_week == 'Sunday' and days == 28:
    calendar_len = 28
elif (days == 31 and (day_of_the_week == 'Friday' or day_of_the_week == 'Saturday')or (days == 30 and day_of_the_week == 'Saturday')):
    calendar_len = 42
else:
    calendar_len = 35

fix_calendar_len = calendar_len

prev_month_iterator = week_day_number[day_of_the_week]- 1
next_month_days = 1
if not (calendar_len == 28 and day_of_the_week == 'Sunday'):
    while prev_month_iterator > 0:
        calendar.insert(0,prev_month)
        prev_month_iterator -= 1
        prev_month -=1
    while len(calendar) < calendar_len:
        calendar.append(next_month_days)
        next_month_days +=1

print_iterator = int(fix_calendar_len / 7)

j = 0
print(
f'''
                                  {month_name} {year:>4}
...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..
+----------+----------+----------+----------+----------+----------+----------+
|{calendar[j]:<2}        |{calendar[j+1]:<2}        |{calendar[j+2]:<2}        |{calendar[j+3]:<2}        |{calendar[j+4]:<2}        |{calendar[j+5]:<2}        |{calendar[j+6]:<2}        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
''',end=''
)
j += 7
for i in range(print_iterator-1):
    print(
f'''\
|{calendar[j]:<2}        |{calendar[j+1]:<2}        |{calendar[j+2]:<2}        |{calendar[j+3]:<2}        |{calendar[j+4]:<2}        |{calendar[j+5]:<2}        |{calendar[j+6]:<2}        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
''',end='')
    j+=7

