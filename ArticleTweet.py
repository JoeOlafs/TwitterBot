import ArticleInfo
with open('links.txt', 'r') as file:
     used_links = file.readlines()
print(used_links)

link_ready = False
i=0
while link_ready == False:
     if ArticleInfo.links[i] in used_links:
          i = i + 1
     else:
          print(ArticleInfo.links[i])
          link = ArticleInfo.links[i]
          #used_links.append(ArticleInfo.links[i])
          with open('links.txt', 'a') as file:
               file.write('\n')
               file.write(ArticleInfo.links[i])
          #print(used_links)
          link_ready = True