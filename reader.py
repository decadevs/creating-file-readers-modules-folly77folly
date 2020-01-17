import abc

#file object as a context manager
class OpenFile():

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self): 
        self.file = open(self.filename, self.mode) 
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.file.close()
    
# class for my interface contract
class ContractInterface(abc.ABC):
    @abc.abstractmethod
    def read_last_two_lines(self):
        pass

    @abc.abstractmethod
    def readall(self):
        pass

# class to read opened file
class ReadFile(ContractInterface):
    def __init__(self, file_descriptor):
        self.fd= file_descriptor
        self.read_file = []
        self.firstTwoLines = []

    def readall(self):
        for line in self.fd:
            self.read_file.append(line)
        return self.read_file

    def read_first_two_lines(self):
        count = 0
        for line in self.fd:
            count += 1
            self.read_file.append(line)
            if count == 2:
                return self.read_file

        
    def read_last_two_lines(self):
        # for line in self.fd:
        #     return self.fd
        # # return self.read_file



class iterate_through_file:
    def __init__(self, file_descriptor):
        self.fd = file_descriptor

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.fd:
            return line




      

with OpenFile('iris.csv') as file_obj:
    abc=ReadFile(file_obj)
    print(abc.read_last_two_lines())
        







