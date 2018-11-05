import cv2
import os

ROOT = os.getcwd()


def crop(fn, r=2, c=2):
    im = cv2.imread(fn)
    im = cv2.resize(im, (1000, 500))

    img_height = im.shape[0]
    img_width = im.shape[1]

    y1 = 0
    M = img_height // r
    N = img_width // c

    for r, y in enumerate(range(0, img_height, M)):
        for c, x in enumerate(range(0, img_width, N)):
            y1 = y + M
            x1 = x + N
            tiles = im[y:y + M, x:x + N]

            cv2.rectangle(im, (x, y), (x1, y1), (0, 255, 0))
            cv2.imwrite(os.path.join(ROOT, 'images/output/{0}{1}.jpeg'.format(r, c)), tiles)
