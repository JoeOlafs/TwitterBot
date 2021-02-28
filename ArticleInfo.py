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

def ArticleLink():
     used_links = []
     used_links_check = []

     with open('links.txt', 'r') as file:
          for lines in file:
               used_links.append(lines)

     for line in used_links:
          used_links_check.append(line.strip())

     link_ready = False
     next_link = ''
     i = 0
     article_links = articleInfo()

     while link_ready == False:
          for item in article_links:
               if item not in used_links_check:
                    next_link = item
                    link_ready = True
                    return next_link
                    break
               else:
                    i = i + 1
                    if i == len(article_links):
                         return ''
                         break