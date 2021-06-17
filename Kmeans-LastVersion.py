                        ###################################################################
                        ## this class contains                                           ##    
                        ## - static list of points                                       ##
                        ## - static number of points                                     ##
                        ## - point character / abscissa / ordinate for each point object ##
                        ###################################################################
class Point:
   points = [];
   nbPoints = 0

   def __init__(self, name, x, y):
        self.name = name
        self.x=x
        self.y=y
        Point.nbPoints += 1
        Point.points.append(self) 

## each input casted as integer should be tested using this function
def enterAnInteger(msg):
    var = 0
    while var == False:             
        try:
            var = int(input(msg))
        except ValueError:
            print("\t\tThat's not an int!")
    return var;
    
nbmyPoints = 0  
## entered value should be an integer
nbmyPoints = enterAnInteger("\nEnter the number of Points: ")

## the point character shouln't be empty and the abscissa-ordinate should be an integer
for i in range(nbmyPoints):
    print("\n<< point", i+1, ">>")
    pointChar = ''
    while pointChar == '':    
        pointChar = input("\t\tEnter the character: ")
        if pointChar == '':
            print("\t\tShouldn't be empty!\n")
    x = y = 0
    x = enterAnInteger("\t\tEnter X: ")
    y = enterAnInteger("\t\tEnter Y: ")
    ## point added to the list of points
    p = Point(pointChar, x, y)
    
## print the points available
print("\nPoints Available: [ ", end = '')
for i in range(len(Point.points)-1):
    print(Point.points[i].name,", ", end = '')
print(Point.points[len(Point.points)-1].name, "]")

                                    #############################################################
                                    ## this class contains                                     ##    
                                    ## - static list of clusters                               ##
                                    ## - static number of clusters                             ##
                                    ## - cluster name / list of points for each cluster object ##
                                    #############################################################
class Clus:
    clusList = []
    nClus = 0
    def __init__(self, name, Point):
        self.name = name
        self.Points = []
        
        if len(Clus.clusList) == 0:                     ## in order to prevent duplicate clusters, we've to implement the first one
            Clus.clusList.append(self)                      ## then make the test    
            Clus.nClus += 1
        
        for i in range(len(Clus.clusList)):
            if name == Clus.clusList[i].name:           # already exist
                Clus.clusList[i].Points.append(Point)
                break
            else:
                if i == len(Clus.clusList)-1:           # doesn't exist yet                    
                    self.Points.append(Point)
                    Clus.clusList.append(self)
                    Clus.nClus += 1
      
## the nb of clusters shdn't be greater than the nb of points      
nbClusters = 0  
while nbClusters == False or nbClusters > nbmyPoints: 
    if nbClusters > nbmyPoints:
        print("nb of clusters shd not be greater than nb of points")
    try:
        nbClusters = enterAnInteger("\nEnter the number of clusters: ") 
    except ValueError:
        print("That's not an int!")

## in order to stop the program execution, we've to compare our clusters' list of the current iteration with those of the previous iteration.
## We can't rely on the centroids' coordinates, we can find 2 iterations with the same coordinates but different clusters' list.
## for this purpose i've created this tmp list of list.
tmpClusters = []
for i in range(nbClusters):## here i've initialized the tmp list with empty lists in order to append the points inside them.
    tmpClusters.append([])
    
#########
## i've created an empty list to append to it the centroids points.
CentroidsDict = []
ci = ""
count = 0

print("\nEnter the initial centroids: ")
again = True
while again == True:
    while count < nbClusters:  
        print("\n<< centroid", count+1, ">>")   #end=''
        ci = input("\t\tEnter the character: ")
        
        print("\t\tCentroids: ", CentroidsDict)
        
        cc = 0
        exist = False
        for j in range(len(Point.points)):
            if ci == Point.points[j].name:
                for k in range(len(CentroidsDict)):
                    # duplicate chars so point already exist
                    if Point.points[j].x in CentroidsDict[k] and Point.points[j].y in CentroidsDict[k]:
                        exist = True
            else : cc += 1
        if cc == len(Point.points):
            print("\t\tpoint doesn't exist")
            again = True
            break
        else:
            if exist == True:
                print("\t\tpoint already exist")
                again = True
                break
            else:
                ## add only the points available in our list of points
                for k in range(len(Point.points)):
                    if ci in Point.points[k].name: 
                        ## add the cluster
                        c = Clus("C" + str(count), Point.points[k])
                        tmpClusters[count].append(Point.points[k]) 
                        count += 1
                        ## add the centroid
                        CentroidsDict.append((Point.points[k].x, Point.points[k].y))
                        print("\t\tpoint added successfully")
                        again = False
                        break
        print("\t\tCentroids: ",CentroidsDict)
        
        # print the clusters
        for k in range(len(Clus.clusList)):
            print("\t       ", Clus.clusList[k].name,"= { ", end = '')
            for j in range(len(Clus.clusList[k].Points)-1):
                print(Clus.clusList[k].Points[j].name, ", ", end = '')
            print(Clus.clusList[k].Points[len(Clus.clusList[k].Points)-1].name, "}")
        print()   
    
#########
## pick a method
minDis = mark = clusterIndex2bRemoved = pointIndex2bRemoved = 0
found = False

mthod = ''
while mthod != "euclidienne" and mthod != "manhattan" and mthod != "minkowski":
    mthod = input("choose a method by entering [ euclidienne, manhattan or minkowski ]: ")
