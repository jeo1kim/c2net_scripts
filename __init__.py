# (*) Useful Python/Plotly tools
import plotly.tools as tls
import numpy as np
import plotly
import sqlite3
import os
import xlwt
import matplotlib.pyplot as plt
import xlrd
from xlsxwriter.workbook import Workbook
from plotly import tools
import plotly.plotly as py
from plotly.graph_objs import *


def update_axis(title, tickangle):
    return dict(
        title="Time",  # axis title
        tickfont=dict(size=13),  # font size, default is 12
        tickangle=tickangle,  # set tick label angles
        gridcolor='#FFFFFF',  # white grid lines
        zeroline=False  # remove thick zero line

    )


'''
def make_anno2(text, fontcolor, x):
    return Annotation(
        text=text,  # annotation text
        xref='paper',  # use paper coordinates
        yref='paper',  # for both x and y coords
        x=x,  # x and y position
        y=1.2,  # in norm. coord.
        xanchor='right',  # 'x' at right border of annotation
        font=Font(
            size=12,  # set text font size
            color=fontcolor  # and color
        ),
        showarrow=False,  # no arrow (default is True)
        bgcolor='#F5F3F2',  # light grey background color
        borderpad=10  # set border/text space (in pixels)
    )
'''

col_mtl = '#0F8C79'
col_van = '#BD2D28'
color0 = 'rgb(255,165,0)'
color1 = 'rgb(0, 0, 128)'
color2 = 'rgb(165,42,42)'
color3 = 'rgb(34,139,34)'
color4 = 'rgb(139,69,19)'
color5 = 'rgb(139,139,131)'
color6 = 'rgb(218,165,32)'
color7 = 'rgb(219,112,147)'
color8 = 'rgb(199,21,133)'
beacon = True;
database = False;
a = 1
if (database):
    for a in range(a, 9, 1):
        # desire number of fragment for this message
        # print "Let's talk about %s." % h
        conn = sqlite3.connect('statistic{0}.db'.format(a))
        c = conn.cursor()

        c.execute(
            "UPDATE rankrxstat SET Time = (Time - (SELECT Time from messagecreatetime) ) where ( (SELECT MessageID from  messagecreatetime)=(SELECT MessageID from  rankrxstat) )")

        conn.commit()
        c.execute(
            "UPDATE beaconrxstat SET Time = (Time - (SELECT Time from messagecreatetime) ) where (SELECT MessageID from  messagecreatetime)=1")
        conn.commit()
    conn.commit()

a = 1
q = 2

fig = tools.make_subplots(rows=4, cols=2, subplot_titles=('Node-1', 'Node-45',
                                                          'Node-2', 'Node-21', 'Node-10', 'Node-13', 'Node-14',
                                                          'Node-6'))
