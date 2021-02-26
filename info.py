from bs4 import BeautifulSoup
import requests
from datetime import date

def gitInfo():
     today = date.today()
     html_text = requests.get('https://github.com/JoeOlafs').text
     soup = BeautifulSoup(html_text, 'lxml')
     dailyContribution = soup.find_all('rect', class_='ContributionCalendar-day')
     for day in dailyContribution:
          if 'data-date' in day.attrs:
               if str(today) == day.attrs['data-date']:
                    contributionToday = day.attrs['data-count']
                    return contributionToday