import numpy as np


def eye_aspect_ratio(eye):
    # 1. Vertical distances (Eyelids)
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])

    # 2. Horizontal distance (Eye width)
    C = np.linalg.norm(eye[0] - eye[3])

    # 3. Calculate Ratio
    ear = (A + B) / (2.0 * C)
    return ear
