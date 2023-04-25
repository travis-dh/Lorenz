import numpy as np

def update(i, axs, sol, colors):
    """
    Update function for the Lorenz system animation.

    Parameters
    ----------
    i : int
        Frame number.

    Returns
    -------
    axs : list of AxesSubplot objects
        List of the three AxesSubplot objects in the figure.

    """
    axs[0].clear()
    axs[1].clear()
    axs[2].clear()

    # Compute the optimal xlim and ylim for each subplot based on the 
    # final values of sol.y and expand them by 5 units for extra space.
    xy_xlim = (np.min(sol.y[0]) - 5, np.max(sol.y[0]) + 5)
    xy_ylim = (np.min(sol.y[1]) - 5, np.max(sol.y[1]) + 5)
    xz_xlim = (np.min(sol.y[0]) - 5, np.max(sol.y[0]) + 5)
    xz_ylim = (np.min(sol.y[2]) - 5, np.max(sol.y[2]) + 5)
    yz_xlim = (np.min(sol.y[1]) - 5, np.max(sol.y[1]) + 5)
    yz_ylim = (np.min(sol.y[2]) - 5, np.max(sol.y[2]) + 5)

    # Plot the scatter points and format the subplots
    axs[0].scatter(sol.y[0][:i*10], sol.y[1][:i*10], c=colors[:i*10], cmap='autumn', s=1)
    axs[0].set_xlim(xy_xlim)
    axs[0].set_ylim(xy_ylim)
    axs[0].set_axis_off()
    axs[0].set_title(r'$xy$')

    axs[1].scatter(sol.y[0][:i*10], sol.y[2][:i*10], c=colors[:i*10], cmap='winter', s=1)
    axs[1].set_xlim(xz_xlim)
    axs[1].set_ylim(xz_ylim)
    axs[1].set_axis_off()
    axs[1].set_title(r'$xz$')

    axs[2].scatter(sol.y[1][:i*10], sol.y[2][:i*10], c=colors[:i*10], cmap='cool', s=1)
    axs[2].set_xlim(yz_xlim)
    axs[2].set_ylim(yz_ylim)
    axs[2].set_axis_off()
    axs[2].set_title(r'$yz$')

    return axs