#Given a list of points and have to figure out how many 
from random import randint
import math

#Define parameters for the set of numbers
setSize = 10
setDimension = 5
square = False
#Might need to write a function to check validity of parameters

#Create an empty array to keep points in
points = []

def generatePoint(setDimension):
  return [randint(-setDimension,setDimension), randint(-setDimension,setDimension)]

#Populate the array
i = 0
while i < setSize:
  proposedPoint = generatePoint(setDimension)
  #Making sure point isn't already inside the list
  if(proposedPoint not in points):
    points.append(proposedPoint)
  else:
    i -=1
  i += 1

#Adding my own test array
points = [[5,5],[5,0],[5,-5],[0,5],[0,0],[0,-5],[-5,5],[-5,0],[-5,-5]]

#Make a list of lines between each point
class Line():
  #A class that contains two points
  def __init__(self, point1, point2):
    self.p1x = point1[0]
    self.p1y = point1[1]
    self.p2x = point2[0]
    self.p2y = point2[1]
    if(self.p2x - self.p1x != 0):
      self.slope = (self.p2y - self.p1y)/(self.p2x - self.p1x)
    else:
      self.slope = -1

    self.length = math.sqrt( (self.p2x-self.p1x)**2 + (self.p2y + self.p1y)**2 )


#Make lines
def makeLine(point1, point2):
  return Line(point1, point2)

lines = []
for p1 in points:
  #This wacky thing makes it so there is just the right number of lines. Each point only makes a line with the points that haven't yet made lines
  for p2 in points[points.index(p1)+1:]:
    proposedLine = makeLine(p1, p2)
    if proposedLine.slope >= 0:
      lines.append(proposedLine)
  #Maybe only keep line if slope is positive to save time?
print(len(lines))

#Pair up lines if they have the same slope and length
linepairs = []
for l1 in lines:
  for l2 in lines[lines.index(l1)+1:]:
    if(l1.slope == l2.slope):
      linepairs.append([l1, l2])



#Match up pairs of parallel lines
print(len(linepairs))
