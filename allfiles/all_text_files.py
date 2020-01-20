from files_contract import Files

class AllFiles(Files):

    def __init__(self, filename, mode ='r'):
        self.filename = filename
        self.mode = mode
        self.file = open(self.filename, self.mode)
        self.file = None
        self.firstTwoLines = []


    def __enter__(self):
        self.file  = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()        

    def __iter__(self):
        # self.file = open (self.filename, self.mode)
        return self

    def __next__(self):
        self.file = open(self.filename, self.mode)
        for line in self.file:
            return line

    def read_all(self):
        return self.file.read()

    def read_first_two_lines(self):
        data = self.file.readline()
        for number in range(2):
            self.firstTwoLines.append(data)
            data = self.file.readline()
        return self.firstTwoLines
            
    def read_last_two_lines(self):
        datas = self.file.readlines()
        tail = datas[-2:]
        return (''.join(tail))
