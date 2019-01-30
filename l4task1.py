import string 
print(string.punctuation)

def display_string():

  str1 = []
  fout = open("file.txt",'r')

  for line in fout:
    str2 = line.lower().strip(string.punctuation + string.whitespace)
    str1 += str2
  return str1

print(display_string())
