import cv2
import numpy as np
import PIL
from PIL import Image

filePath = 'Images/photomosaicImage'
tile = 1
vid_capture = cv2.VideoCapture("192.168.1.111")

while (vid_capture.isOpened()):
    ret, frame = vid_capture.read()
cv2.imshow('image', frame)

    k = cv2.waitKey(1)
    if tile <= 8:
        if k == ord('p'):
            cv2.imwrite('Images/photomosaicImage{}.png'.format(tile), frame)
            tile = tile + 1

    if tile > 8:
        # Top layer
        top_list_im = ['{}1.png'.format(filePath), '{}2.png'.format(filePath), '{}3.png'.format(filePath), '{}4.png'.format(filePath)]
        top_imgs = [PIL.Image.open(i) for i in top_list_im]
        min_shape = sorted([(np.sum(i.size), i.size) for i in top_imgs])[0][1]
        top_img_layer = np.hstack((np.asarray(i.resize(min_shape)) for i in top_imgs))
        top_imgs_layer = PIL.Image.fromarray(top_img_layer)
        top_imgs_layer.save('Images/photomosaicTopLayer.png')

        # Bottom layer
        bottom_list_im = ['{}8.png'.format(filePath), '{}7.png'.format(filePath), '6.png'.format(filePath), '{}5.png'.format(filePath)]
        bottom_imgs = [PIL.Image.open(i) for i in bottom_list_im]
        min_shape = sorted( [(np.sum(i.size), i.size ) for i in bottom_imgs])[0][1]
        bottom_img_layer = np.hstack((np.asarray(i.resize(min_shape)) for i in bottom_imgs))
        bottom_imgs_layer = PIL.Image.fromarray(bottom_img_layer)
        bottom_imgs_layer.save('Images/photomosaicBottomLayer.png')

        # Combined top and bottom layer
        combine_list_im = ['Images/photomosaicTopLayer.png', 'Images/photomosaicBottomLayer.png']
        combine_imgs = [PIL.Image.open(i) for i in combine_list_im]
        min_shape = sorted([(np.sum(i.size), i.size) for i in combine_imgs])[0][1]
        combine_img_layers = np.vstack((np.asarray(i.resize(min_shape)) for i in combine_imgs))
        combined_image = PIL.Image.fromarray(combine_img_layers)
        combined_image.save('Images/Photomosaic.png')

        # Display photomosaic
        photomosaic = cv2.imread("Images/Photomosaic.png", cv2.IMREAD_COLOR)
        displayImage = True
        while displayImage:
            cv2.imshow('image', photomosaic)
            q = cv2.waitKey(1)
            if q == ord('q'):
                cv2.destroyAllWindows()
                break
