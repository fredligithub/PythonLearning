# Below is the sample code for "Online" model that we need pre-set account/pwd
'''
import plotly
plotly.tools.set_credentials_file(username='Fred82Li', api_key='zbSOikFA2i3E9yezA9B4')
'''

import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np
N = 100
random_x = np.linspace(0, 10, N)  # 生成从0到10， 包含100个数字的等差数列
random_y = np.random.randn(N) # randn 这个函数的作用就是从标准正态分布中返回一个或多个样本值

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

# It will generate a file on below web site: https://plot.ly/organize/home
py.iplot(data, filename='Plotly_Basic_Line')
