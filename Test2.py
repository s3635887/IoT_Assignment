import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import plotly.plotly as py
import plotly.graph_objs as go 
import datetime
import pandas as pd
dbname='assignment1.db'
conn = sqlite3.connect(dbname)
query = "select * from ass1_data limit 100"
pf = pd.read_sql_query(query,conn)
print(pf.timestamp)
print(pf.temperature)
plt.plot(pf.timestamp, pf.temperature)
plt.show()
#c = curs.fetchall()

#data=[go.Scatter(
#	x=pf.timestamp,
#	y=pf.temperature)]
#py.iplot(data)
