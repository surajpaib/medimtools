import SimpleITK as sitk
import matplotlib.pyplot as plt
from medimtools.viz.ops import get_image_preview, make_isotropic
from medimtools.viz.ops import *


def quick_view(image: sitk.Image, display: bool = True, isotropic: bool = True, cmap: str = 'gray'):
    if isotropic:
        image = make_isotropic(image)

    image = get_image_preview(image)

    if display:
        f = plt.figure(figsize=(20, 10))
        plt.imshow(image, cmap=cmap)
        plt.show()

    return image

    






