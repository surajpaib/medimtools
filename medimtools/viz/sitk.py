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

    if int(image.GetPixelID()) != 1:
        logger.info("Rescaling image ...")
        # [0,255] for visualization purposes
        image = sitk.Cast(sitk.RescaleIntensity(image, 0, 255), sitk.sitkUInt8)

    if isotropic:
        image = make_isotropic(image)

        if mask:
            mask = make_isotropic(mask, interpolator=sitk.sitkNearestNeighbor)

        if contour:
            contour = make_isotropic(contour, interpolator=sitk.sitkNearestNeighbor)

    if mask:
        image = overlay_mask(image, mask)

    if contour:
        image = overlay_mask(image, contour, contour=True)

    image = get_image_preview(image)

    if display:
        plt.imshow(image, cmap=cmap)
        plt.show()

    return image
