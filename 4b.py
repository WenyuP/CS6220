import csv
f = open("movie_titles.csv", encoding ="cp1252")

dict = {}

count = 0

for line in f:
  string = line.split(",", 2)
  dict[string[2]] = dict.get(string[2], 0) + 1


for k in dict.values():
  if k == 4:
    count = count + 1


print(count)
