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
