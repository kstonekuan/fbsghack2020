import math

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

rgba = [255, 255, 255]

while 'rgba' in line:
    height = getNum("height:", "px")
    width = getNum("width:", "px")
    top = getNum("top:", "px")
    left = getNum("left:", "px")
    radius = getNum("border-radius:", "px")
    centerX = left + width / 2
    centerY = top + height / 2
    dist = math.sqrt((500 - centerX)**2 + (500 - centerY)**2)
    if dist <= radius:
        rgbaIndex = line.find("rgba(")
        closingIndex = line.find(")", rgbaIndex)
        nextRgba = line[rgbaIndex + len('rgba('):closingIndex].replace(" ", "").split(',')
        for i in range(len(rgba)):
            rgba[i] = (float(nextRgba[i]) * float(nextRgba[3]) + rgba[i] * (1 - float(nextRgba[3]))) # A and a1 is always 1 so ignore
    line = input()

print(f'{rgba[0]:.10f},{rgba[1]:.10f},{rgba[2]:.10f}')