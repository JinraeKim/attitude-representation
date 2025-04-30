import matplotlib.pyplot as plt
import numpy as np

from src.attitude import euler2rot, rot2euler
from src.visualize import plot_body_frame, plot_inertial_frame

if __name__ == "__main__":
    names = ["0: initial", "1: yaw (45 deg)", "2: pitch (45 deg)", "3: roll (45 deg)"]
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
        _angles = rot2euler(R)
        print(f"True Euler angles: {angles}")
        print(f"Euler angles from rotation matrix: {_angles}")
        plot_body_frame(ax=ax, R=R)
    plt.savefig("./figures/euler_angles.png")
