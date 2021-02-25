import ArticleInfo
with open('links.txt', 'r') as file:
     used_links = file.readlines()
print(used_links)


link_ready = False
temp_list = []
i = 0

while i < len(ArticleInfo.links):
     pot_link = ArticleInfo.links[i]
     pot_link2 = ArticleInfo.links[i] + '\\n'
     print(pot_link2)
     if pot_link not in used_links and pot_link2 not in used_links:
          next_link = pot_link
          with open('links.txt', 'a') as file:
               file.write('\n')
               file.write(next_link)
          print(next_link)
          break
     else:
          print(pot_link + ' has been used')
          i = i + 1