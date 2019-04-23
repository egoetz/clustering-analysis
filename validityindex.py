from abc import ABC, abstractmethod


class ValidityIndex(ABC):
    """
    The abstract base class for all validity indices.
    """
    @abstractmethod
    def __init__(self, data):
        """
        The abstract initalizer for all validity indices.
        :param data:
        """
        pass