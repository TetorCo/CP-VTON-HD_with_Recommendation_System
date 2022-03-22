import cv2
import os
import numpy as np
from skimage.segmentation import clear_border
import scipy.ndimage.morphology as sm

def seg(image_name):
    IMG_DIR = 'D:/CP2/CP-VTON-HD_with_Recommendation_System/flask/static/upload_image'
    IMG_PATH = os.path.join(IMG_DIR, image_name).replace("\\", '/')
    img = cv2.imread(IMG_PATH, 0)
    img = cv2.resize(img, dsize=(768, 1024))

    _, img_th = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    img_change = 255-img_th
    img_change = clear_border(img_change)
    img_change = np.array(img_change)
    cv2.imwrite(f'./VITON_HD/datasets/test/cloth/{image_name}', img)
    cv2.imwrite(f'./VITON_HD/datasets/test/cloth-mask/{image_name}', img_change)