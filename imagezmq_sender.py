import imagezmq
import simplejpeg
from simple_pyspin import Camera
import cv2
import numpy as np

#HUB='tcp://gork.local:5555'
port = 5555

if __name__ == '__main__':
    cam = Camera()
    cam.init()
    sender = imagezmq.ImageSender("tcp://*:{}".format(port), REQ_REP=False)
    cam.start()
    while True:
        img = cam.get_array()
        jpg_buffer = simplejpeg.encode_jpeg(img[..., np.newaxis], quality=55, colorspace='GRAY')
        sender.send_jpg("microscope", jpg_buffer)

# if __name__ == '__main__':
#     cap = cv2.VideoCapture(0)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)

#     sender = imagezmq.ImageSender(connect_to=HUB)
#     while True:
#         ret, img = cap.read()
#         if ret:
#           jpg_buffer = simplejpeg.encode_jpeg(img, quality=85, colorspace='GRAYSCALE')
#           sender.send_jpg("microscope", jpg_buffer)
