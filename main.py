# E Goetz
# Main program for running and graphing clustering algorithm
from matplotlib.pyplot import scatter, subplot, show, cm
import data
import dbscan
import k_means


def plot_exemplar(data_set, expected_clustering, dbscan_clustering,
                  k_means_clustering):
    """
    Make a set of three graphs showing the expected clustering for a data
    set, the clustering determined by DBSCAN, and the clustering determined
    by k-means.
    :param data_set: The set of points to be clustered
    :param expected_clustering: The clustering a person would produce
    :param dbscan_clustering: The clustering DBSCAN produces
    :param k_means_clustering: The clustering k-means produces
    :return: None.
    :side effect: A matplot scatter plot is created.
    """
    name_list = ["data set", "Desired Clustering", "DBSCAN Clustering",
                 "K-Means Clustering"]
    parameter_list = [data_set, expected_clustering, dbscan_clustering,
                      k_means_clustering]
    for i in range(1,4):
        subplot(3, 1, i, title=name_list[i])
        scatter(list(coordinate[0] for coordinate in data_set),
                list(coordinate[1] for coordinate in data_set),
                c=parameter_list[i], s=30,
                cmap=cm.Paired)
    show()


def main():
    """
    Prompt the user to choose which of the exemplar data sets listed in
    data.py they would like to cluster and if they would like the process
    to be verbose. Then clusters and graphs the specified data set.
    :return: None
    :side effect: Graphs of the expected clustering, DBSCAN clustering, and
    k-means clustering of the specified exemplar data set is generated.
    """
    selection = ""
    while selection not in ["1", "2", "3", "4", "5", "6"]:
        selection = input("Please enter the number of the data set you "
                          "would like to cluster:\n"
                          "1: good form exemplar\n"
                          "2: proximity exemplar\n"
                          "3: figure-ground exemplar\n"
                          "4: similarity exemplar\n"
                          "5: closure exemplar\n"
                          "6: continuity exemplar\n")
    selection = int(selection) - 1

    verbose = input("Verbose? (Y/n)")
    if verbose == "N" or verbose == "n":
        verbose = False
    else:
        verbose = True

    exemplars = [
                 (data.good_form_exemplar,
                  data.good_form_exemplar_clustering),
                 (data.proximity_exemplar,
                  data.proximity_exemplar_clustering),
                 (data.figure_ground_exemplar,
                  data.figure_ground_exemplar_clustering),
                 (data.similarity_exemplar,
                  data.similarity_exemplar_clustering),
                 (data.closure_exemplar, data.closure_exemplar_clustering),
                 (data.continuity_exemplar,
                  data.continuity_exemplar_clustering)]

    dbscan_clustering = dbscan.Dbscan(exemplars[selection][0],
                                      exemplars[selection][1],
                                      verbose=verbose
                                      ).cluster_membership
    k_means_clustering = k_means.KMeans(exemplars[selection][0],
                                        exemplars[selection][1],
                                        verbose=verbose
                                        ).cluster_membership
    plot_exemplar(exemplars[selection][0], exemplars[selection][1],
                  dbscan_clustering, k_means_clustering)


if __name__ == "__main__":
    main()
