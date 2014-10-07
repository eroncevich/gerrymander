import sys
import string
from copy import copy, deepcopy
M = []
m=0
n=0


def main():
  global m
  global n
  inFile = open("smallNeighborhood.txt","r")
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
  finished = False
  pNode = Node(None)
  iterate(D,pNode,-1)

def iterate(D, pNode, num):
  global m
  global n
  finished = True

  #Check Vert Lines
  for j in range(0,n):
    if(vertLine(D,j)):
      cNode = Node(pNode)
      pNode.addChild(cNode)
      newD = deepcopy(D)
      for i in range(0,m):
        newD[i][j] = num+1
      iterate(newD,cNode,num+1)
      finished = False

  #Check Horz Lines
  for i in range(0,m):
    if(horzLine(D,i)):
      cNode = Node(pNode)
      pNode.addChild(cNode)
      newD = deepcopy(D)
      for j in range(0,n):
        newD[i][j] = num+1
      iterate(newD,cNode,num+1)
      finished = False

  if finished:
    print score(D,num)
    print D
  #print D
  return

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

main()
