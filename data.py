import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()

curve = ff.create_distplot([data],["Height Distribution Curve"], show_hist=False)
curve.show()