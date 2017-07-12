#!/usr/bin/python
##James Parks

import sys
import json
import matplotlib.pyplot as pyplot
import numpy as np
from optparse import OptionParser


def autolabel(rects, textOffset):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        print height + textOffset
        #pyplot.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, str(height)[:5], ha='center', va='bottom', fontsize=6)
        pyplot.text(rect.get_x() + rect.get_width() / 2., height + textOffset, str(height)[:5], ha='center', va='bottom', fontsize=6)


def plotIt(allArgs):
    parser = OptionParser(version="%prog 1.0")

    #parser.add_option("-x", "--xValues", dest="xValues", help="The x axis values to plot", metavar="XVAL")
    #parser.add_option("-y", "--yValues", dest="yValues", help="The y axis values to plot", metavar="YVAL")
    parser.add_option("-d", "--data", dest="data", help="The json file that contains the data being compared", metavar="DATA", default="Unknown")
    parser.add_option("-g", "--type", dest="graphType", help="Type of graph to make; Line, Bar, or Pie", metavar="GRAPHTYPE", default="Line")
    parser.add_option("-t", "--title", dest="title", help="The title of the graph", metavar="TITLE", default="Default")
    parser.add_option("-p", "--path", dest="path", help="The path of the graph you want to output", metavar="PATH")
    parser.add_option("-l", "--legend", action="store_true", dest="legend", help="Add a legend to the graph")
    parser.add_option("-x", "--xkcd", action="store_true", dest="xkcd", help="Use the XKCD style")

    options, args = parser.parse_args(allArgs)

    ##Open up the JSON data file and turn it back into a dictionary
    dataFilePath = options.data
    dataFile = open(dataFilePath, "r")
    dataDict = json.load(dataFile)
    dataFile.close()

    ##Set up a couple of variables that will be used in all types of graphs
    dataKeys = dataDict.keys()
    colorCycle = ["r", "g", "b", "c", "m", "y", "k"]

    #for thisKey in dataKeys:
    #    versions = dataDict[thisKey].keys()
    #    versions.sort()
    versions = dataDict[dataKeys[0]].keys()
    versions.sort()
    #print versions

    textOffset = .25
    smallFontSize = 6
    mediumFontSize = 10
    largeFontSize = 16

    ##Set the resolution in a roundabout way
    ##    you can only specify the image size in inches and the dpi
    ##    so I made the dpi 100 for easy multiplication
    myFig = pyplot.figure(figsize=[5, 4], dpi=100)
    print myFig

    if options.graphType:
        print options.graphType
        ##########################################################
        ##I'm makin' me a line graph, jus like dem fancy injuneers
        ##########################################################
        if options.graphType == "Line":
            pyplot.grid(b=True)

            myPlots = []
            for thisKey in dataKeys:
                ##Sanitize and Synchronize the versions and values
                saniVersions = []
                saniValues = []
                for thisVersion in versions:
                    ##Sanitize the versions into ints
                    strVersion = str(thisVersion)
                    if strVersion[0] == "v":
                        saniVer = str(strVersion[1:])
                    else:
                        saniVer = str(strVersion)
                    saniVersions.append(int(saniVer))

                    ##Sanitize the values into floats
                    value = dataDict[thisKey][thisVersion]
                    if type(value) == type(""):
                        saniVal = float(value)
                    else:
                        saniVal = value
                    saniValues.append(value)

                if options.xkcd:
                    with pyplot.xkcd():
                        tempPlot = pyplot.plot(saniVersions, saniValues, ".-", linewidth=1, label=thisKey)
                else:
                    tempPlot = pyplot.plot(saniVersions, saniValues, ".-", linewidth=1, label=thisKey)
                myPlots.append(tempPlot[0])

            ##Write the value above the dot
            ##    Find out the yLength
            yLen = pyplot.ylim()[1] - pyplot.ylim()[0]
            textOffset = (yLen / 100) * 2
            colorChoice = 0
            for thisPlot in myPlots:
                xyData = thisPlot.get_xydata()
                for entry in xyData:
                    if options.xkcd:
                        with pyplot.xkcd():
                            pyplot.text(s=str(entry[1])[:5], x=entry[0], y=entry[1] + textOffset, fontsize=smallFontSize)
                    else:
                        pyplot.text(s=str(entry[1])[:5], x=entry[0], y=entry[1] + textOffset, fontsize=smallFontSize)
                colorChoice = colorChoice + 1

            pyplot.margins(.05, .05)
            pyplot.minorticks_off()
            pyplot.box(on=True)
            #pyplot.xticks(fontsize=6)
            pyplot.tick_params(top=False, right=False, labelsize=smallFontSize)
            #xTicks = range(int(saniX[0]), int(saniX[-1]) + 1, 1)
            #pyplot.xticks(xTicks)

            pyplot.xlabel("Version", fontsize=smallFontSize)

        ########################################################
        ##Stone walls do not a prison make, nor iron bars a cage
        ########################################################
        elif options.graphType == "Bar":
            #fig, ax = pyplot.subplots()
            #pyplot.figure(figsize=[5, 4], dpi=100)

            ##Figure out the bar info
            numOfBars = len(versions)
            barSubGroups = len(dataKeys)
            barWidth = 0.75 / barSubGroups

            ##It's much easier to make this a numpy arange instead of a default python range
            xPos = np.arange(numOfBars)

            curBarSubGroup = 0
            colorChoice = 0
            myRects = []
            for thisKey in dataKeys:
                keyValues = []

                #thisPos = p[]
                #for pos in xPos:
                #    xPos[pos] = pos + (barwidth * curBarSubGroup)

                for thisVersion in versions:
                    thisValue = dataDict[thisKey][thisVersion]
                    keyValues.append(thisValue)

                if options.xkcd:
                        with pyplot.xkcd():
                            #thisRects = ax.bar(xPos + (barWidth * curBarSubGroup), keyValues, barWidth, label=thisKey, color=colorCycle[colorChoice])
                            thisRect = pyplot.bar(xPos + (barWidth * curBarSubGroup), keyValues, barWidth, label=thisKey, color=colorCycle[colorChoice])
                else:
                    thisRect = pyplot.bar(xPos + (barWidth * curBarSubGroup), keyValues, barWidth, label=thisKey, color=colorCycle[colorChoice])
                myRects.extend(thisRect)

                curBarSubGroup = curBarSubGroup + 1
                if colorChoice == len(colorCycle) - 1:
                    colorChoice = 0
                else:
                    colorChoice = colorChoice + 1

            ##Write the value above the dot
            ##    Find out the yLength
            yLen = pyplot.ylim()[1] - pyplot.ylim()[0]
            textOffset = (yLen / 100)

            for thisRect in myRects:
                height = thisRect.get_height()
                if options.xkcd:
                        with pyplot.xkcd():
                            pyplot.text(thisRect.get_x() + thisRect.get_width() / 2., height + textOffset, str(height)[:5], ha='center', va='bottom', fontsize=6)
                else:
                    pyplot.text(thisRect.get_x() + thisRect.get_width() / 2., height + textOffset, str(height)[:5], ha='center', va='bottom', fontsize=6)
                #autolabel(thisRects, textOffset)

            pyplot.margins(.05, .05)
            pyplot.xticks(range(len(versions)), versions, fontsize=smallFontSize)
            #pyplot.minorticks_off()
            pyplot.yticks(fontsize=smallFontSize)
            #pyplot.box(on=True)
            pyplot.tick_params(top=False, right=False)

        ####################
        ##Mmmmm,... half-Tau
        ####################
        elif options.graphType == "Pie":
            ##Determine how many subplots there are going to be
            ##    This is specific to pie charts because it's silly
            ##    to plot multiple versions into the same pie chart
            numOfPlots = len(versions)
            numOfCols = 5

            if numOfPlots <= 16:
                numOfCols = 4
            if numOfPlots <= 9:
                numOfCols = 3
            if numOfPlots <= 4:
                numOfCols = 2
            if numOfPlots == 1:
                numOfCols = 1

            #elif 4 < numOfPlots < 6:
            #else:
            #    numOfCols = numOfPlots
            numOfRows = numOfPlots / numOfCols
            if numOfPlots % 4:
                numOfRows = numOfRows + 1
            plotNum = 1

            ##Make a pie for each version
            for thisVersion in versions:
                totalValue = 0.0
                allValues = []

                for thisKey in dataKeys:
                    thisValue = dataDict[thisKey][thisVersion]
                    allValues.append(thisValue)
                    totalValue = totalValue + thisValue
                #print thisVersion + " :: " + str(totalValue)

                percentages = []
                for thisValue in allValues:
                    percentages.append((thisValue / totalValue) * 100)

                if numOfPlots > 1:
                    pyplot.subplot(numOfRows, numOfCols, plotNum)

                autoLabelPie = '%1.1f%%'
                pieLabels = None
                if options.legend:
                    pieLabels = dataKeys


                if options.xkcd:
                    with pyplot.xkcd():
                        if options.legend:
                            patches, texts, autotexts = pyplot.pie(percentages, labels=pieLabels, autopct=autoLabelPie, shadow=False, startangle=90)
                        else:
                            patches, texts, autotexts = pyplot.pie(percentages, labels=pieLabels, autopct=autoLabelPie, shadow=False, startangle=90)
                else:
                    if options.legend:
                        patches, texts, autotexts = pyplot.pie(percentages, labels=pieLabels, autopct=autoLabelPie, shadow=False, startangle=90)
                    else:
                        patches, texts, autotexts = pyplot.pie(percentages, labels=pieLabels, autopct=autoLabelPie, shadow=False, startangle=90)

                texts.extend(autotexts)
                for thisText in texts:
                    thisText.set_fontsize(smallFontSize)
                pyplot.axis('equal')
                pyplot.xlabel(thisVersion, fontsize=smallFontSize)
                plotNum = plotNum + 1

                #pyplot.margins(.1, .1)

        else:
            print "I don't know what kind of graph to make"

        ##Let's optionally add some stuff to every type of graph
        #0=Best, 1=upperRight, 2=upperLeft, 3=lowerLeft, 4=lowerRight, 5=right, 6=centerLeft, 7=centerRight, 8=lowerCenter, 9=upperCenter, 10=center
        if options.legend and options.graphType != "Pie":
            pyplot.legend(loc=0, fontsize=mediumFontSize)

        ##Give it a title
        if options.title:
            #if options.graphType != "Pie":
            #myFig.title(options.title.title(), fontsize=mediumFontSize)
            pyplot.title(options.title.title(), fontsize=mediumFontSize)

        ##If there is a path specified, write to that path, otherwise show the image
        if options.path:
            pyplot.savefig(options.path)
        else:
            pyplot.show()

if __name__ == '__main__':
    print sys.argv[1:]
    plotIt(sys.argv[1:])