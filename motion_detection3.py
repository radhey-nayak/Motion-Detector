# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:23:21 2020

@author: Radhashyam nayak
"""

import cv2

# Video Capture
#video = cv2.VideoCapture(0)
video = cv2.VideoCapture("demo2.mp4")

ret, frame1 = video.read()
ret, frame2 = video.read()

# Resizing Frames
'''frame1 = cv2.resize(frame1, (700, 1500))
frame2 = cv2.resize(frame2, (700, 1500))

# Rotating Image
frame1 = cv2.rotate(frame1, rotateCode=2)
frame2 = cv2.rotate(frame2, rotateCode=2)'''
# Loop
while video.isOpened():

    # Checking Difference
    diff = cv2.absdiff(frame1, frame2)

    # Converting To Gray Scale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Converting Gray Image To Blur Image For Perfect Result
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresshold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Itaration
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop
    for contour in contours:

        # for creating boxes On The Moving Object: 1
        # (x, y, w, h) = cv2.boundingRect(contour)

        # Checking Contour area
        if cv2.contourArea(contour) < 200:
            continue

        # for creating boxes On The Moving Object: 1
        # cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Drawing Contour
        cv2.drawContours(frame1, contour, -1, (0, 255, 0), 3)

        # Printing Text On Frames
        cv2.putText(frame1, "STATUS: {}".format("movement"), (10, 30), cv2.FONT_HERSHEY_COMPLEX,
                    1, (0, 0, 255), 2)

    # Without Checking Contour Area
    # cv2.drawContours(frame1, contours, -1, (0, 0, 255), 1)

    # Showing Frames
    cv2.imshow("demo", frame1)
    # cv2.imshow("blur", blur)

    # Capturing Frame again for Repete Checking
    frame1 = frame2
    ret, frame2 = video.read()
    '''frame2 = cv2.resize(frame2, (700, 1500))
    frame2 = cv2.rotate(frame2, rotateCode=2)'''

    # Frame Execution Time
    key = cv2.waitKey(1)

    # Exit Key
    if key == ord('q'):
        break

# Relese
video.release()
# Destroy Windows
cv2.destroyAllWindows()
