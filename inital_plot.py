#Run this Script once to create the plot

import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in("username", "APIkey") #Your Username and API Key
STREAM_TOKEN = 'token' 			 #Your Streaming API token

trace1 = Scatter(				 
    x=[],
    y=[], 
    name = 'Core Temp',
    stream = dict(token=STREAM_TOKEN)
)

data = Data([trace1])

layout = Layout(
    title='Raspberry Pi Core Temperature',
    xaxis=XAxis(
        title='Date & Time',
        titlefont=Font(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=YAxis(
        title='Temperature',
        titlefont=Font(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

fig = Figure(data=data, layout=layout)
py.plot(fig, filename='Raspberry Pi Core Temperature')