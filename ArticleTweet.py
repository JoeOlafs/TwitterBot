import ArticleInfo
import time

used_links = []
with open('links.txt', 'r') as file:
     for lines in file:
          used_links.append(lines)
print(used_links)


link_ready = False
temp_list = []
i = 0

while link_ready == False:
     for item in ArticleInfo.links:
          print(item)
          if item not in used_links:
               next_link = item
               print(next_link)
               link_ready = True
               break
          else:
               print(i)
               i = i + 1
               time.sleep(1)

with open('links.txt', 'a') as file:
                    file.write('\n')
                    file.write(next_link)               