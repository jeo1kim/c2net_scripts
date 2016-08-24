import plotly
import sqlite3
import os
import xlwt
import xlrd
from xlsxwriter.workbook import Workbook
from plotly import tools
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go
import time


def update_axis(title, tickangle):
    return dict(
        title="Time",  # axis title
        tickfont=dict(size=13),  # font size, default is 12
        tickangle=tickangle,  # set tick label angles
        gridcolor='#FFFFFF',  # white grid lines
        zeroline=False  # remove thick zero line

    )
'''CREATE TABLE RANKRXSTAT (NodeID TEXT NOT NULL, SenderID TEXT NOT NULL, MessageID VARCHAR(100) NOT NULL,
FragmentId INT NOT NULL, CurrentRank INT NOT NULL, Time DOUBLE	, FullRank INT,
UNIQUE(FragmentId, SenderID, MessageID, CurrentRank));
CREATE TABLE MESSAGECREATETIME ( MessageID      VARCHAR(35)    ,  Time            DOUBLE);


#### senderid, msgid, delay time, creat time #####

select r.senderid, m.messageid, r.time-(select time from messagecreatetime where messageid=r.messageid), m.time-(select min(time)
from messagecreatetime) as xtime from messagecreatetime m left join rankrxstat r on m.MessageID = r.MessageID
where xtime < 1000 group by m.time order by r.senderid;

'''

from datetime import datetime
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
database=False

'''
conn = sqlite3.connect('statistic2.db')
c = conn.cursor()

query = 'SELECT max(Time) - min(Time) FROM rankrxstat group by messageid'
timeq = 'UPDATE rankrxstat SET Time = (Time - (SELECT Time from messagecreatetime WHERE MessageID=rankrxstat.MessageID) )'

c.execute('SELECT * FROM rankrxstat ORDER BY TIME ASC');
conn.commit()

q= c.execute('select r.senderid, m.messageid, r.time, m.time from messagecreatetime m left join rankrxstat r on m.MessageID = r.MessageID group by m.time order by r.senderid').fetchall()

a= c.execute('select r.senderid, m.messageid, r.time-(select time from messagecreatetime where messageid=r.messageid), m.time-(select min(time) '
             'from messagecreatetime) as xtime from messagecreatetime m left join rankrxstat r on m.MessageID = r.MessageID '
             'where xtime < 1000 group by m.time order by r.senderid').fetchall()

print (a)

b= c.execute('select r.senderid, m.messageid, r.time-(select time from messagecreatetime where messageid=r.messageid), m.time-(select min(time) '
             'from messagecreatetime) as xtime from messagecreatetime m left join rankrxstat r on m.MessageID = r.MessageID '
             'where xtime < 1000 group by m.time order by r.senderid').fetchall()
print (b)
'''

fig = tools.make_subplots(rows=3, cols=1, subplot_titles=('Node-1', 'Node-2', 'Node-3'))

count=1
for count in range (count, 3, 1):
    con = sqlite3.connect('statistic{0}.db'.format(count))
    c = con.cursor()

    q = c.execute(
        'select r.senderid, m.messageid, r.time, m.time from messagecreatetime m left join rankrxstat r on m.MessageID = r.MessageID group by m.time order by r.senderid').fetchall()

    c = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x[3])) for x in q if x[0]=='1']
    d= [time.strftime('%M:%S', time.localtime(x[2])) for x in q if x[0]=='1']

    print (c)

    trace0 = go.Bar(
        x=c,y=d, name = [x[0] for x in q]
    )

    trace1 = go.Bar(
        x=[time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x[3])) for x in q if x[0]=='2'],
        y=[time.strftime('%M:%S', time.localtime(x[2])) for x in q if x[0]=='2'], name = [x[0] for x in q]
    )

    trace1 = go.Bar(
        x=[time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x[3])) for x in q if x[0]=='3'],
        y=[time.strftime('%M:%S', time.localtime(x[2])) for x in q if x[0]=='3'], name = [x[0] for x in q]
    )


    data = Data([trace0, trace1])
    fig += [data]

plotly.offline.plot(fig, filename='Netcastnoloss300KB.html'.format(2))




