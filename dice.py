import csv 
import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px

data=pd.read_csv("data.csv")

fig =ff.create_distplot([data["Height"].tolist()],["Height"],show_hist=False)

fig.show()