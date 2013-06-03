import os
import sys
import math

map = [
		[8,0,0,0,0,0,0,0,0],
		[0,0,3,6,0,0,0,0,0],
		[0,7,0,0,9,0,2,0,0],
		[0,5,0,0,0,7,0,0,0],
		[0,0,0,0,4,5,7,0,0],
		[0,0,0,1,0,0,0,3,0],
		[0,0,1,0,0,0,0,6,8],
		[0,0,8,5,0,0,0,1,0],
		[0,9,0,0,0,0,4,0,0]
		]

global count

def getPossibleNum(x,y):
	used = {}
	for i in range(9):
		if map[x][i] > 0:
			used[map[x][i]]=True
	for i in range(9):
		if map[i][y] > 0:
			used[map[i][y]]=True
	xs = 3 * (x/3)
	ys = 3 * (y/3)
	for i in range(xs,xs+3):
		for j in range(ys,ys+3):
			if x != i and y != j and map[i][j]> 0:
				used[map[i][j]]=True
	possible = []
	for i in range(1,10):
		if not used.get(i):
			possible.append(i)
	return possible

def printMap():
	for line in map:
		print line		

def fix(i,j):
	if map[i][j] > 0:
		return fixNext(i,j)
	pNum = getPossibleNum(i,j)
	for p in pNum:
		map[i][j] = p
		#print "fixing %d,%d guess %d"%(i,j,p)
		#printMap()
		global count
		count += 1
		fixNext(i,j)
	map[i][j] = 0
	return False

def fixNext(i,j):
	if i == 8 and j == 8:
		printMap()	#we are done
		return True
	elif j == 8:
		return fix(i+1,0)
	else:
		return fix(i,j+1)

def guess():
	fix(0,0)

if __name__=='__main__':
    count = 0
    guess()
    print "\n\nfinishing guessing %d\n"%count