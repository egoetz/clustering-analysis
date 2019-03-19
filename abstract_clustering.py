from abc import ABC, abstractmethod


class ClusteringAlgorithm(ABC):
    @abstractmethod
    def __init__(self, data):
        pass
