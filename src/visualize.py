import matplotlib.pyplot as plt
import numpy as np


def _set_axes_equal(ax):
    """Make axes of 3D plot have equal scale so that spheres appear as spheres."""
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = sum(x_limits) / 2
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = sum(y_limits) / 2
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = sum(z_limits) / 2

    max_range = max([x_range, y_range, z_range]) / 2

    ax.set_xlim3d([x_middle - max_range, x_middle + max_range])
    ax.set_ylim3d([y_middle - max_range, y_middle + max_range])
    ax.set_zlim3d([z_middle - max_range, z_middle + max_range])


def dashed_arrow(ax, x0, y0, z0, dx, dy, dz, color="r", alpha=0.7):
    # Create a dashed line for the shaft of the arrow
    num_segments = 10  # Number of segments in the dashed line
    x_values = np.linspace(x0, x0 + dx, num_segments)
    y_values = np.linspace(y0, y0 + dy, num_segments)
    z_values = np.linspace(z0, z0 + dz, num_segments)

    # Create the dashed line
    ax.plot(
        x_values,
        y_values,
        z_values,
        linestyle="--",
        color=color,
        alpha=alpha,
        linewidth=2,
    )

    # Plot the arrowhead as a small solid triangle at the end
    ax.quiver(
        x0 + dx,
        y0 + dy,
        z0 + dz,
        0,
        0,
        0,
        color=color,
        alpha=alpha,
        arrow_length_ratio=0.1,
        pivot="tail",
    )


def plot_inertial_frame(*args, alpha=0.3, linestyle="--", **kwargs):
    return plot_frame(R=np.eye(3), *args, linestyle=linestyle, alpha=alpha, **kwargs)


def plot_body_frame(*args, R=np.eye(3), axes_name="XYZ", **kwargs):
    return plot_frame(R=R, *args, **kwargs, axes_name=axes_name)


def plot_frame(
    ax=None,
    R=np.eye(3),  # R: rotation matrix from given frame to the inertial frame
    origin=np.zeros(3),
    length=1.0,
    alpha=1.0,
    axes_name="NED",
    linestyle="-",
):
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
    else:
        fig = ax.figure

    x0, y0, z0 = origin
    axes = {
        axes_name[0]: np.array([1.0, 0, 0]),
        axes_name[1]: np.array([0, 1.0, 0]),
        axes_name[2]: np.array([0, 0, 1.0]),
    }  # defined in the given frame
    colors = {
        axes_name[0]: "r",
        axes_name[1]: "g",
        axes_name[2]: "b",
    }
    R_NED_to_FLU = np.array(
        [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
    )  # You have to represent a vector in FLU (forward-left-up) frame eventually to draw

    for label, dxyz in axes.items():
        dx, dy, dz = R_NED_to_FLU @ R @ (length * dxyz)
        if linestyle == "--":
            dashed_arrow(ax, x0, y0, z0, dx, dy, dz, color=colors[label], alpha=alpha)
        else:
            ax.quiver(
                x0,
                y0,
                z0,
                dx,
                dy,
                dz,
                color=colors[label],
                arrow_length_ratio=0.1,
                linewidth=2,
                alpha=alpha,
            )
        ax.text(
            x0 + 1.2 * dx,
            y0 + 1.2 * dy,
            z0 + 1.2 * dz,
            label,
            color=colors[label],
            fontsize=12,
        )

    # axes
    ax.set_xlim([x0 - length, x0 + length])
    ax.set_ylim([y0 - length, y0 + length])
    ax.set_zlim([z0 - length, z0 + length])

    # ax.set_xlabel("")
    # ax.set_ylabel("")
    # ax.set_zlabel("")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
    # ax.set_title("")
    _set_axes_equal(ax)
    return fig, ax
