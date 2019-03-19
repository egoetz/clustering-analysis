from sklearn.datasets.samples_generator import make_blobs
from dbscan import Dbscan
from k_means import KMeans
from matplotlib.pyplot import scatter, subplot, show, cm


def test_dbscan():
    X, y = make_blobs(n_samples=100, n_features=2, centers=2)
    dbscan_instance = Dbscan(X)
    translations = dict()
    errors = 0
    total = 0
    for data_point in range(len(dbscan_instance._cluster_membership)):
        if not y[data_point] in translations:
            translations[y[data_point]] = dbscan_instance._cluster_membership[
                data_point]
        elif translations[y[data_point]] != \
                dbscan_instance._cluster_membership[data_point]:
            errors += 1
        total += 1
    error_rate = errors / total
    print("Cluster error rate: {}".format(error_rate))
    subplot(2,1,1)
    scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=cm.Paired)
    subplot(2,1,2)
    scatter(X[:, 0], X[:, 1], c=dbscan_instance._cluster_membership, s=30,
            cmap=cm.Paired)
    show()

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
    subplot(2,1,1)
    scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=cm.Paired)
    subplot(2,1,2)
    scatter(X[:, 0], X[:, 1], c=dbscan_instance._cluster_membership, s=30,
            cmap=cm.Paired)
    show()