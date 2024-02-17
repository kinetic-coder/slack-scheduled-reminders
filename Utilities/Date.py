from datetime import datetime, timedelta

def get_week_commencing_date(current_date: datetime) -> str:
    
    date_format = "%d/%m/%Y"

    if isinstance(current_date, str):
        try:
            current_date = datetime.strptime(current_date, date_format)
        except ValueError:
            raise ValueError(f"current_date must be a valid date string in the format {date_format}")
    elif not isinstance(current_date, datetime):
        raise TypeError('current_date must be a datetime object or a string in the format %Y-%m-%d')
    
    start_of_week = current_date - timedelta(days=current_date.weekday())

    return start_of_week.strftime('%d/%m/%Y')