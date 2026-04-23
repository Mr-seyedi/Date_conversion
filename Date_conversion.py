# - تبدیل تاریخ شمسی به میلادی و بالعکس

# با در نظر گرفتن سال کبیسه و ماه های مختلف
#توجه: این کد یک تبدیل ساده است و ممکن است در برخی موارد خاص دقیق نباشد. برای استفاده دقیق تر، بهتر است از کتابخانه های معتبر مانند `datetime` یا `jdatetime` استفاده کنید.
# کاربر باید ابتدا مشخص کند چه تبدیلی میخواهد انجام شود ( شمسی به میلادی یا بلعکس )
# pip install jdatetime کتابخانه ای برای کار با تاریخ شمسی در پایتون است که می تواند به راحتی تبدیل بین تاریخ های شمسی و میلادی را انجام دهد. در این کد، ما از این کتابخانه برای انجام تبدیل ها استفاده خواهیم کرد.

import jdatetime
from datetime import date
# تابع 1: چک میکنه آیا سال کبیسه است یا نه
def get_max_day(j_month, j_year):
    if j_month <= 6:
        return 31
    elif j_month <= 11:
        return 30
    else:
        #return 30 if jdatetime.date(j_year, 1, 1).isleap() else 29
        if jdatetime.date(j_year, 1, 1).isleap():
            return 30   # سال کبیسه → ماه 12 سی روز دارد
        else:
            return 29   # سال عادی → ماه 12 بیست و نه روز دارد

# تابع 2: تاریخ شمسی را به میلادی تبدیل میکنه
def jalali_to_gregorian(j_year, j_month, j_day):
    # خط 1: یک تاریخ شمسی میسازیم
    jalali_date = jdatetime.date(j_year, j_month, j_day)
    # خط 2: آن را به میلادی تبدیل میکنیم
    g = jalali_date.togregorian()
    # خط 3: سال، ماه، روز میلادی را برمیگردانیم
    return g.year, g.month, g.day

# تابع 3: تاریخ میلادی را به شمسی تبدیل میکنه
def gregorian_to_jalali(g_year, g_month, g_day):
    g_date = date(g_year, g_month, g_day)
    j = jdatetime.date.fromgregorian(date=g_date)
    return j.year, j.month, j.day

print("Select number of conversion:")
print("1: Jalali to Gregorian")
print("2: Gregorian to Jalali")
print("3: Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    try:
        j_year = int(input("Enter Jalali year: "))
        j_month = int(input("Enter Jalali month: "))
        while j_month < 1 or j_month > 12:
            print("Invalid month. Please enter a value between 1 and 12.")
            j_month = int(input("Enter Jalali month: "))

        max_day = get_max_day(j_month, j_year)
        j_day = int(input("Enter Jalali day: "))
        while j_day < 1 or j_day > max_day:
            print(f"Invalid day. Please enter a value between 1 and {max_day}.")
            j_day = int(input("Enter Jalali day: "))

        print(f"Your Jalali date: {j_year}/{j_month}/{j_day}")
        g_year, g_month, g_day = jalali_to_gregorian(j_year, j_month, j_day)
        print(f"Gregorian date: {g_year}/{g_month}/{g_day}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

elif choice == 2:
    try:
        g_year = int(input("Enter Gregorian year: "))
        g_month = int(input("Enter Gregorian month: "))
        while g_month < 1 or g_month > 12:
            print("Invalid month.")
            g_month = int(input("Enter Gregorian month: "))

        g_day = int(input("Enter Gregorian day: "))
        while g_day < 1 or g_day > 31:
            print("Invalid day.")
            g_day = int(input("Enter Gregorian day: "))

        print(f"Your Gregorian date: {g_year}/{g_month}/{g_day}")
        j_year, j_month, j_day = gregorian_to_jalali(g_year, g_month, g_day)
        print(f"Jalali date: {j_year}/{j_month}/{j_day}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

elif choice == 3:
    print("Goodbye!")