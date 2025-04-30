import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin

from src.attitude import quat2rot, quat_mul
from src.visualize import plot_body_frame, plot_inertial_frame


def right_fold_accumulate(seq, op):
    result = [seq[0]]
    for x in seq[1:]:
        result.append(op(x, result[-1]))
    return result


if __name__ == "__main__":
    names = ["0: initial", "1: yaw (45 deg)", "2: pitch (45 deg)", "3: roll (45 deg)"]
    theta = np.deg2rad(45)
    q_list = [
        np.array([1.0, 0, 0, 0]),
        np.array(
            [cos(0.5 * theta), *(sin(0.5 * theta) * np.array([0, 0, 1]))]
        ),  # rotate about Z=D
        np.array(
            [
                cos(0.5 * theta),
                *(
                    sin(0.5 * theta)
                    * np.array([-0.5 * np.sqrt(2), 0.5 * np.sqrt(2), 0])
                ),
            ]
        ),  # rotate about Y', represented in inertial frame
        np.array(
            [
                cos(0.5 * theta),
                *(sin(0.5 * theta) * (1 / np.sqrt(3)) * np.array([1, 1, -1.0])),
            ]
        ),  # rotate about X'', represented in inertial frame
    ]
    q_acc_list = right_fold_accumulate(q_list, quat_mul)
    fig = plt.figure(figsize=(12, 3))
    for i, name in enumerate(names):
        ax = fig.add_subplot(1, 4, i + 1, projection="3d")
        ax.set_title(name, fontsize=20)
        plot_inertial_frame(ax=ax)

        q = q_acc_list[i]
        R = quat2rot(q)
        plot_body_frame(ax=ax, R=R)
    plt.savefig("./figures/quaternion.png")
