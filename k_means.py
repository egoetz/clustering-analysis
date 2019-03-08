# E Goetz
# Basic implementation of the k-means clustering algorithm
from abstract_clustering import ClusteringAlgorithm
from random import uniform

class KMeans(ClusteringAlgorithm):
    def __init__(self, data):
        """

        :param data: The set of data points to be clustered.
        """
        self._data_points = data
        self._dimension_minimums = list()
        self._dimension_maximums = list()
        # get minimums and maximums for each dimension
        for point in _data_points:
            for ith_dimension in len(point):
                if point[ith_dimension] < _dimension_minimums[ith_dimension]:
                    _dimension_minimums[ith_dimension] = point[ith_dimension]
                elif point[ith_dimension] > _dimension_minimums[ith_dimension]:
                    _dimension_maximums[ith_dimension] = point[ith_dimension]
        # get the number of clusters
        self._k = getK(data)
        # get the starting means for each k
        self._means = initialize(_k)
        self._old_means = None
        while self._old_means is None or self._means != self._old_means:
            self._old_means = self._means



    def get_k(self):
        return 2


    def initialize(self):
        """
        Initializes the k means to random values that are inclusively within
        the maximum range of the data points for every dimension.
        Precondition: the number of means, _k, has been selected.
        Postcondition: _means contains k random points within those of
        _data_points.
        :return:
        """
        means = list()
        for cluster_k in range(self._k):
            means[cluster_k] = list()
            for dimension in len(self._dimension_minimums):
                means[cluster_k].append(uniform(self._dimension_minimums[
                                                    dimension], self.
                                                _dimension_maximums[dimension])
                                        )
        return means

    def assign(self):
        """
        Assign all data points in the class to the closest mean.
        Precondition: there are data points and k means.
        Postcondition: each member of _clusters contains a partition of
        _data_points.
        :return:
        """
        minimum_distance = None
        for point in self._data_points:
            distance = 0
            for i in len(point):
                distance += (self._means[i] + point[i])**2
            distance = distance / 2
            if minimum_distance is None or distance < minimum_distance:
                minimum_distance = distance
                cluster = i
            self._clusters[cluster].append(point)


    def update(self):
        """
        All of the k means are updated to be the mean of the data points that
        are assigned to their cluster.
        Precondition: _clusters is filled with partitions of _data_points
        Postcondition: _means contains the means of the data points partitions
        contained in clusters.
        :return:
        """
        for i in len(self._means):
            if len(self._means[i]) != 0:
                new_mean = self._clusters[i][0]
                for point in range(1, len(self._clusters[i])):
                    for dimension in len(point):
                        new_mean[dimension] += point[dimension]
                new_mean = new_mean / len(self._clusters[i])
                self.means[i] = new_mean
