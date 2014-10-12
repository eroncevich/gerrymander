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
  pNode = Node(None)
  #print bestScore, bestD, fFlag
  lowN=-1
  while(not finished):
    maxRecurse+=5
    (bestScore,D, finished, lowN) = iterate(D,lowN)
    #print lowN, D, finished
  print "Player 1's score:",bestScore
  score(D,0)
  printDistricts(D)
def iterate(D, num):
  global m
  global n
  global count
  global maxRecurse

  if(m==8):
    blockSizeM = 4
    blockSizeN = 2
  else:
    blockSizeM = 2
    blockSizeN = 2

  if(num>=maxRecurse):
    return (score(D,num), D, False, num)
  finished = True

  isMax = num % 2
  myBest= -m*n if isMax else m*n

  #Check Vert Lines
  for j in range(0,n):
    if(vertLine(D,j)):
      newD = deepcopy(D)
      for i in range(0,m):
        newD[i][j] = num+1
      (cBest,cD, ff, cN) = iterate(newD,num+1)
      if((isMax and cBest>myBest) or((not isMax)and cBest<myBest)):
        myBest = cBest
        bestD = cD
        fFlag = ff
        lowN = cN
      finished = False

  #Check Square
  for j in range(0,n-blockSizeN+1):
    if(square(D,j,blockSizeN)):
      newD = deepcopy(D)
      iteration =0
      for iteration in range(0,m/blockSizeM):
        i0 = iteration*blockSizeM
        for i1 in range(i0,i0+blockSizeM):
          for j1 in range(j,j+blockSizeN):
            newD[i1][j1] = num+iteration*m+1
      (cBest,cD,ff,cN) = iterate(newD,num+1)
      if(num==-1 and i==0 and j==3):
        printDistricts(cD), cBest, myBest
        printDistricts(bestD)
      if((isMax and cBest>myBest)or((not isMax) and cBest<myBest)):
        myBest = cBest
        bestD = cD
        fFlag = ff
        lowN = cN
      finished = False
  if finished:
    return (score(D,num),D,True, num)

  return (myBest,bestD,fFlag,lowN)

def vertLine(D,j):
  global m
  for i in range(0,m):
    if(D[i][j]!=-1):
      return False
  return True

def square(D,j0, blockSizeN):
  global m
  for i in range(0,m):
    for j in range(j0,j0+blockSizeN):
      if(D[i][j] !=-1):
        return False
  return True

def score(D,num):
  global m
  global n
  scoreD = 0
  scoreR = 0
  nScore = {}
  for i in range(0,m):
    for j in range(0,n):
      if(D[i][j] <0):
        continue
      if(D[i][j] not in nScore):
        nScore[D[i][j]]=0
      if M[i][j] =='D':
        nScore[D[i][j]] +=1
      else:
        nScore[D[i][j]] -=1
  for key, score in nScore.iteritems():
    if score>0:
      scoreD+=1
    elif score<0:
      scoreR+=1
  return scoreD-scoreR

def printDistricts(D):
  global m
  global n
  for i in range (0,m):
    for j in range (0,n):
      print M[i][j],D[i][j], " ",
    print ""


class Node:
  def __init__(self,parentN):
    self.children = []
    self.parent = parentN
    self.score = -1
  def addChild(self,child):
    self.children.append(child)
  def setScore(self,points):
    self.score = points

main()
