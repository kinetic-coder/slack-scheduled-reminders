import Utilities.Web as Web
import Utilities.Date as Date
import Utilities.FormattingUtility as Format

from atlassian import Confluence

def get_confluence_page_content(url, api_token, page_id):

    confluence = Confluence(
        url=url,
        token=api_token
    )

    page = confluence.get_page_by_id(page_id, expand='body.storage')
    return page['body']['storage']['value']

def get_grafana_monitors(schedule_collection, week_commencing_date):
    scheduled_staff = None

    for schedule in schedule_collection[:]:
        if schedule["Week commencing"] == week_commencing_date:
            scheduled_staff = schedule
            break

    if scheduled_staff is None:
        raise Exception("No schedule found for this week")
    
    return scheduled_staff

def get_this_weeks_duty_staff(confluence_link: str, confluence_token: str, confluence_page: str):
    
    page_info = schedule = get_confluence_page_content(
        confluence_link,
        confluence_token,
        confluence_page
    )

    page_info_collection = Web.parse_html_table(page_info)

    current_week_commencing_date = Date.get_week_commencing_date()

    duty_staff = get_grafana_monitors(page_info_collection, current_week_commencing_date)
    
    duty_staff_message = "No duty staff found for this week."

    if(duty_staff is not None):
        duty_staff_message = Format.format_scheduling_message(duty_staff)

    return duty_staff_message