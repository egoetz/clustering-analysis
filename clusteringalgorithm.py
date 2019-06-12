# E Goetz
# Abstract base class for clustering algorithms
from abc import ABC, abstractmethod
from numpy import ndarray
from itertools import permutations


class ClusteringAlgorithm(ABC):
    """
    An abstract base class for all clustering algorithms.
    """
    @abstractmethod
    def __init__(self, data):
        """
        Initialize clustering algorithm.
        :param data: The data set to be clustered
        """
        self.generated_samples = data
        pass

    @staticmethod
    def verboseprint(verbose, to_print):
        """
        Prints a message if verbose is True.
        :param verbose: Bool specifying whether to be verbose or not
        :param to_print: Message for a verbose program to print
        :return: None
        :side effect: If verbose is true, to_print is printed.
        """
        if verbose:
            print(to_print)

    @staticmethod
    def get_distance(point1, point2):
        """
        Get the Euclidean distance between two different points.
        :param point1: Point to get distance to point2
        :param point2: Point to get distance to point1
        :return: The Euclidean distance between point1 and point2
        """
        distance = 0
        for dimension in range(len(point1)):
            distance += (point1[dimension] - point2[dimension]) ** 2
        return distance

    @staticmethod
    def get_percent_error(clusters, answer_key):
        """
        Get the percent error of a clustering algorithm's clusters.
        :param clusters: The clusters as found by the clustering algorithm
        :param answer_key: The actual clusters
        :return: The percent error of the clustering algorithm's clusters
        """
        points_shared_between_clusters = ndarray(shape=(len(set(clusters)),
                                                        len(set(answer_key))),
                                                 dtype=int)
        for predicted_cluster_num in range(len(set(clusters))):
            for answer_key_cluster_num in range(len(set(answer_key))):
                points_shared_between_clusters[predicted_cluster_num][
                    answer_key_cluster_num] = 0
                for point in range(len(clusters)):
                    if clusters[point] == predicted_cluster_num and answer_key[
                     point] == answer_key_cluster_num:
                        points_shared_between_clusters[predicted_cluster_num][
                            answer_key_cluster_num] += 1
        greatest_matching_points = 0
        for cluster_match in permutations(range(len(set(clusters))),
                                          min(len(set(clusters)),
                                              len(set(answer_key)))):
            matching_points = 0
            for i in range(len(cluster_match)):
                matching_points += points_shared_between_clusters[
                    cluster_match[i]][i]
            if matching_points > greatest_matching_points:
                greatest_matching_points = matching_points
        error_rate = (len(clusters) - greatest_matching_points) / \
            len(clusters) * 100
        return error_rate
