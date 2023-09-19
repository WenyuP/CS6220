dict = {}
count = 0
currMovie = ""
likedMovies = {}

f = open("movie_titles.csv", encoding ="cp1252")
data_lines = open("combined_data_1.txt", "r").readlines()
for line in data_lines:
  if ":" in line:
    chars = chars = line.split(":")
    currMovie = chars[0]

  if ":" not in line:
    chars = line.split(",")
    dict[int(chars[0])] = dict.get(int(chars[0]), 0) + 1
    if chars[1] == "5":
      if chars[0] not in likedMovies:
        likedMovies[chars[0]] = []
      likedMovies[chars[0]].append(currMovie)

    

data_lines2 = open("combined_data_2.txt", "r").readlines()
for line in data_lines2:
  if ":" in line:
    chars = chars = line.split(":")
    currMovie = chars[0]

  if ":" not in line:
    chars = line.split(",")
    dict[int(chars[0])] = dict.get(int(chars[0]), 0) + 1
    if chars[1] == "5":
      if chars[0] not in likedMovies:
        likedMovies[chars[0]] = []
      likedMovies[chars[0]].append(currMovie)
    

data_lines3 = open("combined_data_3.txt", "r").readlines()
for line in data_lines3:
  if ":" in line:
    chars = chars = line.split(":")
    currMovie = chars[0]

  if ":" not in line:
    chars = line.split(",")
    dict[int(chars[0])] = dict.get(int(chars[0]), 0) + 1
    if chars[1] == "5":
      if chars[0] not in likedMovies:
        likedMovies[chars[0]] = []
      likedMovies[chars[0]].append(currMovie)
    

data_lines4 = open("combined_data_4.txt", "r").readlines()
for line in data_lines4:
  if ":" in line:
    chars = chars = line.split(":")
    currMovie = chars[0]

  if ":" not in line:
    chars = line.split(",")
    dict[int(chars[0])] = dict.get(int(chars[0]), 0) + 1
    if chars[1] == "5":
      if chars[0] not in likedMovies:
        likedMovies[chars[0]] = []
      likedMovies[chars[0]].append(currMovie)

res = []
for j in dict.keys():
  if dict[j] == 200:
    res.append(j)
    

movieNames = {}
for line in f:
  string = line.split(",", 2)
  movieNames[string[0]] = string[2]

for n in likedMovies["508"]:
  print(movieNames[n])

