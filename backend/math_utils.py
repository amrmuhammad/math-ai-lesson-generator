import matplotlib.pyplot as plt
import numpy as np

def plot_quadratic(a=1, b=0, c=0):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"${a}x^2 + {b}x + {c}$")
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Quadratic Function")
    ax.legend()
    return fig