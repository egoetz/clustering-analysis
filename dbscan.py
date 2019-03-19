# E Goetz
# Basic implementation of the DBSCAN clustering algorithm
from abstractclustering import ClusteringAlgorithm
from numpy import ndarray


class Dbscan(ClusteringAlgorithm):
    def __init__(self, data):
        """
        Determine the best eps and min_pts values and their resulting clusters.
        :param data: The data to cluster.
        """
        self._generated_samples = data
        self._cluster_membership = None
        self._eps = None
        self._min_pts = None
        self._cluster_membership = self.get_clusters(3, 2)

    def get_clusters(self, eps, min_pts):
        """
        Find the clusters produced by the given eps and min_pts values.
        :param eps: Epsilon. The maximum distance that can occur between two
        points for them to be considered directly density reachable.
        :param min_pts: The minimum number of points within epsilon distance
        that a point must have in order to be considered a core point (and its
        epsilon neighborhood to be considered part of that point's cluster).
        :return: array indicating cluster membership.
        """
        cluster_membership = ndarray(shape=(len(self._generated_samples)
                                                  ,), dtype=int)
        for index in range(len(cluster_membership)):
            cluster_membership[index] = -1
        cluster_number = 1
        for start_point_index in range(len(cluster_membership)):
            if cluster_membership[start_point_index] == -1:
                density_reachable = [start_point_index]
                directly_density_reachable = list()
                new_points = 1
                while new_points != 0:
                    current_point_index = len(density_reachable) - new_points
                    new_points -= 1
                    for test_point_index in range(len(self._generated_samples
                                                      )):
                        if density_reachable[current_point_index] != \
                                test_point_index:
                            distance = 0
                            for dimension in range(len(self._generated_samples[
                                                           0])):
                                distance += (self._generated_samples[
                                                 density_reachable[
                                                     current_point_index]][
                                                 dimension] - self.
                                             _generated_samples[
                                    test_point_index][dimension])**2
                            if distance <= eps:
                                directly_density_reachable.append(
                                    test_point_index)
                    if len(directly_density_reachable) >= min_pts:
                        to_delete = list()
                        for index in directly_density_reachable:
                            if index in density_reachable:
                                to_delete.append(index)
                        for index in to_delete:
                            directly_density_reachable.remove(index)
                        density_reachable.extend(directly_density_reachable)
                        new_points += len(directly_density_reachable)
                    directly_density_reachable.clear()
                connected_clusters = list()
                for index in density_reachable:
                    if cluster_membership[index] != -1:
                        connected_clusters.append(cluster_membership[index])
                for index in range(len(cluster_membership)):
                    if index in density_reachable or cluster_membership[
                            index] in connected_clusters:
                        cluster_membership[index] = cluster_number
                cluster_number += 1
        return cluster_membership
