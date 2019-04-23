# E Goetz
# Basic implementation of the DBSCAN clustering algorithm
from clusteringalgorithm import ClusteringAlgorithm
from numpy import ndarray, array_equal


class Dbscan(ClusteringAlgorithm):
    def __init__(self, data, answer_key):
        """
        Determine the best eps and min_pts values and their resulting clusters.
        :param data: The data to cluster.
        """
        self.generated_samples = data
        self.dimensions = len(data[0])
        self.max_distance = None
        self.min_distance = None
        for point1 in self.generated_samples:
            for point2 in self.generated_samples:
                if not array_equal(point1, point2):
                    distance = self.get_distance(point1, point2)
                    if self.max_distance is None or distance > \
                            self.max_distance:
                        self.max_distance = distance
                    if self.min_distance is None or distance < \
                            self.min_distance:
                        self.min_distance = distance
        self.cluster_membership = None
        self.eps = None
        self.min_pts = None
        self.cluster_membership = self.get_clusters(3, 2)
        self.s_dbw = None
        self.percent_error = None
        if len(self.generated_samples) < 10:
            self.number_of_eps_values = 10
        else:
            self.number_of_eps_values = len(self.generated_samples)
        for min_pts in range(2, len(self.generated_samples)):
            for multiplier in range(10): #self.number_of_eps_values)):
                epsilon = self.min_distance + ((self.max_distance -
                                                self.min_distance) / 10 *
                                               multiplier)
                print("Trying min pts: {} and eps: {}".format(min_pts,
                                                              epsilon))
                clusters = self.get_clusters(epsilon, min_pts)
                current_error = self.get_percent_error(clusters, answer_key)
                if self.percent_error is None or self.percent_error > \
                        current_error:
                    print("New Percent error: {}".format(current_error))
                    print(answer_key)
                    print(clusters)
                    self.percent_error = current_error
                    self.cluster_membership = clusters
                    if self.percent_error == 0:
                        return
                # centers = self.get_centers(clusters)
                # s_dbw = S_Dbw(self.generated_samples, clusters, centers)
                # if self.s_dbw is None or s_dbw.S_Dbw < self.s_dbw:
                #     self.s_dbw = s_dbw.S_Dbw

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
        cluster_membership = ndarray(shape=(len(self.generated_samples)
                                                  ,), dtype=int)
        for index in range(len(cluster_membership)):
            cluster_membership[index] = -1
        cluster_number = 0
        for start_point_index in range(len(cluster_membership)):
            if cluster_membership[start_point_index] == -1:
                density_reachable = [start_point_index]
                directly_density_reachable = list()
                new_points = 1
                while new_points != 0:
                    current_point_index = len(density_reachable) - new_points
                    new_points -= 1
                    for test_point_index in range(len(self.generated_samples
                                                      )):
                        if density_reachable[current_point_index] != \
                                test_point_index:
                            distance = 0
                            for dimension in range(len(self.generated_samples[
                                                           0])):
                                distance += (self.generated_samples[
                                                 density_reachable[
                                                     current_point_index]][
                                                 dimension] - self.
                                             generated_samples[
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
                connected_clusters = [cluster_number]
                for index in density_reachable:
                    if cluster_membership[index] != -1:
                        connected_clusters.append(cluster_membership[index])
                min_cluster_num = min(connected_clusters)
                for index in range(len(cluster_membership)):
                    if index in density_reachable or cluster_membership[
                            index] in connected_clusters:
                        cluster_membership[index] = min_cluster_num
                if min_cluster_num == cluster_number:
                    cluster_number += 1
        return cluster_membership

    def get_centers(self, clusters):
        cluster_number_to_center = dict()
        for point_index in range(len(clusters)):
            if clusters[point_index] in cluster_number_to_center:
                cluster_number_to_center[clusters[point_index]][0] += \
                    self.generated_samples[point_index]
                cluster_number_to_center[clusters[point_index]][1] += 1
            else:
                cluster_number_to_center[clusters[point_index]] = [
                    self.generated_samples[point_index], 1]
        for a_key in cluster_number_to_center.keys():
            cluster_number_to_center[a_key] = cluster_number_to_center[
                                                  a_key][0] / \
                                              cluster_number_to_center[a_key][
                                                  1]

        smallest_distances = ndarray(shape=(len(cluster_number_to_center),),
                                     dtype=float)
        centers = ndarray(shape=(len(cluster_number_to_center),), dtype=int)
        for cluster_number in range(len(cluster_number_to_center)):
            found_cluster_point = False
            for index in range(len(self.generated_samples)):
                if clusters[index] == cluster_number and \
                    (found_cluster_point == False or
                    get_distance(self.generated_samples[index],
                    cluster_number_to_center[cluster_number]) <
                     smallest_distances[cluster_number]):
                    centers[cluster_number] = index
                    smallest_distances[cluster_number] = get_distance(
                        self.generated_samples[index],
                    cluster_number_to_center[cluster_number])
                    found_cluster_point = True
        return centers
