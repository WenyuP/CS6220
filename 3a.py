f = open("movie_titles.csv", encoding ="cp1252")
count = 0
data_lines = open("combined_data_1.txt", "r").readlines()
for line in data_lines:
  if ":" not in line:
    count = count + 1

data_lines2 = open("combined_data_2.txt", "r").readlines()
for line in data_lines2:
  if ":" not in line:
    count = count + 1

data_lines3 = open("combined_data_3.txt", "r").readlines()
for line in data_lines3:
  if ":" not in line:
    count = count + 1

data_lines4 = open("combined_data_4.txt", "r").readlines()
for line in data_lines4:
  if ":" not in line:
    count = count + 1
    
print(count)
