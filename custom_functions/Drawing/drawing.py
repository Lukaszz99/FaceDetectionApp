import cv2 as cv


def rectangle_with_access(frame, name, top=0, right=0, bottom=0, left=0):
    """
    Draw green rectangle over person face if has access. Display name over rectangle.

    Args:
        frame (numpy.ndarray): frame to draw rectangle
        name (str): name of person to draw rectangle
        top (int): top-left rectangle position
        right (int): top-right rectangle position
        bottom (int): bottom-right rectangle position
        left (int): bottom-left rectangle position
    """
    cv.rectangle(frame, (left, top), (right, bottom),
                 (0, 255, 0), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv.putText(frame, name, (left, y), cv.FONT_HERSHEY_SIMPLEX,
               0.75, (0, 255, 0), 2)

def rectangle_withOUT_access(frame, name, top=0, right=0, bottom=0, left=0):
    """
    Draw green rectangle over person face if access is not granted. Display name over rectangle.

    Args:
        frame (numpy.ndarray): frame to draw rectangle
        name (str): name of person to draw rectangle
        top (int): top-left rectangle position
        right (int): top-right rectangle position
        bottom (int): bottom-right rectangle position
        left (int): bottom-left rectangle position
    """
    cv.rectangle(frame, (left, top), (right, bottom),
                 (0, 0, 255), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv.putText(frame, name, (left, y), cv.FONT_HERSHEY_SIMPLEX,
               0.75, (0, 0, 255), 2)
    bottom = bottom + 18
    cv.putText(frame, 'No access', (left, bottom), cv.FONT_HERSHEY_SIMPLEX,
               0.75, (0, 0, 255), 2)

def rectagne_unknow(frame, top=0, right=0, bottom=0, left=0):
    """
    Draw green rectangle over unknown person. Display 'unknown' over rectangle.

    Args:
        frame (numpy.ndarray): frame to draw rectangle
        top (int): top-left rectangle position
        right (int): top-right rectangle position
        bottom (int): bottom-right rectangle position
        left (int): bottom-left rectangle position
    """

    cv.rectangle(frame, (left, top), (right, bottom),
                 (0, 80, 255), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv.putText(frame, 'Unknown', (left, y), cv.FONT_HERSHEY_SIMPLEX,
               0.75, (0, 80, 255), 2)
