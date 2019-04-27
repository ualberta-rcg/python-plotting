trace0 = go.Scatter(
    x = df.columns,
    y = df.loc['Netherlands'],
    mode = 'lines',
    name = 'Netherlands',
    line = dict(
        color = 'rgb(255, 127, 0)'
    )
)
trace1 = go.Scatter(
    x = df.columns,
    y = df.loc['France'],
    mode = 'lines+markers',
    name = 'France',
    line = dict(
        color = 'rgb(0, 0, 255)'
    )
)

data = [trace0, trace1]
layout = dict(
    title = 'GDP per-capita for the Netherlands and France',
    xaxis = dict(
        title = 'Year'
    ),
    yaxis = dict(
        title = 'GDP per-capita'
    )
)
fig = dict(data=data, layout=layout)
py.iplot(fig)
