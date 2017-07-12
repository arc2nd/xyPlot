import json

path = "./testData.json"

#xValues = range(1,46,1)
xValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

yValues = [66, 56, 70, 72, 67, 68, 70, 71, 74, 69, 72, 70, 70, 70, 72,
           66, 70, 72, 72, 65, 70, 70, 72, 64, 68, 71, 70, 70, 78, 86,
           85, 70, 76, 70, 74, 72, 70, 70, 75, 70, 70, 68, 70, 69, 73]

yValues = [1,2,3,4,5]
y2Values = [2,3,4,5,6]
y3Values = [3,4,5,6,7]

yValues = []

xValues = range(1, len(yValues)+1)

data = [xValues, yValues]

data = [xValues, yValues, xValues, y2Values, xValues, y3Values]

data = {"label1": [xValues, yValues], "label2": [xValues, y2Values], "label3": [xValues, y3Values]}

data = {"working": [[1],[12]], "eating":[[1],[2]], "sleeping":[[1],[8]], "exercising":[[1][2]]}

dataFile = open(path, "w")
json.dump(data, dataFile, indent=4)
dataFile.close()