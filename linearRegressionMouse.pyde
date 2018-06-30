'''LInear Regression with Graph
June 29, 2018
with Curtis'''

import csv

#set the range of x-values
xmin = -20
xmax = 130

#range of y-values
ymin = -20
ymax = 500

#calculate the range
rangex = xmax - xmin
xmid = (xmin + xmax)/2.0
rangey = ymax - ymin
ymid = (ymin + ymax) / 2.0

def setup():
    global xscl, yscl
    global dataList
    size(600,600)
    xscl = width/float(rangex)
    yscl = -height/float(rangey)
    #empty dataList 
    #dataList = []#[(-2 , -1), (1, 1), (3, 2)]#getDataList()
    #dataList = getDataList()
    dataList = [[random(500),random(500)] for i in range(200)]
    
def draw():
    global xscl, yscl,dataList
    background(255)#white
    translate(width/2,height/2)
    grid(xscl,yscl)
    #dataList = getDataList()
    graphPoints(dataList)
    if len(dataList)>1:
        noFill()
        strokeWeight(1) #thicker line
        stroke(0) #black
        #uncomment if not doing mouse points 
        #dataList = [(-2 , -1), (1, 1), (3, 2)]#getDataList()
        
        slope,yint = linReg(dataList)
        println([slope,yint])
        #draw line of best fit
        strokeWeight(2) #even thicker line
        stroke(0,255,0) #green
        graphFunction(slope,yint)
        fill(255,0,0) #red
        textSize(18)
        text("y = "+str(round(slope,1))+"x + "+str(round(yint,1)),20,20)
    
def f(x,m,b):
    return m*x + b

def graphFunction(m,b):
    x = xmin
    while x <= xmax:
        #stroke(0)
        line((x-xmid)*xscl, (f(x,m,b)-ymid)*yscl,
            (x+0.1-xmid)*xscl, (f(x+0.1,m,b)-ymid)*yscl)
        x += 0.1

def graphPoints(pointsList):
    fill(0,0,255) #blue
    noStroke()
    for pt in pointsList:
        ellipse((pt[0]-xmid)*xscl,
                (pt[1]-ymid)*yscl,
                10,10)
                
def grid(xscl,yscl):
    stroke(0) #black axes
    strokeWeight(1)
    line((0-xmid)*xscl, (ymin-ymid)*yscl,(0-xmid)*xscl, (ymax-ymid)*yscl)
    line((xmin-xmid)*xscl, (0-ymid)*yscl,(xmax-xmid)*xscl, (0-ymid)*yscl)
    
def getDataList():
    with open("sweden.csv") as csvfile:
        data = csv.reader(csvfile)
        header = next(data) #first row is header
        dataList = []
        for row in data:
            #row = []
            #change these if you're working with ints
            x = float(row[0])
            y = float(row[1])
            dataList.append([x,y])
        #println(dataList)
    return dataList

def linReg(data):
    '''Takes a list of points and
    finds the line of best fit.
    input: list, like [[x1,y1],[x2,y2]...
    ouput: (slope,y-intercept) of line
    '''
    n = len(data) #number of points
    sumx = sum([row[0] for row in data])
    sumx2 = sum([row[0]**2 for row in data])
    sumy = sum([row[1] for row in data])
    sumxy = sum([row[0]*row[1] for row in data])

    a = (n*sumxy - sumx*sumy)/float((n*sumx2 - sumx**2))
    b = (1/float(n))*(sumy-a*sumx)
    return a,b

def mouseDragged():
    global dataList
    dataList.append([(mouseX/float(xscl))+xmid-rangex/2.0,
                     (mouseY/float(yscl))+ymid+rangey/2.0])
    
def mouseClicked():
    global dataList
    dataList.append([(mouseX/float(xscl))+xmid-rangex/2.0,
                     (mouseY/float(yscl))+ymid+rangey/2.0])