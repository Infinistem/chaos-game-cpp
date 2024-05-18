import numpy as np,matplotlib.pyplot as plt

class Graph:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
def mandelbrot(c, i): # generate the set
    z = 0
    for x in range(i):
        if abs(z) > 2:
            return x
        z = pow(z, 2) + c
    return i
def plot(xmin, xmax, ymin, ymax, w, h, i):
    x = np.linspace(xmin, xmax, w)
    y = np.linspace(ymin, ymax, w)
    dat = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            c = complex(x[j], y[i])
            dat[i, j] = mandelbrot(c, i)
    return dat


def init(): # plot the set
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    height, width, itt= 1000, 1000, 20000 # high precision
    img = plot(xmin, xmax, ymin, ymax, width, height, itt) # have params for customization
    plt.imshow(img, extent=[xmin, xmax, ymin, ymax], cmap="hsv")
    plt.colorbar()
    plt.title('Mandebrot Viewer')
    plt.show()
def zoom():
    pass
init()