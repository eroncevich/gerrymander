import sys
import string
from copy import copy, deepcopy
M = []
m=0
n=0
count =0;


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
  finished = False
  pNode = Node(None)
  #print bestScore, bestD, fFlag
  while(not finished):
    (bestScore,D, finished) = iterate(D,-1)
  print bestScore, D, fFlag
def iterate(D, num):
  global m
  global n
  global count

  if(m==8):
    blockSize = 3
  else:
    blockSize = 2

  if(num>2):
    return (score(D,num), D, False)
  finished = True

  isMax = num % 2
  myBest= m*n if isMax else -m*n

  #Check Vert Lines
  for j in range(0,n):
    if(vertLine(D,j)):
      newD = deepcopy(D)
      for i in range(0,m):
        newD[i][j] = num+1
      (cBest,cD, ff) = iterate(newD,num+1)
      if(isMax and cBest<myBest):
        myBest = cBest
        bestD = cD
        fFlag = ff
      elif((not isMax)and cBest>myBest):
        myBest = cBest
        bestD = cD
        fFlag = ff
      finished = False

  # #Check Horz Lines
  # for i in range(0,m):
  #   if(horzLine(D,i)):
  #     cNode = Node(pNode)
  #     pNode.addChild(cNode)
  #     newD = deepcopy(D)
  #     for j in range(0,n):
  #       newD[i][j] = num+1
  #     iterate(newD,cNode,num+1)
  #     finished = False

  #Check Square
  for i in range(0,m-blockSize+1):
    for j in range(0,n-blockSize+1):
      if(square(D,i,j,blockSize)):
        newD = deepcopy(D)
        for i1 in range(i,i+2):
          for j1 in range(j,j+2):
            newD[i1][j1] = num+1
        (cBest,cD,ff) = iterate(newD,num+1)
        if(isMax and cBest<myBest):
          myBest = cBest
          bestD = cD
          fFlag = ff
        elif((not isMax) and cBest>myBest):
          myBest = cBest
          bestD = cD
          fFlag = ff
        finished = False
  if finished:
    return (score(D,num),D,True)

  return (myBest,bestD,fFlag)

def vertLine(D,j):
  global m
  for i in range(0,m):
    if(D[i][j]!=-1):
      return False
  return True
def horzLine(D,i):
  global n
  for j in range(0,n):
    if(D[i][j]!=-1):
      return False
  return True
def square(D,i0,j0,blockSize):
  for i in range(i0,i0+2):
    for j in range(j0,j0+2):
      if(D[i][j] !=-1):
        return False
  return True

def score(D,num):
  global m
  global n
  scoreD = 0
  scoreR =0
  nDem = [0]*(num+1)
  nRep = [0]*(num+1)
  for i in range(0,m):
    for j in range(0,n):
      if(D[i][j] <0):
        continue
      if M[i][j] =='D':
        nDem[D[i][j]] = nDem[D[i][j]]+1
      else:
        nRep[D[i][j]] = nRep[D[i][j]]+1
  for i in range(0,num+1):
    if(nDem[i]>nRep[i]):
      scoreD = scoreD+1
    elif(nDem[i]<nRep[i]):
      scoreR = scoreR+1
  return scoreD-scoreR


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
