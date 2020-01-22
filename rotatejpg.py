import numpy as np 
import argparse
import imutils 
import cv2
import glob
import os


def rotatejpg(jpgfile, outdir):

    src = cv2.imread(jpgfile)

    (h,w) = src.shape[:2] 
    center = (w//2, h//2)

    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    dst = cv2.warpAffine(src, M, (w, h))

    cv2.imwrite(os.path.join(outdir,'r_' + os.path.basename(jpgfile)),dst)


#rotatejpg('./datasets/haema/trainA/000000 Neutrophilic (mature).jpg', './datasets/haema/rotated_testA')

for jpgfile in glob.glob(r'./Neutrophilic (immature_Myelozyt)/*.jpg'):
    rotatejpg(jpgfile,r'./trainA_rotated')
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", required = True, help = "Path to the image")
    # ap.add_argument("-n", "--name", required = True, help = "Name of the image")
    # args = vars(ap.parse_args())

# #    print(args)

#     image = cv2.imread(args["image"])
#     # cv2.imshow("Original", image)
#     # cv2.waitKey(0)


#     (h,w) = image.shape[:2]
#     center = (w//2, h//2)

#     M = cv2.getRotationMatrix2D(center, 90, 1.0)
#     rotated = cv2.warpAffine(image, M, (w, h))
#     # cv2.imshow("Rotated by 90 degrees", rotated)
#     # cv2.waitKey(0)