print()
if mthod == "euclidienne": 
    print("method picked: ( (x1 - x2)^2 + (y1 - y2)^2 ) ^ 1/2")
if mthod == "manhattan":
    print("method picked: ( |x1 - x2| + |y1 - y2| )")
if mthod == "minkowski":    
    print("method picked: ( |x1 - x2|^n + |y1 - y2|^n ) ^ 1/n")
    nth = enterAnInteger("Enter the nth root : ") 

print();

import math   

ccc = 0
iteration = 0

while ccc != nbClusters:
    iteration += 1
    print("Iteration", iteration)
    
    ## store the point index to remove the duplicates in each iteration
    for i in range(nbmyPoints):
        found = False
        for k in range(nbClusters):
            if Point.points[i] in Clus.clusList[k].Points:  
                for kk in range(len(Clus.clusList[k].Points)):
                    if Point.points[i] == Clus.clusList[k].Points[kk]:
                        found = True
                        clusterIndex2bRemoved = k
                        pointIndex2bRemoved = kk
                        break
        ## euclidienne
        ## i've saved the index of minimum distance in the "mark" variable in order to append the point to the same cluster index. 
        if mthod == "euclidienne":        ## ( (x1 - x2)^2 + (y1 - y2)^2 ) ^ 1/2
            minDis = math.sqrt(((Point.points[i].x - CentroidsDict[0][0])**2  +  (Point.points[i].y - CentroidsDict[0][1])**2))
            #print("minDistance: ", minDis)
            mark = 0
            for j in range(1, len(CentroidsDict)):     
                v = math.sqrt((Point.points[i].x - CentroidsDict[j][0])**2  +  (Point.points[i].y - CentroidsDict[j][1])**2)
                #print("v", v)
                if v < minDis:
                    minDis = v
                    mark = j
                    
                ## when the loop reaches the end here we've to add the point
                if j == len(CentroidsDict)-1:
                    Clus.clusList[mark].Points.append(Point.points[i])
                    
                    ## we've to remove the duplicate old point after the operation getting done.
                    if found:
                        Clus.clusList[clusterIndex2bRemoved].Points.pop(pointIndex2bRemoved)
        ## manhattan
        if mthod == "manhattan":       ## ( |x1 - x2| + |y1 - y2| ) 
            minDis = abs(Point.points[i].x - CentroidsDict[0][0])  +  abs(Point.points[i].y - CentroidsDict[0][1])
            #print("minDistance: ", minDis)
            mark = 0
            for j in range(1, len(CentroidsDict)):     
                v = abs(Point.points[i].x - CentroidsDict[j][0]) +  abs(Point.points[i].y - CentroidsDict[j][1])
                #print("v", v)
                if v < minDis:
                    minDis = v
                    mark = j
                
                if j == len(CentroidsDict)-1:
                    Clus.clusList[mark].Points.append(Point.points[i])
                    
                    if found:
                        Clus.clusList[clusterIndex2bRemoved].Points.pop(pointIndex2bRemoved)  
        ## minkowski
        if mthod == "minkowski":        ## ( |x1 - x2|^n + |y1 - y2|^n ) ^ 1/n
            minDis = ((abs(Point.points[i].x - CentroidsDict[0][0])**nth  +  abs(Point.points[i].y - CentroidsDict[0][1])**nth))**(1/nth)
            #print("minDistance: ", minDis)
            mark = 0
            for j in range(1, len(CentroidsDict)):     
                v = (abs(Point.points[i].x - CentroidsDict[j][0])**nth  +  abs(Point.points[i].y - CentroidsDict[j][1])**nth)**(1/nth)
                #print("v", v)
                if v < minDis:
                    minDis = v
                    mark = j
                
                if j == len(CentroidsDict)-1:
                    Clus.clusList[mark].Points.append(Point.points[i])
                    
                    if found:
                        Clus.clusList[clusterIndex2bRemoved].Points.pop(pointIndex2bRemoved)
           
    X = Y = centerX = centerY = 0

    print()
    ## update the centroids coordinates
    for i in range(nbClusters):
        X = Y = 0 
        for j in range(len(Clus.clusList[i].Points)):
            X += Clus.clusList[i].Points[j].x
            Y += Clus.clusList[i].Points[j].y
        centerX = X/len(Clus.clusList[i].Points)
        centerY = Y/len(Clus.clusList[i].Points)
        CentroidsDict[i] = (centerX, centerY)
    #print("\tCentroids ", CentroidsDict)
    
    ## print the clusters
    for i in range(nbClusters):
        print("       ", Clus.clusList[i].name,"= { ", end = '')
        for j in range(len(Clus.clusList[i].Points)-1):
            print(Clus.clusList[i].Points[j].name, ", ", end = '')
        print(Clus.clusList[i].Points[len(Clus.clusList[i].Points)-1].name, "}", end = '\t'); print("<<", CentroidsDict[i], ">>")
   
    ## stop condition, when the current clusters' list are equals to the previous list "rien ne change"
    ccc = 0
    for i in range(len(tmpClusters)):
        if tmpClusters[i] == Clus.clusList[i].Points:
            ccc += 1
        if  ccc == nbClusters:
            print("\n_-_RIEN NE CHANGE_-_")
            
    ## clear the tmp list and fill it again with the current points to be compared in the next iteration       
    for i in range(nbClusters):
        tmpClusters[i] = []
        for j in Clus.clusList[i].Points:
            tmpClusters[i].append(j)     
    print()