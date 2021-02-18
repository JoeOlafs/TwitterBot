from bs4 import BeautifulSoup
import requests
from datetime import date

date = date.today()
print(type(date))
html_text = requests.get('https://github.com/JoeOlafs').text
soup = BeautifulSoup(html_text, 'lxml')
dailyContribution = soup.find_all('rect', class_='ContributionCalendar-day')
for day in dailyContribution:
     if 'data-date' in day.attrs:
          if str(date) == day.attrs['data-date']:
               contributionToday = day.attrs['data-count']