#  import ABC , abstractclass from abc
from abc import ABC, abstractmethod
import pandas as pd

class Files(ABC):

    def __init__(self, filename):
        pass

    def __enter__(self):
        pass       

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def fetch_first_two_rows(self):
        pass

    @abstractmethod
    def fetch_last_two_rows(self):
        pass
    
