from datetime import datetime, timedelta

def subtract_five_days():

    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")


    new_date = current_date - timedelta(days=5)

    print(f"Date after subtracting 5 days: {new_date.strftime('%Y-%m-%d %H:%M:%S')}")
subtract_five_days()
