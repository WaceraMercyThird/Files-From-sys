from re import T
from sys import argv

script, filename=argv

f = open("demofile.txt", "r")
print(f.read())

print(f"This is file {filename}")
print(f"Open and read the file")
input() # write the name for the file to ba opened

#open the file in a different file
f = open("sample2.txt", "r")
print(f.read())

#return first five characters in a file 
f = open("sample2.txt", "r")
print(f.read(5))
print(" ")

#read one line of the file

f = open("sample2.txt", "r")
print(f.readline())
print(f.readline())

#loop line by line

t = open("demofile.txt", "r")
for x in t:
  print(x)



f.close()