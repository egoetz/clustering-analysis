# E Goetz
# test file for clustering algorithm implementations
from sklearn.datasets.samples_generator import make_blobs
from dbscan import Dbscan
from k_means import KMeans
from matplotlib.pyplot import scatter, subplot, show, cm


def test_dbscan():
    """
    Test the DBSCAN algorithm is clustering as expected.
    :return: None.
    :Side effect: Graph generated showing actual clustering and DBSCAN
    clustering. The program runner must determine if the DBSCAN clustering
    indicates the DBSCAN algorithm is correct or not.
    """
    X, y = make_blobs(n_samples=100, n_features=2, centers=2)
    print("calling dbscan class")
    dbscan_instance = Dbscan(X, y)
    translations = dict()
    print("Cluster error rate: {}".format(dbscan_instance.percent_error))
    subplot(2,1,1)
    scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=cm.Paired)
    subplot(2,1,2)
    scatter(X[:, 0], X[:, 1], c=dbscan_instance._cluster_membership, s=30,
            cmap=cm.Paired)
    show()


def test_kmeans():
    """
    Test the k-means algorithm is clustering as expected.
    :return: None.
    :Side effect: Graph generated showing actual clustering and k-means
    clustering. The program runner must determine if the k-means clustering
    indicates the k-means algorithm is correct or not.
    """
    X, y = make_blobs(n_samples=100, n_features=3, centers=2)
    kmeans_instance = KMeans(X, y)
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
    scatter(X[:, 0], X[:, 1], c=kmeans_instance._cluster_membership, s=30,
            cmap=cm.Paired)
    show()
