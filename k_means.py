# E Goetz
# Basic implementation of the k-means clustering algorithm
from clusteringalgorithm import ClusteringAlgorithm
from random import uniform
from numpy import ndarray, zeros, array_equal


class KMeans(ClusteringAlgorithm):
    def __init__(self, data, answer_key, dimension_minimums=None,
                 dimension_maximums=None, verbose=False):
        """
        Cluster data using the k-means algorithm.
        :param data: the data set to be clustered
        :param answer_key: the expected clusters
        :param dimension_minimums: the smallest values of each dimension in the
        data set
        :param dimension_maximums: the largest values of each dimension in the
        data set
        :param verbose: whether to print progress messages
        """
        self.verboseprint(verbose, "Calling KMeans")
        self.answer_key = answer_key
        self.generated_samples = data
        self.cluster_membership = None
        self.dimension_minimums = dimension_minimums
        self.dimension_maximums = dimension_maximums
        # get minimums and maximums for each dimension
        if self.dimension_minimums is None or self.dimension_maximums is None:
            if self.dimension_minimums is None:
                self.dimension_minimums = self.generated_samples[0].copy()
            if self.dimension_maximums is None:
                self.dimension_maximums = self.generated_samples[0].copy()
            for point in self.generated_samples:
                for ith_dimension in range(len(point)):
                    if point[ith_dimension] < self.dimension_minimums[
                                                                ith_dimension]:
                        self.dimension_minimums[ith_dimension] = point[
                            ith_dimension]
                    elif point[ith_dimension] > self.dimension_maximums[
                                                                ith_dimension]:
                        self.dimension_maximums[ith_dimension] = point[
                            ith_dimension]
        self.verboseprint(verbose, "Found the minimal value for each data "
                                   "point dimension: {}".format(
                                    self.dimension_minimums))
        self.verboseprint(verbose, "Found the maximum value for each data "
                                   "point dimension: {}".format(
                                    self.dimension_maximums))
        self.get_k(verbose)

    def get_k(self, verbose):
        """
        Get the number of clusters or k that has the smallest percent error.
        :param verbose: whether to print progress messages
        :return: None
        :side effect: self.k, self.cluster_membership, and self.percent_error
        are set to the k, cluster_membership, and percent_error values of the
        clustering attempt with the smallest percent error.
        """
        self.percent_error = None
        for k in range(1, len(self.generated_samples)):
            self.verboseprint(verbose, "Setting k to {}".format(k))
            means = self.initialize(k)
            old_means = None
            clusters = None
            while old_means is None or not array_equal(means, old_means):
                clusters = self.assign(means)
                old_means = means.copy()
                means = self.update(k, clusters, old_means)
            current_error = self.get_percent_error(clusters, self.answer_key)
            if self.percent_error is None or self.percent_error > \
                     current_error:
                self.verboseprint(verbose, "\tNew Percent error: {}".format(
                    current_error))
                self.percent_error = current_error
                self.cluster_membership = clusters
                self.k = k
                if self.percent_error == 0:
                    return

    def initialize(self, k):
        """
        Initialize the k means to random values that are inclusively within
        the maximum range of the data points for every dimension.
        :return: An ndarray holding k random points with the same number of
        dimensions as the points in self.generated_samples
        """
        means = ndarray((k, len(self.generated_samples[0])))
        for cluster_k in range(k):
            for dimension in range(len(self.generated_samples[0])):
                means[cluster_k][dimension] = uniform(self.dimension_minimums[
                                                    dimension], self.
                                                dimension_maximums[dimension])
        return means

    def assign(self, means):
        """
        Assign all data points in the class to the closest mean.
        :return: An ndarray holding a number representing cluster membership
        for every point.
        """
        cluster_membership = ndarray((len(self.generated_samples),), dtype=
        int)
        for point_index in range(len(self.generated_samples)):
            minimum_distance = None
            cluster = None
            for mean_index in range(len(means)):
                distance = 0
                for i in range(len(self.generated_samples[point_index])):
                    distance += (means[mean_index][i] - self.
                                 generated_samples[point_index][i])**2
                distance = distance / 2
                if minimum_distance is None or distance < minimum_distance:
                    minimum_distance = distance
                    cluster = mean_index
            cluster_membership[point_index] = cluster
        return cluster_membership

    def update(self, k, clusters, old_means):
        """
        Update the k means to be the mean of the data points that
        are assigned to their cluster.
        :return: An ndarray holding k points that are the means of the k
        clusters
        """
        new_means = zeros((k, len(self.generated_samples[0])))
        cluster_sizes = zeros((k,))
        for point_index in range(len(self.generated_samples)):
            mean_index = clusters[point_index]
            cluster_sizes[mean_index] += 1
            for dimension in range(len(self.generated_samples[point_index])):
                new_means[mean_index][dimension] += self.generated_samples[
                    point_index][dimension]
        for mean_index in range(len(new_means)):
            if cluster_sizes[mean_index] != 0:
                new_means[mean_index] = new_means[mean_index] / cluster_sizes[
                    mean_index]
            else:
                new_means[mean_index] = old_means[mean_index]
        return new_means