# for loop base on our number of subplot
for a in range(a, 9, 1):
    # Open excel file to import database information
    workbook = Workbook('rank{0}.xlsx'.format(a))
    # desire number of fragment for this message
    fragmentnum = 0;
    k = fragmentnum;
    # loop through database foe each fragmen and create worksheet for each fragment information
    for k in range(k, -1, -1):
        # print "Let's talk about %s." % h
        h = k
        h = str(h)
        worksheet = workbook.add_worksheet()
        conn = sqlite3.connect('statistic{0}.db'.format(a))
        c = conn.cursor()
        c.execute(
            "select MessageID, FragmentId, CurrentRank, Time FROM RANKRXSTAT WHERE MessageID= ? and FragmentId= ?",
            (1, h))
        mysel = c.execute(
            "select MessageID, FragmentId, CurrentRank, Time FROM RANKRXSTAT WHERE MessageID= ? and FragmentId= ?",
            (1, h))
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write_row(i, 0, row)
    workbook.close()

    if (beacon):
        # Open excel file to import database information
        workbook = Workbook('beacon{0}.xlsx'.format(a))
        # desire number of fragment for this message
        fragmentnum = 1;
        k = fragmentnum;
        # loop through database foe each fragmen and create worksheet for each fragment information
        for k in range(k, 2, 1):
            # print "Let's talk about %s." % h
            h = k
            h = str(h)
            worksheet = workbook.add_worksheet()
            conn = sqlite3.connect('statistic{0}.db'.format(a))
            c = conn.cursor()
            c.execute("select NodeID, SenderID, Time FROM BEACONRXSTAT WHERE Time >= ? and  Time  <= ?",
                      (0, 100))
            mysel = c.execute(
                "select NodeID, SenderID, Time FROM BEACONRXSTAT WHERE Time >= ? and  Time  <=?",
                (0, 100))
            for i, row in enumerate(mysel):
                for j, value in enumerate(row):
                    worksheet.write_row(i, 0, row)
    workbook.close()

    # Read Beacon statistic

    n = 0
    # Plot graph base on information on each excel sheet
    wb = xlrd.open_workbook('rank{0}.xlsx'.format(a))
    for n in range(n, 1, 1):
        sh1 = wb.sheet_by_index(n)
        print sh1.col_values(3)  # column 0
        print sh1.col_values(2)  # column 1
        # sh2 = wb.sheet_by_index(k)
        z = sh1.cell_value(3, 1)  # column 0
        z = int(z)
        # y = sh2.col_values(2)  # column 1

        locals()['trace{0}'.format(n)] = Bar(
            x=sh1.col_values(3),
            y=sh1.col_values(2), xaxis='x{}'.format(a), yaxis='y{}'.format(a),
            marker=Marker(color=locals()['color{0}'.format(n)]), name='FragmentId{0}'.format(z), showlegend=False
        )

    workbook.close()
    if (beacon):
        n = 10
        i = 0
        # Plot graph base on information on each excel sheet
        wb = xlrd.open_workbook('beacon{0}.xlsx'.format(a))

        for n in range(n, 11, 1):
            sh1 = wb.sheet_by_index(0)
            # row_count = sh1.max_row
            print sh1.col_values(2)  # column 0
            print sh1.col_values(1)  # column 1
            # sh2 = wb.sheet_by_index(k)

            if sh1.ncols <= 0:
                z = ' '
            else:
                z = sh1.cell_value(0,0)  # column 0
                z = int(z)

            # y = sh2.col_values(2)  # column 1

            # locals()['trace{0}'.format(n)] = Bar(
            #    x=sh1.col_values(1),
            #   y=sh1.col_values(0), xaxis='x{}'.format(a), yaxis='y{}'.format(a),
            #  marker=Marker(color=locals()['color{0}'.format(n)]), name='FragmentId{0}'.format(z)
            # )
            locals()['trace{0}'.format(n)] = Bar(
                x=sh1.col_values(2),
                y=sh1.col_values(1), xaxis='x{}'.format(a), yaxis='y{}'.format(a),
                marker=Marker(color='#000000'), visible='legendonly', name='Beacons for node{}'.format(z)
            )

    workbook.close()

    # locals()['data{0}'.format(a)] = [trace7, trace6, trace5, trace4, trace3, trace2, trace1]
    # data2 = [trace7, trace6, trace5, trace4, trace3, trace2, trace1]
    # fig['layout'].update(title="Rank Pregression for Message1 on Node-{0}".format(a), xaxis=dict(
    # set x-axis' labels direction at 45 degree angle
    # tickangle=0, title="Time(s)"), yaxis=YAxis(title="Rank Progression"))

    # setting graph layout
    fig['layout'].update(barmode='overlay')

    '''
    annotations=Annotations([

        Annotation(
            x=0.4121875,
            y=0.86809523809523809,
            align='center',
            arrowcolor='#444',
            arrowhead=1,
            arrowsize=1,
            arrowwidth=2,
            ax=-10,
            ay=-50,
            bgcolor='rgba(0, 0, 0, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            borderpad=1,
            borderwidth=1,
            font=Font(
                color='#444',
                family='"Open sans", verdana, arial, sans-serif',
                size=12
            ),
            opacity=10,
            showarrow=True,
            text='<b>Black bars indicating Beacon</b>',
            textangle=0,
            xanchor='auto',
            xref='paper',
            yanchor='auto',
            yref='paper'
        )
    ]))
    '''
    fig['layout']['xaxis{}'.format(a)].update(title="Time".format(a), range=[0, 30], showgrid=True
                                              , autorange=False, showticklabels=True, dtick=1
                                              )
    fig['layout']['yaxis{}'.format(a)].update(title="Current Rank", range=[0, 305], showgrid=True
                                              , autorange=False, showticklabels=True, hoverformat=',f', dtick=30)
    fig['layout'].update(title="Netcast Rank Progression, File size=300KB, no packet loss")
    fig['data'] += [trace0,trace10]

plotly.offline.plot(fig, filename='Netcastnoloss300KB.html'.format(q))
# for q in range(q, 5, 1):

# fig= Figure(data=data, layout=layout)

# fig['data'] +=[trace6]
# fig['data'] +=[trace5]



# plot_url = plotly.offline.plot(fig, filename='angled-text-bar')
# ax.set_ylabel('Time')



# plt.savefig('excel-1.png')
