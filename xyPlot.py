#!/usr/bin/env python
##James Parks

import os
import sys
import json
import types
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

def xyPlot(allArgs):
    parser = OptionParser(version="%prog 1.0")

    parser.add_option("-x", "--xValues", dest="xValues", help="The x axis values to plot", metavar="XVAL")
    parser.add_option("-y", "--yValues", dest="yValues", help="The y axis values to plot", metavar="YVAL")
    parser.add_option("--lb", "--label", dest="label", help="A label", metavar="LABEL", default="")
    parser.add_option("--xl", "--xLabel", dest="xLabel", help="X Axis Label", default="")
    parser.add_option("--yl", "--yLabel", dest="yLabel", help="Y Axis Label", default="")
    parser.add_option("--pt", "--ptLabel", dest="ptLabel", action="store_true", help="Label individual data points")
    parser.add_option("-f", "--dataFile", dest="data", help="The json file that contains the data being plotted", metavar="DATA", default="Unknown")
    parser.add_option("-g", "--type", dest="graphType", help="Type of graph to make; Line, Bar, or Pie", metavar="GRAPHTYPE", default="Line")
    parser.add_option("-d", "--grid", dest="grid", action="store_true", help="Include a grid?")
    parser.add_option("-t", "--title", dest="title", help="The title of the graph", metavar="TITLE", default="Plot Title")
    parser.add_option("-p", "--path", dest="path", help="The path of the graph you want to output", metavar="PATH")
    parser.add_option("-l", "--legend", action="store_true", dest="legend", help="Add a legend to the graph")
    parser.add_option("-k", "--xkcd", action="store_true", dest="xkcd", help="Use the XKCD style")
    parser.add_option("-s", "--swap", action="store_true", dest="swap", help="Swap X and Y data sets")
    parser.add_option('--wi', '--width', dest='width', help='png file width in inches', default=5)
    parser.add_option('--he', '--height', dest='height', help='png file height in inches', default=4)

    options, args = parser.parse_args(allArgs)

    if options.xValues and options.yValues:
        xValues = options.xValues.split(",")
        if len(xValues) < 2:
            tryAgain = options.xValues.split("-")
            if len(tryAgain):
                xValues = []
                for thisVal in range(int(tryAgain[0]), int(tryAgain[-1])+1):
                    xValues.append(str(thisVal))

        yValues = options.yValues.split(",")

        dataDict = [xValues, yValues]
        plotSets = dataDict
    plotLabels = [""]

    if options.data:
        if os.path.exists(options.data):
            dataFile = open(options.data)
            dataDict = json.load(dataFile)
            dataFile.close()
            if type(dataDict) is types.ListType:
                plotSets = dataDict
                #for thisList in dataDict:
                xValues = plotSets[0]
                yValues = plotSets[1]
            elif type(dataDict) is types.DictType:
                plotLabels = dataDict.keys()
                plotSets = []
                for thisKey in dataDict.keys():
                    plotLists = dataDict[thisKey]
                    for thisList in plotLists:
                        plotSets.append(thisList)
            else:
                print "Malformed input data file"
                return
    
    if options.swap:
        xValues = plotSets[1]
        yValues = plotSets[0]

    ##Set up a couple of variables that will be used in all types of graphs
    #dataKeys = dataDict.keys()
    colorCycle = ["r", "g", "b", "c", "m", "y", "k"]
    textOffset = .25
    smallFontSize = 6
    mediumFontSize = 10
    largeFontSize = 16

    ##Set the resolution in a roundabout way
    ##    you can only specify the image size in inches and the dpi
    ##    so I made the dpi 100 for easy multiplication
    myFig = pyplot.figure(figsize=[int(options.width), int(options.height)], dpi=100)
    #print myFig

    if options.graphType:
        #print options.graphType
        ##########################################################
        ##I'm makin' me a line graph, jus like dem fancy injuneers
        ##########################################################
        if options.graphType.lower() == "line":
            if options.grid:
                if options.xkcd:
                    with pyplot.xkcd():
                        pyplot.grid(b=True)
                else:
                    pyplot.grid(b=True)
            myPlots = []

            colorChoice = 0
            curPlot = 0
            for xValues, yValues in zip(plotSets[0::2], plotSets[1::2]):
                if options.swap:
                    tempX = xValues
                    xValues = yValues
                    yValues = tempX
                if len(plotLabels) > 0:
                    thisLabel = plotLabels[curPlot]
                else:
                    thisLabel = options.label
                print('Plotting: {0}'.format(thisLabel))
                print('    len(x): {0}'.format(len(xValues)))
                print('    len(y): {0}'.format(len(yValues)))

                if '.sample' in thisLabel.lower():
                    from scipy.interpolate import splev, splrep
                    tck = splrep(xValues, yValues)
                    x2 = np.linspace(xValues[0], xValues[-1], 100)
                    y2 = splev(x2, tck)
                    tempPlot = pyplot.plot(x2, y2, label=thisLabel, linestyle='-', linewidth=1)
                    myPlots.append(tempPlot[0])
                else:
                    tempPlot = pyplot.plot(xValues, yValues, label=thisLabel) #, "-", linewidth=1, label=options.label)
                    pyplot.setp(tempPlot, color=colorCycle[colorChoice], marker='.') #linestyle="-", marker=".", linewidth=1)
                    myPlots.append(tempPlot[0])

                ##Write the value above the dot
                if options.ptLabel:
                    ##    Find out the yLength
                    yLen = pyplot.ylim()[1] - pyplot.ylim()[0]
                    textOffset = (yLen / 100) * 2
                    colorChoice = 0
                    for thisPlot in myPlots:
                        xyData = thisPlot.get_xydata()
                        for entry in xyData:
                            pyplot.text(s=str(entry[1])[:5], x=entry[0], y=entry[1] + textOffset, fontsize=smallFontSize)
                if colorChoice == len(colorCycle) - 1:
                    colorChoice = 0
                else:
                    colorChoice = colorChoice + 1
                curPlot = curPlot + 1

            pyplot.margins(.05, .05)
            #pyplot.minorticks_off()
            pyplot.box(on=True)
            pyplot.xticks(fontsize=6)
            #pyplot.tick_params(top=False, right=False, labelsize=smallFontSize)
            #xTicks = range(int(saniX[0]), int(saniX[-1]) + 1, 1)
            #pyplot.xticks(xTicks)

            #pyplot.xlabel("Version", fontsize=smallFontSize)

        ########################################################
        ##Stone walls do not a prison make, nor iron bars a cage
        ########################################################
        elif options.graphType.lower() == "bar":
            #fig, ax = pyplot.subplots()
            #pyplot.figure(figsize=[5, 4], dpi=100)

            ##Figure out the bar info
            numOfPlots = len(dataDict) / 2
            #barSubGroups = len(dataKeys)
            barWidth = 0.9 / numOfPlots

            ##It's much easier to make this a numpy arange instead of a default python range
            #xPos = np.arange(numOfPlots)

            colorChoice = 0
            myRects = []
            #for thisKey in xValues:

            colorChoice = 0
            plotSubGrp = 1
            curPlot = 0
            for xValues, yValues in zip(plotSets[0::2], plotSets[1::2]):
                if len(plotLabels) > 0:
                    thisLabel = plotLabels[curPlot]
                else:
                    thisLabel = "Nothing"

                numOfValues = len(xValues)
                xPos = np.arange(numOfValues)
                print("xpos: {0}".format(type(xPos)))
                print("barWidth: {0}".format(type(barWidth)))
                print("plotSubGrp: {0}".format(type(plotSubGrp)))
                print("yValues: {0}".format(type(yValues)))
                print("thislabel: {0}".format(type(thisLabel)))
                print("colorChoice: {0}".format(type(colorCycle[colorChoice])))
                xpos = xPos + (barWidth * plotSubGrp)
                print xpos
                print yValues
                print barWidth

                intY = []
                for thisVal in yValues:
                    intY.append(int(thisVal))

                if options.xkcd:
                    with pyplot.xkcd():
                        #thisRects = ax.bar(xPos + (barWidth * curBarSubGroup), keyValues, barWidth, label=thisKey, color=colorCycle[colorChoice])
                        thisRect = pyplot.bar(xPos + (barWidth * plotSubGrp), yValues, barWidth, label=thisLabel, color=colorCycle[colorChoice])
                else:
                    thisRect = pyplot.bar(xPos + (barWidth * plotSubGrp), intY, barWidth, label=thisLabel, color=colorCycle[colorChoice])
                    #thisRect = pyplot.barh(xpos, intY)
                myRects.extend(thisRect)

                ##Write the value above the dot
                if options.ptLabel:
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
                if colorChoice == len(colorCycle) - 1:
                    colorChoice = 0
                else:
                    colorChoice = colorChoice + 1
                plotSubGrp = plotSubGrp + 1



        ###################
        ##Mmmmm,... half-Tau
        ####################
        elif options.graphType.lower() == "pie":
            print "Not Yet Implemented"
            return

        else:
            print "I don't know what kind of graph to make"
            return

        ##Let's optionally add some stuff to every type of graph
        #0=Best, 1=upperRight, 2=upperLeft, 3=lowerLeft, 4=lowerRight, 5=right, 6=centerLeft, 7=centerRight, 8=lowerCenter, 9=upperCenter, 10=center
        if options.legend and options.graphType != "Pie":
            pyplot.legend(loc=0, fontsize=mediumFontSize)

        ##Give it a title
        if options.title:
            #if options.graphType != "Pie":
            #myFig.title(options.title.title(), fontsize=mediumFontSize)
            pyplot.title(options.title.title(), fontsize=mediumFontSize)

        ##X and Y Axis Labels
        if options.xLabel:
            pyplot.xlabel(options.xLabel, fontsize=mediumFontSize)
        if options.yLabel:
            pyplot.ylabel(options.yLabel, fontsize=mediumFontSize)

        pyplot.margins(.05, .05)
        #pyplot.xticks(range(len(versions)), versions, fontsize=smallFontSize)
        #pyplot.minorticks_off()
        pyplot.yticks(fontsize=smallFontSize)
        #pyplot.box(on=True)
        pyplot.tick_params(top=False, right=False)


        ##If there is a path specified, write to that path, otherwise show the image
        if options.path:
            pyplot.savefig(options.path)
        else:
            pyplot.show()

if __name__ == '__main__':
    #print sys.argv[1:]
    xyPlot(sys.argv[1:])
