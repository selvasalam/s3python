from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)

date_info = {'current': current_date.strftime('%Y-%m-%d')}
date_info.update({'minus_5_days': new_date.strftime('%Y-%m-%d')})

print("Date Info:", date_info)
