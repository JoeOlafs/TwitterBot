from bs4 import BeautifulSoup
import requests

def articleInfo():
     links = []
     html_text = requests.get('https://hashnode.com/featured').text
     soup = BeautifulSoup(html_text, 'lxml')
     #print(soup.prettify())
     articles = soup.find_all('a',target='_blank', class_='block')
     for article in articles:
          if 'https' in article.attrs['href']:
               if article.attrs['href'] not in links:
                    links.append(article.attrs['href'])
     return links
#print(links)

