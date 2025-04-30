import numpy as np
from numpy import cos, sin


def euler2rot(phi, theta, psi):
    """
    Input:
        phi: roll
        theta: pitch
        psi: yaw

    Output:
        R: rotation matrix (attitude)
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
    """
    Input:
        R: rotation matrix (attitude)

    Output:
        phi: roll
        theta: pitch
        psi: yaw
    """
    return np.array(
        [
            np.arctan2(R[2, 1], R[2, 2]),
            -np.arcsin(R[2, 0]),
            np.arctan2(R[1, 0], R[0, 0]),
        ]
    )


def quat2rot(q):
    """
    Input:
        q: unit quaternion (attitude)

    Output:
        R: rotation matrix (attitude)
    """
    return np.array(
        [
            [
                1 - 2 * (q[2] ** 2 + q[3] ** 2),
                2 * (q[1] * q[2] - q[0] * q[3]),
                2 * (q[1] * q[3] + q[0] * q[2]),
            ],
            [
                2 * (q[1] * q[2] + q[0] * q[3]),
                1 - 2 * (q[1] ** 2 + q[3] ** 2),
                2 * (q[2] * q[3] - q[0] * q[1]),
            ],
            [
                2 * (q[1] * q[3] - q[0] * q[2]),
                2 * (q[2] * q[3] + q[0] * q[1]),
                1 - 2 * (q[1] ** 2 + q[2] ** 2),
            ],
        ]
    )


def quat_mul(p, q):
    p_w, *p_v = p
    q_w, *q_v = q
    p_v = np.array(p_v)
    q_v = np.array(q_v)
    return np.array(
        [p_w * q_w - np.dot(p_v, q_v), *(p_w * q_v + q_w * p_v + np.cross(p_v, q_v))]
    )


def rotvec2rot(angle, vec):
    vec = vec / np.linalg.norm(vec)
    u1, u2, u3 = vec
    c, s = cos(angle), sin(angle)
    return np.array(
        [
            [
                u1**2 * (1 - c) + c,
                u1 * u2 * (1 - c) - u3 * s,
                u1 * u3 * (1 - c) + u2 * s,
            ],
            [
                u1 * u2 * (1 - c) + u3 * s,
                u2**2 * (1 - c) + c,
                u2 * u3 * (1 - c) - u1 * s,
            ],
            [
                u1 * u3 * (1 - c) - u2 * s,
                u2 * u3 * (1 - c) + u1 * s,
                u3**2 * (1 - c) + c,
            ],
        ]
    )


def rot2rotvec(R):
    angle = np.arccos((np.trace(R) - 1) / 2)
    if np.linalg.norm(angle) < 1e-9:
        vec = np.array([1, 0, 0])
    else:
        vec = np.array(
            [
                R[2, 1] - R[1, 2],
                R[0, 2] - R[2, 0],
                R[1, 0] - R[0, 1],
            ]
        ) / (2 * sin(angle))
    return angle, vec
