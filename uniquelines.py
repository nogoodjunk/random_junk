#!/usr/bin/env python

f = open("feedlist.txt", "r")
f2 = open("feedlistUnique.txt", "w")
uniquelines = set(f.read().split("\n"))
uniquelines = [line for line in uniquelines if line != '']
f2.write("".join([line + "\n" for line in uniquelines]))
f2.close()
