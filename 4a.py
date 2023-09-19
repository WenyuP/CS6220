import csv
f = open("movie_titles.csv", encoding ="cp1252")
count = 0

times = {}

for line in f:
  string = line.split(",", 2)
  times[string[2]] = times.get(string[2], 0) + 1
  

for key in times.keys():
  if times[key] == 1:
    count = count + 1
print(count)
