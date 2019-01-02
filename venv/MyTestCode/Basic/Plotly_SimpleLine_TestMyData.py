import plotly.plotly as py
import plotly.graph_objs as go

random_x = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
random_y = [2, 4, 6, 0, -2, -3, -8, 10, 9, 3]

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

# It will generate a file on below web site: https://plot.ly/organize/home
py.iplot(data, filename='Plotly_Basic_Line_MyData')
