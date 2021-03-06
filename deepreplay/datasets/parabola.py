import numpy as np

def load_data(xlim=(-1, 1), n_points=1000, shuffle=True, seed=13):
    # feature x1, 1,000 points evenly spaced between -1 and 1
    x1 = np.linspace(xlim[0], xlim[1], n_points)
    # feature x2, for the two curves
    x2_blue = np.square(x1)
    x2_green = np.square(x1) - .5

    # coordinates for points in the blue line
    blue_line = np.vstack([x1, x2_blue])
    # coordinates for points in the green line
    green_line = np.vstack([x1, x2_green])

    # Remember, blue line is negative (0) and green line is positive (1)
    X = np.concatenate([blue_line, green_line], axis=1).transpose()
    y = np.concatenate([np.zeros(n_points), np.ones(n_points)])

    # But we must not feed the network with neatly organized inputs...
    # so let's randomize them
    if shuffle:
        np.random.seed(seed)
        shuffled = np.random.permutation(range(X.shape[0]))
        X = X[shuffled]
        y = y[shuffled].reshape(-1, 1)

    return (X, y)