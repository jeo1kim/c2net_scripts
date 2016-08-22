# (*) Useful Python/Plotly tools
import plotly.tools as tls
import numpy as np
import plotly
import sqlite3
import xlwt
import matplotlib.pyplot as plt
import xlrd
from xlsxwriter.workbook import Workbook
from plotly import tools
import plotly.plotly as py
from plotly.graph_objs import *

checker = True;
update = False;
Emanelog = True;
a = 1
if (checker):
    for a in range(a, 9, 1):
        # desire number of fragment for this message
        # print "Let's talk about %s." % h
        conn = sqlite3.connect('statistic{0}.db'.format(a))
        c = conn.cursor()
        '''
        c.execute(
            "UPDATE rankrxstat SET Time = (Time - (SELECT Time from messagecreatetime WHERE MessageID='afca10ff-87ef-46bc-9cd5-69d8ce76c5d3') ) where  (MessageID='afca10ff-87ef-46bc-9cd5-69d8ce76c5d3') ")
        '''
        c.execute(
            "UPDATE rankrxstat SET Time = (Time - (SELECT Time from messagecreatetime WHERE MessageID='385d76f6-2124-4482-a4af-49a1470b2cdc') ) ")

        conn.commit()

        c.execute("UPDATE beaconrxstat SET Time = (Time - (SELECT Time from messagecreatetime WHERE MessageID='385d76f6-2124-4482-a4af-49a1470b2cdc') )")

        conn.commit()

    conn.commit()
if (update):
    conn = sqlite3.connect('statistic5.db')
    c = conn.cursor()
    c.execute(
        "UPDATE rankrxstat SET MessageID =3 where MessageID=4 ")
    conn.commit()
a=1
if (Emanelog):
    for a in range(a, 9, 1):
        # desire number of fragment for this message
        # print "Let's talk about %s." % h
        conn = sqlite3.connect('statistic{0}.db'.format(a))
        c = conn.cursor()

        c.execute(
            "UPDATE emanelog SET dropTime = (dropTime - (SELECT Time from messagecreatetime WHERE MessageID='385d76f6-2124-4482-a4af-49a1470b2cdc'))")
        conn.commit()
    conn.commit()

'''
1e6951d8-2022-4f6a-b532-bca5818e6e8a
'''
