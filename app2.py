import streamlit as st
import jdatetime
from datetime import datetime

st.title("📅 محاسبه سن شما (هجری شمسی)")

# ورودی تاریخ تولد
tavalod = st.text_input("تاریخ تولد خود را به صورت YYYY-MM-DD وارد کنید:")

if tavalod:
    try:
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

        st.success(f"شما {years} سال و {months} ماه و {days} روز دارید. 🎉")

    except Exception as e:
        st.error("فرمت تاریخ اشتباه است! لطفاً به صورت YYYY-MM-DD وارد کنید.")
