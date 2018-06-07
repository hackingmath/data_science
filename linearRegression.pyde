'''Linear Regression Stats Exercise
June 7, 2018
grid functionality from grid.pyde'''

import csv

#set the range of x-values
xmin=-20
xmax=130

#range of y-values
ymin = -20
ymax = 500

#calculate the range
rangex = xmax - xmin
xmid = (xmin+xmax)/2.0
rangey = ymax - ymin
ymid = (ymin+ymax)/2.0

def setup():
    global xscl, yscl
    size(600,600)
    xscl= width / float(rangex)
    yscl= -height / float(rangey)

def draw():
    global xscl, yscl
    background(255) #white
    translate(width/2,height/2)
    grid(xscl, yscl)
    
    noFill()
    strokeWeight(1) #thicker line
    stroke(0) #black

    #line(0,0,3*xscl,6*yscl)
    #fill(255,0,0)
    #ellipse(3*xscl,6*yscl,10,10)
    dataList = getDataList()
    graphPoints(dataList)
    slope,yint = linreg(dataList)
    println([slope,yint])
        
    strokeWeight(2) #thicker line
    stroke(0,255,0) #green
    graphFunction(slope,yint)
    #fill(0,255,0) #green test point
    #ellipse((108-xmid)*xscl,(392.5-ymid)*yscl,10,10)
 
def f(x,m,b):
    #return 6*x**3 + 31*x**2 + 3*x - 10
    return m*x + b

def graphFunction(m,b):
    x = xmin
    while x <= xmax:
        #stroke(0)
        line((x-xmid)*xscl,(f(x,m,b)-ymid)*yscl,
             (x+0.1-xmid)*xscl,(f(x+0.1,m,b)-ymid)*yscl)
        x += 0.1
        
def graphPoints(pointsList):
    fill(0,0,255) #black
    noStroke()
    for pt in pointsList:
        ellipse((pt[0]-xmid)*xscl,
                (pt[1]-ymid)*yscl,
                10,10)
    
def grid(xscl, yscl):
    '''Draws a grid for graphing'''
    #cyan lines
    '''strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin, xmax + 1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)'''
    stroke(0) #black axes
    strokeWeight(1)
    line((0-xmid)*xscl,(ymin-ymid)*yscl,(0-xmid)*xscl,(ymax-ymid)*yscl)
    line((xmin-xmid)*xscl,(0-ymid)*yscl, (xmax-xmid)*xscl*xscl,(0-ymid)*yscl)
    
def getDataList():
    
    with open("sweden.csv") as csvfile:
        data = csv.reader(csvfile)
        header = next(data) #first row is header
        dataList = []
        for row in data:
            #row = [x,y]
            #change these if you're working with ints
            x = float(row[0])
            y = float(row[1])
            dataList.append([x,y])
        println(dataList)
    return dataList
    
'''Farmdata: [[1910, 139], [1920, 149],
[1930, 157], [1940, 175], [1950, 216],
[1959, 303], [1969, 390], [1978, 449],
[1987, 462], [1997, 487]]'''

#students/books example
'''ex1 = [[36,31],[28,29],[35,34],[39,35],[30,29],
       [30,30],[31,30],[38,38],[36,34],[38,33],
       [29,29],[26,26]]'''

def linreg(data):
    '''Returns the slope and y-intercept of
    line of best fit through a set of points
    input: list like [[x1,y1],[x2,y2],...]
    output: (slope,y-intercept)'''
    n = len(data)

    sumx = sum([row[0] for row in data])
    sumx2 = sum([row[0]**2 for row in data])
    sumy = sum([row[1] for row in data])
    sumxy = sum([row[0]*row[1] for row in data]) 

    a = (n*sumxy - sumx*sumy)/(n*sumx2 - sumx**2)
    b = (1/float(n))*(sumy-a*sumx)
    return a,b

#println(linreg(ex1)) #(0.6727272727272727, 9.3) correct!
#output for dataList: (4.717948717948718, -8926.171794871796)
