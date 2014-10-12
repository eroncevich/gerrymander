import sys
import string
from copy import copy, deepcopy
M = []
m=0
n=0
maxRecurse=0
count =0


def main():
  global m
  global n
  inFile = open(sys.argv[1],"r")
  i=0
  for row in inFile:
    j=0
    M.append([])
    for index in row:
      if(index=='\n' or index == ' '):
        continue
      M[i].append(index)
      j=j+1
    i=i+1
  print M
  m = len(M)
  n = len(M[0])
  D = initDMatrix()
  createTree(D)

def initDMatrix():
  global m
  global n
  D =[]
  for i in range(0,m):
    D.append([])
    for j in range(0,n):
      D[i].append(-1)
  return D

def createTree(D):
  global m
  global n
  global count
  global maxRecurse
  maxRecurse =0
  finished = False

  lowN=-1
  while(not finished):
    maxRecurse+=5
    (bestScore,D, finished, lowN) = iterate(D,lowN)
    #print lowN, D, finished
  print "Player 1's score:",bestScore
  score(D)
  printDistricts(D)
def iterate(D, num):
  global m
  global n
  global count
  global maxRecurse

  #if small, choose 2x2, if large choose 4x2
  if(m==8):
    blockSizeM = 4
    blockSizeN = 2
  else:
    blockSizeM = 2
    blockSizeN = 2

  #if too complex and deep, stop, and return current path
  if(num>=maxRecurse):
    return (score(D), D, False, num)
  finished = True

  isMax = num % 2
  myBest= -m*n if isMax else m*n

  #Check Vert Lines mx1
  for j in range(0,m):
    if(vertLine(D,j)):#check if spot is empty
      newD = deepcopy(D)
      for i in range(0,m):#fill in districts
        newD[i][j] = num+1
      (cBest,cD, ff, cN) = iterate(newD,num+1)
      #pick the best number for the min/max depending on turn number
      if((isMax and cBest>myBest) or((not isMax)and cBest<myBest)):
        myBest = cBest
        bestD = cD
        fFlag = ff
        lowN = cN
      finished = False

  #Check Square/Rect
  #This is special because if a rectangle is picked at (i,j)
  #The entire column must be Sqr/Rect for the board to be complete
  #this saves computation time
  for j in range(0,n-blockSizeN+1):
    if(square(D,j,blockSizeN)): #check if spot is empty
      newD = deepcopy(D)
      iteration =0
      for iteration in range(0,m/blockSizeM):
        i0 = iteration*blockSizeM
        for i1 in range(i0,i0+blockSizeM):
          for j1 in range(j,j+blockSizeN):
            newD[i1][j1] = num+iteration*m+1 #fill in districts
      (cBest,cD,ff,cN) = iterate(newD,num+1)
      #pick the best number for the min/max depending on turn number
      if((isMax and cBest>myBest)or((not isMax) and cBest<myBest)):
        myBest = cBest
        bestD = cD
        fFlag = ff
        lowN = cN
      finished = False

  if finished: #all districts are filled in
    return (score(D),D,True, num)
  #returns best district arrangement for Min or max
  return (myBest,bestD,fFlag,lowN)

#checks if spot open
def vertLine(D,j):
  global m
  for i in range(0,m):
    if(D[i][j]!=-1):
      return False
  return True

#checks if spot open
def square(D,j0, blockSizeN):
  global m
  for i in range(0,m):
    for j in range(j0,j0+blockSizeN):
      if(D[i][j] !=-1):
        return False
  return True

def score(D):
  global m
  global n
  scoreD = 0
  scoreR = 0
  nScore = {}
  #go through every square, count Dem vs Rep depending on
  #district as determined by D[i][j]
  for i in range(0,m):
    for j in range(0,n):
      if(D[i][j] <0): #ignore if this location hasn't been assigned Dist
        continue
      if(D[i][j] not in nScore):
        nScore[D[i][j]]=0
      if M[i][j] =='D':
        nScore[D[i][j]] +=1
      else:
        nScore[D[i][j]] -=1
  #count the score of each district
  for key, score in nScore.iteritems():
    if score>0:
      scoreD+=1
    elif score<0:
      scoreR+=1
  #The score is the number of R wins - D wins
  return scoreR-scoreD

def printDistricts(D):
  global m
  global n
  for i in range (0,m):
    for j in range (0,n):
      print M[i][j],D[i][j], " ",
    print ""


main()
