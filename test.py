used_links = []
with open('links.txt', 'r') as file:
     for lines in file:
          used_links.append(lines)
print(used_links)
for item in used_links:
     print(item)


     if pot_link in used_links:
          print(pot_link + ' has been used')
          i = i + 1
     elif pot_link2 in used_links:
          print(pot_link + ' has been used')
          i = i + 1
     else:
          next_link = pot_link
          with open('links.txt', 'a') as file:
               file.write('\n')
               file.write(next_link)
          print(next_link)
          break