import cv2 as cv
import numpy as np


# image = cv.imread("lena.jpg", cv.IMREAD_UNCHANGED)
# cv.imshow("Original", image)
def GaussianKernel(kernel_size, sigma, mux, muy):
    Gaussian_Kernel = np.zeros((kernel_size, kernel_size), dtype='float32')
    p = kernel_size//2
    q = kernel_size//2
    for x in range(-p, p+1):
        for y in range(-q, q+1):
            gaussian = (1/(2*np.pi*sigma**2)) * \
                np.exp(-(((x-mux)**2)+(y-muy)**2)/(2*sigma**2))
            Gaussian_Kernel[x+p, y+q] = gaussian
    Gaussian_Kernel = Gaussian_Kernel/np.sum(Gaussian_Kernel)
    return Gaussian_Kernel

# print(Gaussian_Kernel)

# Blurred_image = cv.filter2D(image, -1, Gaussian_Kernel)


# cv.imshow("Blurred Image", Blurred_image)
# cv.waitKey(0)
kernel = GaussianKernel(3, 1.4, 0, 0)
print(kernel)

# def Convolve(image,kernel):
#     image =
