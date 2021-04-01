import csv 
import plotly.figure_factory as ff
import pandas as pd

data=pd.read_csv("data.csv")

fig=ff.create_distplot([data["Weight"].tolist()],["Weight"],show_hist=False)

fig.show()