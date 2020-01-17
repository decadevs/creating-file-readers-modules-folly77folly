# import pandas as p

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
    

# class to read opened file
class ReadFile:
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
        with open(self.filename) as f:
            data = f.readlines()
            tail = data[-2:]
            two_tails = ''.join(tail) 
            return two_tails



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
    print(abc.read_first_two_lines())
        







