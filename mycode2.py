import jdatetime
from datetime import datetime

def run_my_code():
    tavalod = input('لطفاً تاریخ تولد خود را بصورت YYYY-MM-DD وارد کنید: ')
    year, month, day = map(int, tavalod.split('-'))
    tavalod_date = jdatetime.date(year, month, day)
    today = jdatetime.date.today()
    years = today.year - tavalod_date.year
    months = today.month - tavalod_date.month
    days = today.day - tavalod_date.day

    if days < 0:
        months -= 1
        last_month = today.month - 1 if today.month > 1 else 12
        last_month_year = today.year if today.month > 1 else today.year - 1
        days += (datetime(today.year, today.month, 1) - datetime(last_month_year, last_month, 1)).days

    if months < 0:
        years -= 1
        months += 12

    print(f'شما {years} سال و {months} ماه و {days} روز دارید.')
    
