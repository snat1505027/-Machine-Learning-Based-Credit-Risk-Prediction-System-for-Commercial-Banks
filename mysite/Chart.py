import chart_studio.plotly as py
from plotly.graph_objs import *
py.sign_in('SNAT', 'ooyDeMaNPelPQgGES4Qd')
trace1 = {
  "uid": "cb2558", 
  "name": "y (cm)", 
  "type": "scatter", 
  "x": ["0", "3", "6", "9", "12", "15", "18", "21"], 
  "y": ["0", "-0.42", "-1.43", "-3.12", "-5.21", "-7.93", "-11.28", "-15.19"], 
  "error_x": {"array": ["0.1", "0.1", "0.1", "0.1", "0.1", "0.1", "0.1", "0.1"]}, 
  "error_y": {"array": ["0", "0.10", "0.11", "0.14", "0.19", "0.22", "0.34", "0.26"]}
}
data = Data([trace1])
layout = {
  "title": "Graph #1: X vs. Y", 
  "width": 1099, 
  "xaxis": {
    "type": "linear", 
    "range": [-1.2777777777777781, 22.27777777777778], 
    "title": "x (cm) ±0.1", 
    "autorange": True
  }, 
  "yaxis": {
    "type": "linear", 
    "range": [-16.319480519480518, 1.07012987012987], 
    "title": "y (cm)", 
    "autorange": True
  }, 
  "height": 505, 
  "autosize": True
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)

