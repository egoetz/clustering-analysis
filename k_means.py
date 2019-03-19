# E Goetz
# Basic implementation of the k-means clustering algorithm
from abstract_clustering import ClusteringAlgorithm
from random import uniform
from numpy import ndarray, zeros, array_equal


class KMeans(ClusteringAlgorithm):
    def __init__(self, data):
        """
        Run the k-means algorithm on the given data.
        :param data: The set of data points to be clustered.
        """
        self._generated_samples = data
        self._cluster_membership = None
        self._dimension_minimums = self._generated_samples[0].copy()
        self._dimension_maximums = self._generated_samples[0].copy()
        # get minimums and maximums for each dimension
        for point in self._generated_samples:
            for ith_dimension in range(len(point)):
                if point[ith_dimension] < self._dimension_minimums[
                                                                ith_dimension]:
                    self._dimension_minimums[ith_dimension] = point[
                        ith_dimension]
                elif point[ith_dimension] > self._dimension_maximums[
                                                                ith_dimension]:
                    self._dimension_maximums[ith_dimension] = point[
                        ith_dimension]
        self._k = self.get_k()
        self._means = self.initialize()
        self._old_means = None
        while self._old_means is None or not array_equal(self._means, self.
                                                         _old_means):
            self._cluster_membership = self.assign()
            self._old_means = self._means.copy()
            self._means = self.update()

    def __repr__(self):
        return "Generated samples:  \n {} \n" \
               "Cluster membership: {} \n"\
               "Feature/dimensional minimums: {} \n" \
               "Feature/dimensional maximums: {} \n" \
               "K: {} \n" \
               "Means: {} \n" \
               "Old means: {}".format(self._generated_samples,
                                      self._cluster_membership,
                                      self._dimension_minimums,
                                      self._dimension_maximums,
                                      self._k,
                                      self._means,
                                      self._old_means)

    def get_k(self):
        return 2

    def initialize(self):
        """
        Initialize the k means to random values that are inclusively within
        the maximum range of the data points for every dimension.
        Precondition: the number of means, _k, has been selected.
        Postcondition: _means contains k random points within those of
        _generated_samples.
        :return:
        """
        means = ndarray((self._k,len(self._generated_samples[0])))
        for cluster_k in range(self._k):
            for dimension in range(len(self._generated_samples[0])):
                means[cluster_k][dimension] = uniform(self._dimension_minimums[
                                                    dimension], self.
                                                _dimension_maximums[dimension])
        return means

    def assign(self):
        """
        Assign all data points in the class to the closest mean.
        Precondition: there are data points and k means.
        Postcondition: each member of _clusters contains a partition of
        _generated_samples.
        :return:
        """
        cluster_membership = ndarray((len(self._generated_samples),), dtype=
        int)
        for point_index in range(len(self._generated_samples)):
            minimum_distance = None
            cluster = None
            for mean_index in range(len(self._means)):
                distance = 0
                for i in range(len(self._generated_samples[point_index])):
                    distance += (self._means[mean_index][i] - self.
                                 _generated_samples[point_index][i])**2
                distance = distance / 2
                if minimum_distance is None or distance < minimum_distance:
                    minimum_distance = distance
                    cluster = mean_index
            cluster_membership[point_index] = cluster
        return cluster_membership

    def update(self):
        """
        Update the k means to be the mean of the data points that
        are assigned to their cluster.
        Precondition: _clusters is filled with partitions of _generated_samples
        Postcondition: _means contains the means of the data points partitions
        contained in clusters.
        :return:
        """
        new_means = zeros((self._k, len(self._generated_samples[0])))
        cluster_sizes = zeros((self._k,))
        for point_index in range(len(self._generated_samples)):
            mean_index = self._cluster_membership[point_index]
            cluster_sizes[mean_index] += 1
            for dimension in range(len(self._generated_samples[point_index])):
                new_means[mean_index][dimension] += self._generated_samples[
                    point_index][dimension]
        for mean_index in range(len(new_means)):
            if cluster_sizes[mean_index] != 0:
                new_means[mean_index] = new_means[mean_index] / cluster_sizes[
                    mean_index]
            else:
                new_means[mean_index] = self._means[mean_index]
        return new_means
