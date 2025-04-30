import matplotlib.pyplot as plt
import numpy as np

from src.attitude import euler2rot
from src.visualize import plot_body_frame, plot_inertial_frame

if __name__ == "__main__":
    names = ["roll", "pitch", "yaw", "mixed"]
    angles_list = [
        np.array([np.deg2rad(15), 0, 0]),
        np.array([0, np.deg2rad(15), 0]),
        np.array([0, 0, np.deg2rad(15)]),
        np.array([np.deg2rad(45), np.deg2rad(45), np.deg2rad(45)]),
    ]
    for name, angles in zip(names, angles_list):
        fig, ax = plot_inertial_frame()

        R = euler2rot(*angles)
        plot_body_frame(ax=ax, R=R)
        plt.savefig("./figures/euler_angles/" + name + ".png")
