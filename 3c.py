import datetime
f = open("movie_titles.csv", encoding ="cp1252")


earliestDate = datetime.datetime(5000, 5, 3)
latestDate = datetime.datetime(1000, 5, 3)

data_lines = open("combined_data_1.txt", "r").readlines()
for line in data_lines:
  if ":" not in line:
    chars = line.split(",")
    date = chars[2]
    dates = date.split("-")
    d1 = datetime.datetime(int(dates[0]), int(dates[1]), int(dates[2]))
    if d1 < earliestDate:
      earliestDate = d1
    
    if d1 > latestDate:
      latestDate = d1

data_lines2 = open("combined_data_2.txt", "r").readlines()
for line in data_lines2:
  if ":" not in line:
    chars = line.split(",")
    date = chars[2]
    dates = date.split("-")
    d1 = datetime.datetime(int(dates[0]), int(dates[1]), int(dates[2]))
    if d1 < earliestDate:
      earliestDate = d1
    
    if d1 > latestDate:
      latestDate = d1


data_lines3 = open("combined_data_3.txt", "r").readlines()
for line in data_lines3:
  if ":" not in line:
    chars = line.split(",")
    date = chars[2]
    dates = date.split("-")
    d1 = datetime.datetime(int(dates[0]), int(dates[1]), int(dates[2]))
    if d1 < earliestDate:
      earliestDate = d1
    
    if d1 > latestDate:
      latestDate = d1

data_lines4 = open("combined_data_4.txt", "r").readlines()
for line in data_lines4:
  if ":" not in line:
    chars = line.split(",")
    date = chars[2]
    dates = date.split("-")
    d1 = datetime.datetime(int(dates[0]), int(dates[1]), int(dates[2]))
    if d1 < earliestDate:
      earliestDate = d1
    
    if d1 > latestDate:
      latestDate = d1

print(earliestDate)
print(latestDate)
