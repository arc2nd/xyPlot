#!/usr/bin/python
##James Parks 2017-07-15

import os
import sys
import json
import types
import numpy as np
import pygal
from optparse import OptionParser


def parse_args(allArgs):
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
    return options, args

def pgPlot(options):
    ##acquire/massage data
    ##  if points passed in via command line
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

    ##  if points passed in via JSON file
    if options.data:
        if os.path.exists(options.data):
            with open(options.data, 'r') as fp:
                data_dict = json.load(fp)
            """if type(data_dict) is types.ListType:
                plot_sets = data_dict
                #for thisList in dataDict:
                x_vals = plot_sets[0]
                y_vals = plot_sets[1]
            elif type(data_dict) is types.DictType:
                plot_labels = [] 
                plot_sets = []
                for this_key in data_dict.keys():
                    plot_labels.append(this_key)
                    plotLists = data_dict[this_key]
                    for this_list in plot_lists:
                        plot_sets.append(this_list)
            else:
                print "Malformed input data file"
                return"""

    ##whoops, did we get x and y mixed up?
    if options.swap:
        x_vals = plot_sets[1]
        y_vals = plot_sets[0]

    ##Set up a couple of variables that will be used in all types of graphs
    #dataKeys = dataDict.keys()
    color_cycle = ["r", "g", "b", "c", "m", "y", "k"]
    text_offset = .25
    small_font = 6
    medium_font = 10
    large_font = 16

    svg_str = None

    ##prep the graph config
    config = pygal.Config()
    config.show_legend = True
    config.width = int(options.width) * 100
    config.height = int(options.height) * 100

    ##what kind of graph are we making?
    if options.graphType:
        ##########################################################
        ##I'm makin' me a line graph, jus like dem fancy injuneers
        ##########################################################
        if options.graphType.lower() == "line":
            #line_graph = pygal.Line()
            line_graph = pygal.XY(config, dynamic_print_values=True, show_x_guides=options.grid, show_y_guides=options.grid, x_label_rotation=45)
            print('label: {0}'.format(str(options.label)))
            line_graph.title = str(options.label)
            for this_key in data_dict:
                print('{0}: {1}'.format(this_key, data_dict[this_key][0]))
                print('{0}: {1}'.format(this_key, data_dict[this_key][1]))
                print('len x: {0}. len y: {1}'.format(len(data_dict[this_key][0]), len(data_dict[this_key][1])))
    
                if '.sample' in this_key.lower():
                    from scipy.interpolate import splev, splrep
                    xValues = data_dict[this_key][0]
                    yValues = data_dict[this_key][1]
                    tck = splrep(xValues, yValues)
                    x2 = np.linspace(xValues[0], xValues[-1], 200)
                    y2 = splev(x2, tck)
                    xy2 = []
                    i=0
                    for i in range(0, len(x2)):
                        xy2.append( (x2[i], y2[i]) )
                    #line_graph.add(this_key, y2, show_dots=False)
                    line_graph.add(this_key, xy2, show_dots=False)
                else:
                    xy = []
                    i = 0
                    for i in range(0, len(data_dict[this_key][1])):
                        xy.append( (data_dict[this_key][0][i], data_dict[this_key][1][i]) )
                    #line_graph.add(this_key, data_dict[this_key][1])
                    line_graph.add(this_key, xy)

            svg_str = line_graph.render()

    if svg_str:
        svg_path = '/home/james/scripts/test.svg'
        fp = open(svg_path, 'w+')
        fp.write(svg_str)
        fp.close()

if __name__ == '__main__':
    options, args = parse_args(sys.argv[1:])
    pgPlot(options)





