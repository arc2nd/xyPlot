#!/usr/bin/python

import datetime
import os
import commands

all_charts = ['sugar', 'sugar2', 'pressure2', 'weight2', 'bmi2']

today = datetime.date.today()
fmt_today = '{:%Y%m%d}'.format(today)

for this_chart in all_charts:
    chart_path = '../statsChart/{0}_{1}.json'.format(this_chart, fmt_today)
    if this_chart[-1].isdigit():
        this_chart = this_chart[:-1]
    if os.path.exists(chart_path):
        cmd = './pgPlot.py -g line -f {0} --lb \'{1}\' -d --wi 8 --he 5'.format(chart_path, this_chart.title())
        status, output = commands.getstatusoutput(cmd)
        print('status: {0}\n\noutput: {1}\n\n'.format(status, output))
    else:
        print('can\'t find chart file: {0}'.format(chart_path))



