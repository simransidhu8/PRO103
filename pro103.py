import plotly.express as px
import pandas as pd

df = pd.read_csv("pro103.csv")
fig = px.scatter(df, x="date", y="cases", color = "country", title="Cases in countries")
fig.show()