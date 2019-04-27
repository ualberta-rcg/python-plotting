# Mean -2, standard deviation 1
random_y2 = np.random.randn(N) - 2

trace0 = go.Scatter(
    x = linear_x,
    y = random_y0,
    mode = 'lines'
)
trace1 = go.Scatter(
    x = linear_x,
    y = random_y1,
    mode = 'lines+markers'
)
trace2 = go.Scatter(
    x = linear_x,
    y = random_y2,
    mode = 'markers'
)

data = [trace0, trace1, trace2]
py.iplot(data)

