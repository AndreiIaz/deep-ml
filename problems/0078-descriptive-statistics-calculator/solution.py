import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    result = dict()
    result['mean'] = np.mean(data)
    result['median'] = np.median(data)
    fr = dict()
    for item in data:
        fr[item] = fr.get(item, 0) + 1
    # [(x1, fr1), (x2, fr2), ..., (xn, frn)]
    
    sorted_fr = sorted(fr.items(), key=lambda x: x[1])
    max_fr = sorted_fr[-1][1]
    modes = [x[0] for x in sorted_fr if x[1] == max_fr]
    mode = min(modes)
    result['mode'] = mode
    result['variance'] = np.var(data, ddof=0)
    result['standard_deviation'] = np.std(data, ddof=0)
    result['25th_percentile'] = np.percentile(data, 25)
    result['50th_percentile'] = np.percentile(data, 50)
    result['75th_percentile'] = np.percentile(data, 75)
    result['interquartile_range'] = result['75th_percentile'] - result['25th_percentile']
    return result