from datetime import datetime, timedelta

def get_week_commencing_date():
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    return start_of_week.strftime('%d/%m/%Y')