import cv2 as cv


def rectangle_with_access(frame, name='Na', top=0, right=0, bottom=0, left=0):
    cv.rectangle(frame, (left, top), (right, bottom),
                 (0, 255, 0), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv.putText(frame, name, (left, y), cv.FONT_HERSHEY_SIMPLEX,
               0.75, (0, 255, 0), 2)

def rectangle_withOUT_access(frame, name='Na', top=0, right=0, bottom=0, left=0):
    cv.rectangle(frame, (left, top), (right, bottom),
                 (0, 0, 255), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv.putText(frame, name, (left, y), cv.FONT_HERSHEY_SIMPLEX,
               0.75, (0, 0, 255), 2)
    bottom = bottom + 18
    cv.putText(frame, 'No access', (left, bottom), cv.FONT_HERSHEY_SIMPLEX,
               0.75, (0, 0, 255), 2)

def rectagne_unknow(frame, top=0, right=0, bottom=0, left=0):
    cv.rectangle(frame, (left, top), (right, bottom),
                 (0, 80, 255), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv.putText(frame, 'Unknown', (left, y), cv.FONT_HERSHEY_SIMPLEX,
               0.75, (0, 80, 255), 2)
