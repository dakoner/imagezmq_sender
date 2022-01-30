import numpy as np
import socket
import time
import imagezmq
import simplejpeg
#from simple_pyspin import Camera
from imutils.video import videostream

HUB='tcp://desktop-h3tsld0.local:5555'

# if __name__ == '__main__':
#     cam = Camera()
#     cam.init()
#     sender = imagezmq.ImageSender(connect_to=HUB)
#     cam.start()
#     while True:
#         img = cam.get_array()
#         jpg_buffer = simplejpeg.encode_jpeg(img[..., np.newaxis], quality=55, colorspace='GRAY')
#         sender.send_jpg("microscope", jpg_buffer)
#         print("sent")

if __name__ == '__main__':
    cam = videostream.VideoStream(usePiCamera=False).start()
    sender = imagezmq.ImageSender(connect_to=HUB)
    while True:
        img = cam.read()
        jpg_buffer = simplejpeg.encode_jpeg(img, quality=55, colorspace='RGB')
        sender.send_jpg("microscope", jpg_buffer)
        print("sent")
