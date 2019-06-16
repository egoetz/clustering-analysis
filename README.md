# clustering-analysis
An ongoing project designed to explore the properties of basic clustering algorithms.

# How to Use: **Black Box Understanding**
From terminal, `cd` into the `clustering-analysis` directory and run the following command:
```
python3 main.py
```

Once you have started the program, you will be presented with the following text:
```
Please enter the number of the data set you would like to cluster:
1: good form exemplar
2: proximity exemplar
3: figure-ground exemplar
4: similarity exemplar
5: closure exemplar
6: continuity exemplar
```
Enter the number of the dataset you would like to cluster. To examine these sets in more detail, explore the `data.py` file.

Afterwards, you will be prompted to choose whether you want the program to be verbose or not
```
Verbose? (Y/n)
```
If prompted to be verbose, then the program will print statements describing what clustering algorithm is being called, and with what parameters. If the percent error of the clusters as specified by a given parameter call is better than that of a previous parameter call, then the new percent error will be printed.

Once a number of parameters have been tried for each clustering algorithm, the program will create a graph of the desired clustering shown with the graphs of the clusters created by the various clustering algorithms (when percent error is minimized).

# How it Works: **White Box Understanding**
## The Clustering Algorithms 
### clusteringalgorithm.py
A file holding the abstract base class for all clustering algorithms. Included in order to provide design consistancy and to illustrate UML structure. Specifies the basic methods and fields of the class.
### dbscan.py
A file containing a naive implementation of the DBSCAN algorithm as defined by "A Density-Based Algorithm for Discovering Clustersin Large Spatial Databases with Noise." 
### k_means.py
A file containing a naive implementation of the K-means algorithm as elicitated in the paper "Least squares quantization in PCM" by S. P. Lloyd.
### tests.py
A file designed to run with pytest and to ensure that ClusteringAlgorithm's subclasses are functioning as expected. Because of the nature of clustering algorithms, the results of a subclass' tests must be analyzed manually--- the return value of any given test will default to zero.
## The Datasets
### data.py
A file containing a number of arrays that represent datasets. When plotted, each of these datasets act as an exemplar of one of Gestalt's principles.
## The Main Program
### main.py
When run, a file that allows a user to run clustering algorithms on a given dataset.
