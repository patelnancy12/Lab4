import string 

def count_string():
  str1 = []
  fout = open("file1.txt",'r')
  r = fout.readlines()

  for line in r:
    str2 = line.lower().strip(string.punctuation + string.whitespace)
    str1 += str2

  total = {}
  for word in  str1:
    total[word] = total.get(word, 0) + 1

  words_t = len(str1)
  words_d = len(total.keys())

  print("Total Words : " + str(words_d))
  print("Different Words :" + str(words_d))


print(count_string())
