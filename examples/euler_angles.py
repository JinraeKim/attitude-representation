import matplotlib.pyplot as plt
import numpy as np

from src.attitude import euler2rot
from src.visualize import plot_body_frame, plot_inertial_frame

if __name__ == "__main__":
    names = ["initial", "yaw (45 deg)", "pitch (45 deg)", "roll (45 deg)"]
    angles_list = [
        np.array([0, 0, 0.0]),
        np.array([0, 0, np.deg2rad(45)]),
        np.array([0, np.deg2rad(45), np.deg2rad(45)]),
        np.array([np.deg2rad(45), np.deg2rad(45), np.deg2rad(45)]),
    ]
    fig = plt.figure(figsize=(12, 3))
    for i, (name, angles) in enumerate(zip(names, angles_list)):
        ax = fig.add_subplot(1, 4, i + 1, projection="3d")
        ax.set_title(name, fontsize=20)
        plot_inertial_frame(ax=ax)

        R = euler2rot(*angles)
        plot_body_frame(ax=ax, R=R)
    plt.savefig("./figures/euler_angles.png")
