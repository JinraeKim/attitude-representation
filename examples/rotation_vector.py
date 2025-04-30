import matplotlib.pyplot as plt
import numpy as np

from src.attitude import rot2rotvec, rotvec2rot
from src.visualize import plot_body_frame, plot_inertial_frame


def right_fold_accumulate_rot(seq):
    result = [rotvec2rot(*seq[0])]
    for x in seq[1:]:
        result.append(rotvec2rot(*x) @ result[-1])
    return result


if __name__ == "__main__":
    names = ["0: initial", "1: yaw (45 deg)", "2: pitch (45 deg)", "3: roll (45 deg)"]
    theta = np.deg2rad(45)
    rotvec_list = [
        (0, np.array([1, 0, 0])),
        (theta, np.array([0, 0, 1])),  # rotate aout Z=D
        (
            theta,
            np.array([-1, 1.0, 0]),
        ),  # rotate about Y', represented in inertial frame
        (
            theta,
            np.array([1, 1, -1.0]),
        ),  # rotate about X'', represented in inertial frame
    ]
    R_list = right_fold_accumulate_rot(rotvec_list)
    fig = plt.figure(figsize=(12, 3))
    for i, (name) in enumerate(names):
        ax = fig.add_subplot(1, 4, i + 1, projection="3d")
        ax.set_title(name, fontsize=20)
        plot_inertial_frame(ax=ax)

        R = R_list[i]
        plot_body_frame(ax=ax, R=R)

        _rotvec = rot2rotvec(R)
        _R = rotvec2rot(*_rotvec)
        print(f"Obtained rotation matrix using angle and axis: {R}")
        print(f"reverted rotation matrix using rot2rotvec and rotvec2rot: {_R}")

    plt.savefig("./figures/rotvec.png")
