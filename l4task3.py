import string 
def frequent_words():
  str1 = []
  fout = open("file1.txt",'r')
  r = fout.readlines()
  for line in r:
    str2 = line.lower().strip(string.punctuation + string.whitespace)
    str1 += str2

  max = 10
  for u in str1 :
    if str1.count(u) > max:
      max = str1.count(u)
      print(u)
  print(max)


print(frequent_words())


