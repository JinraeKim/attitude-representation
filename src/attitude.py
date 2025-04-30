import numpy as np
from numpy import cos, sin


def euler2rot(phi, theta, psi):
    """
    phi: roll
    theta: pitch
    psi: yaw
    """
    return np.array(
        [
            [
                cos(theta) * cos(psi),
                -cos(phi) * sin(psi) + sin(phi) * sin(theta) * cos(psi),
                sin(phi) * sin(psi) + cos(phi) * sin(theta) * cos(psi),
            ],
            [
                cos(theta) * sin(psi),
                cos(phi) * cos(psi) + sin(phi) * sin(theta) * sin(psi),
                -sin(phi) * cos(psi) + cos(phi) * sin(theta) * sin(psi),
            ],
            [
                -sin(theta),
                sin(phi) * cos(theta),
                cos(phi) * cos(theta),
            ],
        ]
    )


def rot2euler(R):
    return np.array(
        [
            np.arctan2(R[2, 1], R[2, 2]),
            -np.arcsin(R[2, 0]),
            np.arctan2(R[1, 0], R[0, 0]),
        ]
    )
