import SimpleITK as sitk
import matplotlib.pyplot as plt
from medimtools.viz.ops import *


def quick_view(
    image: sitk.Image,
    display: bool = True,
    isotropic: bool = True,
    cmap: str = "gray",
    mask=None,
    contour=None,
):
    if isotropic:
        image = make_isotropic(image)

    if mask:
        image = overlay_mask(image, mask)

    if contour:
        image = overlay_mask(image, contour, contour=True)

    image = get_image_preview(image)

    if display:
        plt.imshow(image)
        plt.show()

    return image
