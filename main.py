from matplotlib.pyplot import scatter, subplot, show, cm
import data, dbscan, k_means


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


# Create
def main():
        """
        Obtains the clustering of all exemplar data sets listed in data.py and
        plot the clusters.
        :return: None
        :side effect: Graphs of the expected clustering, DBSCAN clustering, and
        k-means clustering of all exemplar data sets are generated.
        """
        exemplars = [(data.venn_diagram, data.venn_diagram_cluster_membership),
                     (data.proximity_exemplar,
                      data.proximity_exemplar_clustering),
                     (data.figure_ground_exemplar,
                      data.figure_ground_exemplar_clustering),
                     (data.moon_line, data.moon_line_clusters)]
        for exemplar, exemplar_clustering in exemplars:
                dbscan_clustering = dbscan.Dbscan(exemplar, exemplar_clustering
                                                  ).cluster_membership
                k_means_clustering = k_means.KMeans(exemplar,
                                                    exemplar_clustering
                                                    ).cluster_membership
        plot_exemplar(exemplar, exemplar_clustering, dbscan_clustering,
                      k_means_clustering)


if __name__ == "__main__":
        main()
