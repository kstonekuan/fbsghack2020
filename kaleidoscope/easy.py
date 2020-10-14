line = ""

while 'rgba' not in line:
    line = input()

maxHeight = 0
rgba = ""

while 'rgba' in line:
    heightIndex = line.find("height:")
    pxIndex = line.find("px", heightIndex)
    height = int(line[heightIndex + len('height:'):pxIndex])
    if height > maxHeight:
        maxHeight = height
        rgbaIndex = line.find("rgba(")
        closingIndex = line.find(")", rgbaIndex)
        rgba = line[rgbaIndex + len('rgba('):closingIndex].replace(" ", "")
    line = input()

print(rgba)