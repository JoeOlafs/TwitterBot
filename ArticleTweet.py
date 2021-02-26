import ArticleInfo
import time

used_links = []
used_links_check = []

with open('links.txt', 'r') as file:
     for lines in file:
          used_links.append(lines)
#print(used_links)

for line in used_links:
     used_links_check.append(line.strip())

#print(used_links_check)


link_ready = False
next_link = ''
i = 0

while link_ready == False:
     for item in ArticleInfo.links:
          #print(item)
          if item not in used_links_check:
               next_link = item
               #print(next_link)
               link_ready = True
               break
          else:
               #print(i)
               i = i + 1

if next_link != '':
     tweet = f'Just a quick read for your enjoyment.\nFeatured on @hashnode\n#hashnode #codenewbie\n{next_link}'
     print(tweet)

with open('links.txt', 'a') as file:
     file.write('\n')
     file.write(next_link) 