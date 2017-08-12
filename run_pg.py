#!/usr/bin/python

import datetime
import os
import commands

all_charts = ['sugar', 'sugar2', 'sugarTime2', 'pressure', 'pressure2', 'weight', 'weight2', 'bmi2']

today = datetime.date.today()
fmt_today = '{:%Y%m%d}'.format(today)

for this_chart in all_charts:
    chart_path = '../statsChart/{0}_{1}.json'.format(this_chart, fmt_today)
    if this_chart[-1].isdigit():
        chart_title = this_chart[:-1]
        chart_type = 'date'
    else:
        chart_title = this_chart
        chart_type = 'line'

    if os.path.exists(chart_path):
        cmd = './pgPlot.py -g {0} -f {1} --lb \'{2}\' -d --wi 8 --he 5'.format(chart_type, chart_path, chart_title.title())
        status, output = commands.getstatusoutput(cmd)
        print('status: {0}\n\noutput: {1}\n\n'.format(status, output))
    else:
        print('can\'t find chart file: {0}'.format(chart_path))



