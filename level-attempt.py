import pandas as pd
import csv
import plotly.express as px
dx = pd.read_csv("level-attempt.csv")
mean = dx.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
fig = px.scatter(mean, x = "student_id" , y = "level", size = "attempt", color = "attempt")
fig.show()