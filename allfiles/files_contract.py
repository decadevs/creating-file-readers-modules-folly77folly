#  import ABC , abstractclass from abc
from abc import ABC, abstractmethod

class Files(ABC):

    def __init__(self, filename, mode = 'r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file         

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    # def __iter__(self):
    #     self.file = open (self.filename, self.mode)
    #     return self.file

    def __next__(self):
        for line in self.file:
            return line

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def read_first_two_lines(self):
        pass

    @abstractmethod
    def read_last_two_lines(self):
        pass
    
