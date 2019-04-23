# E Goetz
# Basic implementation of the k-means clustering algorithm
from clusteringalgorithm import ClusteringAlgorithm
from random import uniform
from numpy import ndarray, zeros, array_equal


class KMeans(ClusteringAlgorithm):
    def __init__(self, data, answer_key):
        """
        Run the k-means algorithm on the given data.
        :param data: The set of data points to be clustered.
        """
        self.answer_key = answer_key
        self.generated_samples = data
        self.cluster_membership = None
        self.dimension_minimums = self.generated_samples[0].copy()
        self.dimension_maximums = self.generated_samples[0].copy()
        # get minimums and maximums for each dimension
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
        self.get_k()

    def __repr__(self):
        return "Generated samples:  \n {} \n" \
               "Cluster membership: {} \n"\
               "Feature/dimensional minimums: {} \n" \
               "Feature/dimensional maximums: {} \n" \
               "K: {} \n" \
               "Means: {} \n" \
               "Old means: {}".format(self.generated_samples,
                                      self.cluster_membership,
                                      self.dimension_minimums,
                                      self.dimension_maximums,
                                      self.k,
                                      self.means,
                                      self.old_means)

    def get_k(self):
        self.percent_error = None
        for k in range(1, len(self.generated_samples)):
            print("Trying k: {}".format(k))
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
                print("New Percent error: {}".format(current_error))
                print(self.answer_key)
                print(clusters)
                self.percent_error = current_error
                self.cluster_membership = clusters
                self.k = k
                if self.percent_error == 0:
                    return

    def initialize(self, k):
        """
        Initialize the k means to random values that are inclusively within
        the maximum range of the data points for every dimension.
        Precondition: the number of means, _k, has been selected.
        Postcondition: _means contains k random points within those of
        generated_samples.
        :return:
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
        Precondition: there are data points and k means.
        Postcondition: each member of _clusters contains a partition of
        generated_samples.
        :return:
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
        Precondition: _clusters is filled with partitions of generated_samples
        Postcondition: _means contains the means of the data points partitions
        contained in clusters.
        :return:
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
