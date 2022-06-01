# to delete a file import os

from sys import argv
import os

script, filename=argv

f = open("sample.txt", 'w')

os.remove("sample.txt")