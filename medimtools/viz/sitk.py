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
    coords=None,
):

    if int(image.GetPixelID()) != 1:
        logger.info("Rescaling image for vizualization ...")
        # [0,255] for visualization purposes
        image = sitk.Cast(sitk.RescaleIntensity(image, 0, 255), sitk.sitkUInt8)

    if isotropic:
        image = make_isotropic(image)

        if mask:
            mask = make_isotropic(mask, interpolator=sitk.sitkNearestNeighbor)

        if contour:
            contour = make_isotropic(contour, interpolator=sitk.sitkNearestNeighbor)

    if contour:
        mask = get_contour(contour)

    image = get_image_preview(image, coords=coords)

    if mask:
        mask = get_image_preview(mask, coords=coords)

    if display:
        plt.imshow(image, cmap=cmap)

        if mask is not None:
            plt.imshow(mask, cmap=cmap, alpha=0.5)

        plt.show()

    return image
