import sys
import string
M = []
D =[]
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
  initDMatrix()
  print D
  createTree()

def initDMatrix():
  global m
  global n
  for i in range(0,m):
    D.append([])
    for j in range(0,n):
      D[i].append(0)

def createTree():
  global m
  global n
  finished = False
  pNode = Node(None)
  iterate(D,pNode,0)

def iterate(D, pNode, num):
  global m
  global n
  finished = True

  #Check Vert Lines
  for j in range(0,n):
    if(vertLine(j)):
      cNode = Node(pNode)
      pNode.addChild(cNode)
      newD = D
      for i in range(0,m):
        newD[i][j] = num+1
      iterate(newD,cNode,num+1)
      finished = False

  #Check Horz Lines
  for i in range(0,m):
    if(horzLine(i)):
      cNode = Node(pNode)
      pNode.addChild(cNode)
      newD = D
      for j in range(0,n):
        newD[i][j] = num+1
      iterate(newD,cNode,num+1)
      finished = False

  if finished:
    print D
  return

def vertLine(j):
  global m
  for i in range(0,m):
    if(D[i][j]!=0):
      return False
  return True
def horzLine(i):
  global n
  for j in range(0,n):
    if(D[i][j]!=0):
      return False
  return True

class Node:
  def __init__(self,parentN):
    self.children = []
    self.parent = parentN
    self.score = -1
  def addChild(self,child):
    self.children.append(child)

main()
