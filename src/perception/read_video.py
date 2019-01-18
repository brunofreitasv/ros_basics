#!/usr/bin/env python

from __future__ import division
import numpy as np
import cv2
     
def main():
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, Frame =video_capture.read()
        cv2.imshow('Frame', Frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()