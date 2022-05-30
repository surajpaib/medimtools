import SimpleITK as sitk


def get_stats(image):
    filter = sitk.StatisticsImageFilter()

    filter.Execute(image)

    return {
        "min": filter.GetMinimum(),
        "max": filter.GetMaximum(),
        "mean": filter.GetMean(),
        "std": filter.GetSigma(),
        "size": image.GetSize(),
        "spacing": image.GetSpacing(),
        "origin": image.GetOrigin(),
        "direction": image.GetDirection(),
    }
