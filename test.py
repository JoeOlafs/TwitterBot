used_links = []
used_links_check = []

with open('links.txt', 'r') as file:
     for lines in file:
          used_links.append(lines)
print(used_links)

for lines in used_links:
     used_links_check.append(lines.strip())

for item in used_links:
     print(item)
for item in used_links_check:
     print(item)
