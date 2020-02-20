# from object_file import *
filename = 'a_example.txt'
f = open('files/'+filename, 'r')

BOOKS, LIBS, DAYS = map(int, f.readline().split())

print(BOOKS, LIBS, DAYS)