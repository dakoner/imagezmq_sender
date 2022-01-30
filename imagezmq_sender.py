import imagezmq
import simplejpeg
#from simple_pyspin import Camera

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
    import cv2
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3264)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2448)

    sender = imagezmq.ImageSender(connect_to=HUB)
    while True:
        ret, img = cap.read()
        if ret:
          jpg_buffer = simplejpeg.encode_jpeg(img, quality=85, colorspace='RGB')
          sender.send_jpg("microscope", jpg_buffer)
