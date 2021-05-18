def GrayScale(image):
    print("""
    1. BT-709 (HDTV) Method Take 0.21Red + 0.72Green + 0.07Blue. (Also known as ITU-R BT-709 formula.)
    2. BT-601 (PAL/NTSC) Method Take 0.30Red + 0.59Green + 0.11Blue. (Also known as ITU-R BT-601 formula.)
    3. Average Red, Green, Blue Take 1/3 of each color component. ( 1/3Red + 1/3Green + 1/3Blue)
    """)
    method = int(input("Method number: "))
    import cv2 as cv

    image = cv.imread('lena.jpg', cv.IMREAD_UNCHANGED)
    R = image[:, :, 0]/255
    G = image[:, :, 1]/255
    B = image[:, :, 2]/255

    if method == 1:
        BT_709_image = 0.21*R + 0.72*G + 0.07*B
        cv.imshow("BT-709_image", BT_709_image)
        cv.waitKey(0)
        return BT_709_image
    elif method == 2:
        BT_601_image = 0.30*R + 0.59*G + 0.11*B
        cv.imshow("BT-601_image", BT_601_image)
        cv.waitKey(0)
        return BT_601_image
    else:
        RGB_avg = (R+G+B)/3
        cv.imshow("RGB_avg", RGB_avg)
        cv.waitKey(0)
        return RGB_avg
