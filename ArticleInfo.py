from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://hashnode.com/featured').text
soup = BeautifulSoup(html_text, 'lxml')
#print(soup.prettify())
articles = soup.find_all('a',target='_blank', class_='block')
for article in articles:
     print(article.text)