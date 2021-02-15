df = pd.read_csv('data/gapminder_gdp_americas.csv', index_col='country')
df = df.drop(columns=['continent'])
years = df.columns.str.strip('gdpPercap_')
df.columns = years.astype(int)

trace0 = go.Bar(
    x = df.columns,
    y = df.loc['Canada'],
    name = 'Canada',
    marker_color = 'rgb(200, 0, 0)'
)
trace1 = go.Bar(
    x = df.columns,
    y = df.loc['United States'],
    name = 'United States',
    marker_color = 'rgb(0, 0, 200)'
)
trace2 = go.Bar(
    x = df.columns,
    y = df.loc['Mexico'],
    name = 'Mexico',
    marker_color = 'rgb(0, 200, 0)'
)

data = [trace0, trace1, trace2]
layout = go.Layout(
    title = 'Per-capita GDP Growth in North America',
    xaxis_title = 'Year',
    yaxis_title = 'GDP per-capita'
)

fig = go.Figure(data=data, layout=layout)
fig.show()
