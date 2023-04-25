import sys
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation, FFMpegWriter
from update_graph import update

matplotlib.style.use('seaborn-v0_8-pastel')

def lorenz(t, X, sigma, beta, rho):
    """
    This function computes the derivatives of the three state variables 
    (x, y, and z) at a given point in time for a Lorenz system, given 
    the current values of the state variables and the system parameters.

    Parameters
    ----------
    t : float
        The current time. This serves as a placeholder for a `solve_ivp` parameter.
    X : list of float
        The current values of the state variables [x, y, z].
    sigma : float
        The system parameter sigma.
    beta : float
        The system parameter beta.
    rho : float
        The system parameter rho.

    Returns
    -------
    list of float
        The derivatives of the state variables [x_dot, y_dot, z_dot] at the current time.

    """
    x, y, z = X
    x_dot = sigma * (y - x)
    y_dot = x * (rho - z) - y
    z_dot = x * y - beta * z
    return [x_dot, y_dot, z_dot]

if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        params = json.load(f)
else:
    params = {
        'sigma': 10,
        'beta': 2.667,
        'rho': 28,
        'x0': 0,
        'y0': 1,
        'z0': 1.05,
        'dt': 0.002,
        'T': 25,
        'dark': False
    }

sigma = params['sigma']
beta = params['beta']
rho = params['rho']
x0 = params['x0']
y0 = params['y0']
z0 = params['z0']
dt = params['dt']
T = params['T']
dark = params['dark']

if dark:
    matplotlib.style.use('dark_background')

sol = solve_ivp(lorenz, [0, T], [x0, y0, z0], args=(sigma, beta, rho), dense_output=True, max_step=dt)

fig, axs = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Lorenz Attractor Phase Space')

# Have colors span from t_0 to t_final
colors = np.arange(0, len(sol.t))

anim = FuncAnimation(fig, update, fargs=(axs, sol, colors), frames=int(T/dt/10), interval=0.01, blit=False)
writer = FFMpegWriter(fps=60, bitrate=1800)
anim.save('output.mp4', writer=writer, dpi=100)