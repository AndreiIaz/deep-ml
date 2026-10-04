def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    import numpy as np
    n = len(samples)
    values, counts = np.unique(samples, return_counts = True)
    counts = np.array(counts, dtype=np.float64) / n
    # counts /= n
    # PMF = list((values[i], counts[i]) for i in range(n))
    PMF = list(zip(values, counts))
    return PMF
    