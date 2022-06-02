# Get various statistics from the label/mask file
import SimpleITK as sitk


def get_mask_stats(mask):
    filter = sitk.LabelShapeStatisticsImageFilter()
    filter.Execute(mask)

    return {
        "NumberOfObjects": filter.GetNumberOfLabels(),
        "BoundingBox": filter.GetBoundingBox(1),
        "Centroid": filter.GetCentroid(1),
        "Perimeter": filter.GetPerimeter(1),
        "EquivalentSphericalRadius": filter.GetEquivalentSphericalRadius(1),
    }
