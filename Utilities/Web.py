from bs4 import BeautifulSoup

def parse_html_table(table_string):
    soup = BeautifulSoup(table_string, 'html.parser')
    table = soup.find('table')

    headers = ['Week commencing', '1st','2nd']

    rows = []
    for row in table.select('tbody tr')[1:]:
        values = [td.text.strip() for td in row.select('td')]
        rows.append(dict(zip(headers, values)))

    return rows