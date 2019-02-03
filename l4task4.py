# Program to count words and perform various other strig operations...

import string

def frequent_words():

  str1 = []
  fout = open("file1.txt",'r')
  r = fout.readlines()
  for l in fout.readlines():
    l = l.strip()
    w = l.split()

  for line in r:
    str2 = line.lower().strip(string.punctuation + string.whitespace)
    str1 += str2


print(frequent_words())
