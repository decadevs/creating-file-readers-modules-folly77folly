
# class ContextManager():
import abc
from abc import ABC


class MyInterface(abc.ABC):

    @abc.abstractmethod
    def read_two_lines():
        pass

    @abc.abstractmethod
    def read_last_two_lines():
        pass

#file object as a context manager
class ReadBytesFromFile(MyInterface):

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = open(self.filename, self.mode) 

    def __enter__(self): 
        self.file = open(self.filename, self.mode) 
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.file.close()
    
    def __iter__(self):
        return self

    def __next__(self):
        for a in self:
            yield a
    
    def readall(self):
        return self.file.read()

    def read_two_lines(self):
        with open(self.filename) as myfile:
            head = [next(myfile) for x in range(2)]
            return(head)
        
    def read_last_two_lines(self):
        with open(self.filename) as f:
            data = f.readlines()
            tail = data[-2:]
            two_tails = ''.join(tail) 
            return two_tails  


readthings = ReadBytesFromFile('README.md')
print(readthings.read_two_lines())



