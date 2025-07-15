from datetime import datetime

def get_earlier_date():
    date_format = "%Y-%m-%d"

    date1_str = input(f"Enter the first date (format {date_format}): ")

    date2_str = input(f"Enter the second date (format {date_format}): ")

    try:
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        if date1 < date2:
            print(f"The earlier date is: {date1_str}")
        elif date2 < date1:
            print(f"The earlier date is: {date2_str}")
        else:
            print("Both dates are the same.")

    except ValueError:
        print("One or both dates are in the wrong format. Please use YYYY-MM-DD.")

get_earlier_date()
