# Mean -2, standard deviation 1
random_y2 = np.random.randn(N) - 2

fig = go.Figure()
fig.add_scatter(
    x = linear_x,
    y = random_y0,
    mode = 'lines'
)
fig.add_scatter(
    x = linear_x,
    y = random_y1,
    mode = 'lines+markers'
)
fig.add_scatter(
    x = linear_x,
    y = random_y2,
    mode = 'markers'
)
fig.show()
