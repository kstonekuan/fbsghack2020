import math
from collections import defaultdict

def getNum(start, end):
    startIndex = line.find(start)
    endIndex = line.find(end, startIndex)
    try:
        return int(line[startIndex + len(start):endIndex])
    except ValueError:
        return float(line[startIndex + len(start):endIndex])

line = ""

while 'rgba' not in line:
    line = input()

clusters = defaultdict(dict)
index = 0

while 'rgba' in line:

    height = getNum("height:", "px")
    width = getNum("width:", "px")
    top = getNum("top:", "px")
    left = getNum("left:", "px")
    radius = getNum("border-radius:", "px")
    centerX = left + width / 2
    centerY = top + height / 2

    rgbaIndex = line.find("rgba(")
    closingIndex = line.find(")", rgbaIndex)
    rgba = line[rgbaIndex + len('rgba('):closingIndex].replace(" ", "").split(',')
    maxRgba = max(int(rgba[0]), int(rgba[1]),int(rgba[2]))
    
    clusters[index]['center'] = [centerX, centerY]
    clusters[index]['radius'] = radius
    clusters[index]['colour'] = rgba.index(str(maxRgba))
    clusters[index]['connected'] = list()

    index += 1
    line = input()

for index in clusters:
    for i in range(index + 1, len(clusters)):
        centerOne = clusters[index]['center']
        centerTwo = clusters[i]['center']
        dist = math.sqrt((centerOne[0] - centerTwo[0])**2 + (centerOne[1] - centerTwo[1])**2)
        if dist < clusters[index]['radius'] + clusters[i]['radius'] and clusters[index]['colour'] == clusters[i]['colour']:
            clusters[index]['connected'].append(i)
            clusters[i]['connected'].append(index)

# for key, value in clusters.items():
#     print(key, value)

# A function used by DFS 
def DFSUtil(v, visited, graph): 

    # Mark the current node as visited and print it 
    visited[v]= True
    length = 1
    # Recur for all the vertices adjacent to 
    # this vertex 
    for i in graph[v]['connected']: 
        if visited[i] == False: 
            length += DFSUtil(i, visited, graph)
    
    return length


# The function to do DFS traversal. It uses 
# recursive DFSUtil() 
def DFS(graph): 
    maxLength = 0
    V = len(graph)  #total vertices 

    # Mark all the vertices as not visited 
    visited =[False]*(V) 

    # Call the recursive helper function to print 
    # DFS traversal starting from all vertices one 
    # by one 
    for i in range(V):
        length = 0
        if visited[i] == False: 
            length = DFSUtil(i, visited, graph) 

        maxLength = max(maxLength, length)
        
    
    return maxLength


print(DFS(clusters))