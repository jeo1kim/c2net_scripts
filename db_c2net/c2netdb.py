import sqlite3
conn = sqlite3.connect('statistic3.db')
c = conn.cursor()

query_avg = 'SELECT AVG(delay) FROM (SELECT max(Time)-min(Time) as delay FROM RANKRXSTAT GROUP BY MessageID)'

query = 'SELECT max(Time) - min(Time) FROM rankrxstat group by messageid'

for row in c.execute(query):
    print row

