from sklearn.datasets.samples_generator import *
from k_means import KMeans


def test_kmeans():
    """
    Test the k-means algorithm for expected error rate.
    :return: Number indicating whether the test was passed
    0 - Expected result. Test passed.
    1 - Unexpected result. Test failed because of high error rate.
    """
    X, y = make_blobs(n_samples=100, n_features=3, centers=2)
    kmeans_instance = KMeans(X)
    translations = dict()
    errors = 0
    total = 0
    for data_point in range(len(kmeans_instance._cluster_membership)):
        if not kmeans_instance._cluster_membership[data_point] in translations:
            translations[kmeans_instance._cluster_membership[data_point]] = y[
                data_point]
        elif translations[kmeans_instance._cluster_membership[data_point]] != \
                y[data_point]:
            errors += 1
        total += 1
    error_rate = errors / total
    print("Cluster error rate: {}".format(error_rate))
    if error_rate >= .05:
        return 1
    else:
        return 0
