import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data1.csv")
data = df["Avg Rating"].tolist()

curve = ff.create_distplot([data],["Height Distribution Curve"], show_hist=False)
curve.show()