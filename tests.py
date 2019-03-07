from sklearn.datasets.samples_generator import *



def test_kmeans():
    X, y = make_blobs(n_samples=100, n_features=2, centers=2)
